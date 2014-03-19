XTermColor: Easy Terminal Colors
================================

XTermColor is a convenient python module for quickly colorizing text for output to the terminal either via ANSI color code or RGB color value.  Support 256 colors!

![xtermcolor list](https://github.com/broadinstitute/xtermcolor/raw/master/img/list.png)

Installation
------------

With [pip](http://www.pip-installer.org/en/latest/)

```bash
$ pip install xtermcolor
```

Or, via `easy_install`:

```bash
$ easy_install xtermcolor
```

Or, Using `setup.py` from the project directory

```bash
$ python setup.py install
```

Command Line Usage
------------------

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
-------------------

Simply import the `colorize` function from the `xtermcolor` module.  `colorize()` is always called with a string as the first argument, but has a number of keyword arguments that can be specified:

* `rgb` - String of the RGB color value to color the text as.
* `ansi` - Integer value of the ANSI color code.
* `bg` - String of the RGB color value for the background color.
* `ansi_bg` - Integer value of ANSI color code for background color.
* `fd` - File descriptor that will be used to print the text.  Defaults to stdout.

arguments `rgb` and `ansi` are mutually exclusive, as are `bg` and `ansi_bg`.

![xtermcolor module](https://github.com/broadinstitute/xtermcolor/raw/master/img/module.png)
