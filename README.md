# RST Scratch project

Simple enough! A project for editing rst files in VS Code

## Documents

The built document example can be found on [Read the Docs](https://rst-scratch-project.readthedocs.io/en/latest/index.html)

## Install

It is assumed <https://github.com/Amourspirit/python_rst_scratch> has been cloned or unzipped to a folder.

### Virtual Environment

[Poetry](https://python-poetry.org/) is required to install this project.

See [Configuring a Poetry environment](https://rst-scratch-project.readthedocs.io/en/latest/poetry/index.html).

Once Poetry is installed simple run `poetry install` in the root of the project.

```sh
poetry install
```

Start VS Code

```sh
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
