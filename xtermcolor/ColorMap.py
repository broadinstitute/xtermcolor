class TerminalColorMapException(Exception):
  pass

colors = {}

def _compute():
  grayscale_start = 0x08
  grayscale_end = 0xf8
  grayscale_step = 10
  
  primary = [0x000000, 0x800000, 0x008000, 0x808000, 0x000080, 0x800080, 0x008080, 0xc0c0c0]

  bright = [0x808080, 0xff0000, 0x00ff00, 0xffff00, 0x0000ff, 0xff00ff, 0x00ffff, 0xffffff]
  
  intensities = [0x00, 0x5F, 0x87, 0xAF, 0xD7, 0xFF]
  
  for index, color in enumerate(primary + bright):
    colors[index] = color

  c = 16
  for i in intensities: 
    color = i << 16;
    for j in intensities: 
      color &= ~(0xff << 8);
      color |= j << 8;
      for k in intensities: 
        color &= ~0xff;
        color |= k;
        colors[c] = color
        c += 1

  c = 232    
  for hex in list(range(grayscale_start, grayscale_end, grayscale_step)):
    color = (hex << 16) | (hex << 8) | hex;
    colors[c] = color
    c += 1

def _rgb(color):
  return ((color >> 16) & 0xff, (color >> 8) & 0xff, color & 0xff)

def _diff(color1, color2):
  (r1, g1, b1) = _rgb(color1)
  (r2, g2, b2) = _rgb(color2)
  return abs(r1-r2) + abs(g1-g2) + abs(b1-b2)

def _convert(hexcolor):
  diffs = {}
  for xterm, rgb in colors.items():
    diffs[_diff(rgb, hexcolor)] = xterm
  minDiffAnsi = diffs[min(diffs.keys())]
  return (minDiffAnsi, colors[minDiffAnsi])
    
def colorize(string, rgb=None, ansi=None,bg=None,ansi_bg=None):
  if rgb is None and ansi is None:
    raise TerminalColorMapException('colorize: must specify one named parameter: rgb or ansi')
  if rgb is not None and ansi is not None:
    raise TerminalColorMapException('colorize: must specify only one named parameter: rgb or ansi')
  if bg is not None and ansi_bg is not None:
    raise TerminalColorMapException('colorize: must specify only one named parameter: bg or ansi_bg')
  
  
  if len(colors)==0:
      _compute()
      pass
  
  if rgb != None:
    (closestAnsi, closestRgb) = _convert(rgb)
  elif ansi != None:
    (closestAnsi, closestRgb) = (ansi, colors[ansi])
  
  if bg == None and ansi_bg == None:
      return "\033[38;5;{ansiCode:d}m{string:s}\033[0m".format(ansiCode=closestAnsi, string=string)
  
  if bg != None:
      (closestBgAnsi,unused) = _convert(bg)
  elif ansi_bg != None:
      (closestBgAnsi,unused) = (ansi_bg, colors[ansi_bg])

  return u"\033[38;5;{ansiCode:d}m\033[48;5;{bf:d}m{string:s}\033[0m".format(ansiCode=closestAnsi,bf=closestBgAnsi, string=string)
    
class TerminalColorMap:
  def getColors(self, order='rgb'):
    return colors
  def convert(self, hexcolor):
    return _convert(hexcolor);
  def colorize(self, string, rgb=None, ansi=None,bg=None,ansi_bg=None):
      return colorize(string,rgb,ansi,bg,ansi_bg)
  def rgb(self, color):
      return _rgb(self, color)
  def diff(self, color1, color2):
      return _diff(color1,color2)
class VT100ColorMap(TerminalColorMap):
  def __init__(self):
    self._compute()

  def _compute(self):
    primary = [0x000000, 0x800000, 0x008000, 0x808000, 0x000080, 0x800080, 0x008080, 0xc0c0c0]
    bright = [0x808080, 0xff0000, 0x00ff00, 0xffff00, 0x0000ff, 0xff00ff, 0x00ffff, 0xffffff]
    
    for index, color in enumerate(primary + bright):
      colors[index] = color

class XTermColorMap(VT100ColorMap):
  def _compute(self):
    _compute()
