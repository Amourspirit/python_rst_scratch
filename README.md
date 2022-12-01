# RST Scratch project

Simple enough! A project for editing rst files in VS Code

## Install

### Virtual Environment

It is assumed <https://github.com/Amourspirit/python_rst_scratch> has been cloned or unzipped to a folder.

[Poetry](https://python-poetry.org/) is required to install this project.

### Linux

```sh
$ python -m venv ./.venv
```

Activate virtual environment.

```sh
source ./.venv/bin/activate
```

Install requirements using Poetry.

```sh
(.venv) $ poetry install
```

Start VS Code

```sh
code .
```

### Windows

Start by using terminal to create a `.venv` environment in the projects root folder

```ps
PS C:\python_rst_scratch> python -m venv .\.venv
```

Activate Virtual environment.

```ps
PS C:\python_rst_scratch> .\.venv\Scripts\Activate
```

Install requirements using Poetry.

```ps
(.venv) PS C:\python_rst_scratch> poetry install
```

```ps
code .
```

## Quick start rst edit

Add a file to `docs/scratch` and edit.

Optionally just edit `docs/scratch/scratch.rst`

## Live Preview

For live preview install extension [reStructuredText Language Support for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext)

## HTML Server (localhost)

A localhost html server can be started if needed.

Defaults to port 8000

```sh
python ./dev_cmds/run_http.py
```

Optionally a port can be passed to script.

```sh
python ./dev_cmds/run_http.py 8081
```
