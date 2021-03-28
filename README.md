# backgrounder

A tool to configure your macOS desktop backgrounds via the command-line.

---

Requires Python 3.6+.

```shell script
$ python3 -m venv ./venv
$ source ./venv/bin/activate # or activate.csh or activate.fish
$ pip install -r requirements-dev.txt
$ pip install -r requirements.txt
$ python3 -m backgrounder
```

Other commands:

## CLI

```shell script
$ python3 -m backgrounder --help
```

```shell script
usage: backgrounder [-h] [-s SPACES] [-i IMAGE] [-r]

Haphazardly change desktop backgrounds.

optional arguments:
  -h, --help            show this help message and exit
  -s SPACES, --spaces SPACES
                        number of spaces to change
  -i IMAGE, --image IMAGE
                        the path to your background image
  -r, --random          chooses a desktop picture at random
```

The main CLI entry point; see `--help`.

Basic usage is as follows:

```shell script
# Change the current desktop's background to a random OS image
$ python3 -m backgrounder --random

# Change the first 2 desktop backgrounds
$ python3 -m backgrounder --random --spaces 2

# Have an image in mind? Provide the path.
$ python3 -m backgrounder --image /System/Library/Desktop\ Pictures/Big\ Sur.heic
```

## Misc. Scripts

```shell script
$ make
```

An overall wrapper for the below two commands
* Type checking and linting invoked with `mypy` via rules that live inside `.mypy.ini`.
* Formatting invoked via `yapf` via rules that live inside `script/format`.

```shell script
$ make format
```

Keeping things tidy.

```shell script
$ make lint
```

Keeping things type-checked and linted.

---

You may notice that there are multiple `requirements*.txt` files. They are split apart so that the dependencies install easily.

| filename                  | why                                          |
| ------------------------- | -------------------------------------------- |
| `requirements.txt`        | Common runtime dependencies                  |
| `requirements-dev.txt`    | Development dependencies – mypy, yapf, etc   |
