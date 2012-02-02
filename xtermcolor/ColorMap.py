class TerminalColorMapException(Exception):
  pass

class TerminalColorMap:
  def getColors(self, order='rgb'):
    return self.colors

  def rgb(self, color):
    return ((color >> 16) & 0xff, (color >> 8) & 0xff, color & 0xff)

  def diff(self, color1, color2):
    (r1, g1, b1) = self.rgb(color1)
    (r2, g2, b2) = self.rgb(color2)
    return abs(r1-r2) + abs(g1-g2) + abs(b1-b2)

  def convert(self, hexcolor):
    diffs = {}
    for xterm, rgb in self.colors.items():
      diffs[self.diff(rgb, hexcolor)] = xterm
    minDiffAnsi = diffs[min(diffs.keys())]
    return (minDiffAnsi, self.colors[minDiffAnsi])

  def colorize(self, string, rgb=None, ansi=None):
    if rgb is None and ansi is None:
      raise TerminalColorMapException('colorize: must specify one named parameter: rgb or ansi')
    if rgb is not None and ansi is not None:
      raise TerminalColorMapException('colorize: must specify only one named parameter: rgb or ansi')

    if rgb:
      (closestAnsi, closestRgb) = self.convert(rgb)
    elif ansi:
      (closestAnsi, closestRgb) = (ansi, self.colors[ansi])

    return "\033[38;5;{ansiCode:d}m{string:s}\033[0m".format(ansiCode=closestAnsi, string=string)

class VT100ColorMap(TerminalColorMap):
  primary = [
    0x000000, 0x800000, 0x008000, 0x808000, 0x000080, 0x800080, 0x008080, 0xc0c0c0
  ]

  bright = [
    0x808080, 0xff0000, 0x00ff00, 0xffff00, 0x0000ff, 0xff00ff, 0x00ffff, 0xffffff
  ]

  def __init__(self):
    self.colors = dict()
    self._compute()

  def _compute(self):
    for index, color in enumerate(self.primary + self.bright):
      self.colors[index] = color

class XTermColorMap(VT100ColorMap):
  grayscale_start = 0x08;
  grayscale_end = 0xf8;
  grayscale_step = 10;
  intensities = [
    0x00, 0x5F, 0x87, 0xAF, 0xD7, 0xFF
  ]

  def _compute(self):
    for index, color in enumerate(self.primary + self.bright):
      self.colors[index] = color

    c = 16
    for i in self.intensities: 
      color = i << 16;
      for j in self.intensities: 
        color &= ~(0xff << 8);
        color |= j << 8;
        for k in self.intensities: 
          color &= ~0xff;
          color |= k;
          self.colors[c] = color
          c += 1

    c = 232    
    for hex in list(range(self.grayscale_start, self.grayscale_end, self.grayscale_step)):
      color = (hex << 16) | (hex << 8) | hex;
      self.colors[c] = color
      c += 1
