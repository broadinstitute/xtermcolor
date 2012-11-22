from xtermcolor.ColorMap import XTermColorMap, VT100ColorMap

def colorize(string, rgb=None, ansi=None,bg=None,ansi_bg=None,xterm=True):
    if xterm:
        cmap = XTermColorMap()
    else:
        cmap = VT100ColorMap()
    return cmap.colorize(string,rgb,ansi,bg,ansi_bg)