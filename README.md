xtermcolor is a convenient python module for quickly colorizing text for output to the terminal either via ANSI color code or RGB color value.  Support 256 colors!

![xtermcolor list](https://github.com/broadinstitute/xtermcolor/raw/master/img/list.png)

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

To convert an RGB value to a printf() string or the closest ANSI color code, use `xtermcolor convert` as follows:

![xtermcolor convert](https://github.com/broadinstitute/xtermcolor/raw/master/img/convert.png)

Python Module Usage
===================

Simply import the `colorize` function from the `xtermcolor` module and use as follows:

![xtermcolor module](https://github.com/broadinstitute/xtermcolor/raw/master/img/module.png)
