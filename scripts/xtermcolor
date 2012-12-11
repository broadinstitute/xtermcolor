import sys, argparse
from xtermcolor.ColorMap import XTermColorMap, VT100ColorMap

def cPrintfString(xterm):
  return '"\\033[38;5;{xterm:d}m%s\\033[0m"'.format(xterm=xterm)

def Cli():
  parser = argparse.ArgumentParser(
              description = 'xtermcolor: 256 terminal color library')

  parser.add_argument('action',
              choices = ['convert', 'list'],
              help = 'Actions')

  parser.add_argument('--color',
              help = 'Color to convert')

  parser.add_argument('--compat',
              choices=['xterm', 'vt100'],
              default='xterm',
              help = 'Compatibility mode.  Defaults to xterm.')

  cli = parser.parse_args()

  if cli.compat.lower() not in ['xterm', 'vt100']:
    sys.stderr.write('Error: --compat must be xterm or vt100\n')
    sys.exit(-1)
  
  if cli.compat.lower() == 'xterm':
    colorMap = XTermColorMap()
  if cli.compat.lower() == 'vt100':
    colorMap = VT100ColorMap()

  if cli.action == 'list':
    for xterm, hexcolor in colorMap.getColors().items():
      string = "\033[38;5;{xterm:d}mansi={xterm:d}; rgb=#{hexcolor:06x}; printf={cprintf:s}\033[0m"
      print(string.format(xterm=xterm, hexcolor=hexcolor, cprintf=cPrintfString(xterm)));

  if cli.action == 'convert':
    if not cli.color:
      sys.stderr.write('Error: must specify --color\n')
      sys.exit(-1)
    if cli.color[0] == '#':
      cli.color = '0x' + cli.color[1:]
    cli.color = int(cli.color, 16)
    
    colorizedMsg = colorMap.colorize('The quick brown fox jumped over the lazy dog.', cli.color)
    (ansi, rgb) = colorMap.convert(cli.color)
    print("#{start:06x} is closest to #{closest:06x} which is ANSI code {ansi:d}\n".format( \
          start=cli.color, closest=rgb, ansi=ansi))
    print("Example: " + colorizedMsg)
    print("printf() string: " + cPrintfString(ansi))
