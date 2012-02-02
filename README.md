Installation
============

With pip

```bash
$ pip install xtermcolor
```

Using setup.py

```bash
$ python setup.py install
```

Command Line Usage
==================

    $ xtermcolor --help
    usage: xtermcolor [-h] [--color COLOR] [--compat {xterm,vt100}] {convert,list}

    xtermcolor: 256 terminal color library

    positional arguments:
      {convert,list}        Actions

    optional arguments:
      -h, --help            show this help message and exit
      --color COLOR         Color to convert
      --compat {xterm,vt100}
                            Compatibility mode. Defaults to xterm.


Python Module Usage
===================

```python
>>> from xtermcolor.ColorMap import XTermColorMap, VT100ColorMap
>>> cmap = XTermColorMap()
>>> print(cmap.colorize('Hello World', 0x00ffec))
Hello World
```