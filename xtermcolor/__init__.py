from xtermcolor.ColorMap import XTermColorMap, VT100ColorMap


def colorize(string, rgb=None, ansi=None,bg=None,ansi_bg=None,xterm=True):
    if xterm != colorize.xterm:
        colorize.xterm = xterm
        if xterm:
            colorize.cmap = XTermColorMap()
        else:
            colorize.cmap = VT100ColorMap()
    return colorize.cmap.colorize(string,rgb,ansi,bg,ansi_bg)

colorize.xterm = True
colorize.cmap = XTermColorMap()