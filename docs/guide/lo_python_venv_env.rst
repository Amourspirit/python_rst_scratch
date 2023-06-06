.. _lo_python_venv_env:

LibreOffice Python Virtual Environment
======================================

.. contents:: Table of Contents
    :local:
    :backlinks: top
    :depth: 2

Overview
--------

In the context of this guide a LibreOffice Python environment is a Python runtime environment that is configured to be used with LibreOffice.
It is used to run Python script in LibreOffice and to automate LibreOffice directly.

A LibreOffice Python virtual environment also can be a way to develop more complex python macros for LibreOffice in a full blown IDE like Vs Code or PyCharm.
With all the advantages of source control, testing and debugging. Tools such as |odev|_ can be leveraged to run and debug the python code in the IDE as used directly in LibreOffice.
Also the python code can be run in the IDE without the need to start LibreOffice manually.
There are numerous other advantages of using a Virtual Environment and an IDE for development, but this is not the focus of this guide.

With packages such as ooo-dev_tools_ ("OooDev") and types-scriptforge_ it is possible to develop LibreOffice python macros in a full blown IDE if type checking and auto completion is desired.

This guide assumes you have a reasonable exposure to Python as well as you have some familiarity with LibreOffice application suite.
It contains some Python code samples that are meant to be run in the LibreOffice Python environment.

Creating a LibreOffice Python Virtual Environment is different on other operating systems.

Windows
-------

Guides
^^^^^^

See the following Guides:

- :ref:`guide_windows_manual_venv`
- :ref:`guide_windows_poetry_venv`
- :ref:`guide_lo_pip_windows_install`
- :ref:`guide_lo_portable_pip_windows_install`
- :ref:`guide_pip_via_zaz_pip`
- :ref:`guide_zaz_pip_installation`

Pre-Configured Virtual Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are also pre-configured virtual environments available for download at |pre_cfg|_.
These virtual environments are created for usage with pip_.
Follow the instruction on the |pre_cfg|_ page to download and install the virtual environment.

Short version of the instructions:

1. Create a directory for your project.
2. Download the virtual environment zip that matches your LibreOffice python version into your project folder.
3. Extract the zip into the project folder ( extracted to ``.venv`` ).
4. Activate the virtual environment by running ``.\.venv\Scripts\activate.ps1`` (PowerShell).
5. Update pip_ ``pip install --upgrade pip``
6. Update oooenv_ ``pip install --upgrade oooenv``
7. Run ``oooenv update --update`` to update the virtual environment to the current version of LibreOffice python.


.. _types-scriptforge: https://pypi.org/project/types-scriptforge/
.. _pyenv-win: https://pypi.org/project/pyenv-win/
.. _poetry: https://python-poetry.org/
.. _oooenv: https://pypi.org/project/oooenv/
.. _pip: https://pypi.org/project/pip/

.. |pre_cfg| replace:: Pre-configured virtual environments for LibreOffice on Windows
.. _pre_cfg: https://github.com/Amourspirit/lo-support_file/tree/main/virtual_environments/windows
.. _ooo-dev_tools: https://pypi.org/project/ooo-dev-tools/