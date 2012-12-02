from os import isatty, environ, write

from xtermcolor.ColorMap import XTermColorMap, VT100ColorMap

def _colorize(string, rgb=None, ansi=None,bg=None,ansi_bg=None,xterm=True):
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
    if xterm != _colorize.xterm:
        _colorize.xterm = xterm
        if xterm:
            _colorize.cmap = XTermColorMap()
        else:
            _colorize.cmap = VT100ColorMap()
    return _colorize.cmap.colorize(string,rgb,ansi,bg,ansi_bg)

_colorize.xterm = True
_colorize.cmap = XTermColorMap()

def colorize(string, rgb=None, ansi=None,bg=None,ansi_bg=None,fd=1):
    '''Returns the colored string to print on the terminal.
    
    This function detects the terminal type and if it is supported and the
    output is not going to a pipe or a file, then it will return the colored
    string, otherwise it will return the string without modifications.
    
    string = the string to print. Only accepts strings, unicode strings must
             be encoded in advance.
    rgb    = Rgb color for the text; for example 0xFF0000 is red.
    ansi   = Ansi for the text
    bg     = Rgb color for the background
    ansi_bg= Ansi color for the background
    fd     = The file descriptor that will be used by print, by default is the
             stdout
    '''
    
    #Reinitializes if fd used is different
    if colorize.fd != fd:
        colorize.init = False
    
    #Checks if it is on a terminal, and if the terminal is recognized
    if not colorize.init:
        colorize.init = True
        colorize.is_term = isatty(fd)
        if 'TERM' in environ:
            if environ['TERM'] == 'xterm':
                colorize.xterm = True
            elif environ['TERM'] == 'vt100':
                colorize.xterm = False
            else:
                colorize.is_term = False
        else:
            colorize.is_term = False
    
    if colorize.is_term:
        string=_colorize(string,rgb,ansi,bg,ansi_bg,colorize.xterm)

    return string
colorize.init = False
colorize.fd = 1