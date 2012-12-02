from xtermcolor.ColorMap import XTermColorMap, VT100ColorMap

def colorize(string, rgb=None, ansi=None,bg=None,ansi_bg=None,xterm=True):
    '''Returns the colored string to print on the terminal.
    
    string = the string to print. Only accepts strings, unicode strings must
             be encoded in advance.
    rgb    = Rgb color for the text; for example 0xFF0000 is red.
    ansi   = Ansi for the text
    bg     = Rgb color for the background
    ansi_bg= Ansi color for the background
    xterm  = True by default, if False, escape codes for VT100 terminal will
             be generated.
    '''
    if xterm != colorize.xterm:
        colorize.xterm = xterm
        if xterm:
            colorize.cmap = XTermColorMap()
        else:
            colorize.cmap = VT100ColorMap()
    return colorize.cmap.colorize(string,rgb,ansi,bg,ansi_bg)

colorize.xterm = True
colorize.cmap = XTermColorMap()

