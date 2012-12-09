from os import isatty, environ, write

from xtermcolor.ColorMap import XTermColorMap, VT100ColorMap

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
        colorize.fd = fd
    
    #Checks if it is on a terminal, and if the terminal is recognized
    if not colorize.init:
        colorize.init = True
        colorize.is_term = isatty(fd)
        if 'TERM' in environ:
            if environ['TERM'].startswith('xterm'):
                colorize.cmap = XTermColorMap()
            elif environ['TERM'] == 'vt100':
                colorize.cmap = VT100ColorMap()
            else:
                colorize.is_term = False
        else:
            colorize.is_term = False
    
    if colorize.is_term:
        string = colorize.cmap.colorize(string,rgb,ansi,bg,ansi_bg)

    return string
colorize.init = False
colorize.fd = 1
