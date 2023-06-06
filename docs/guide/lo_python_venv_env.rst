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

With packages such as types-scriptforge_ working on a `ScripForge` project can be done in the IDE as well with type checking and auto completion.

This guide assumes you have a reasonable exposure to Python as well as you have some familiarity with LibreOffice application suite.
It contains some Python code samples that are meant to be run in the LibreOffice Python environment.


Creating a LibreOffice Python Virtual Environment is different on other operating systems.

Windows
-------

:ref:`guide_windows_manual_venv` is a guide on how to create a LibreOffice Python Virtual Environment on Windows manually.

The basic steps to create a LibreOffice Python Virtual Environment on Windows are:

1. Find out the version of python for LibreOffice you are using.
2. Install the same version of python on your system using tools such as pyenv-win_.
3. Activate the matching python version installed with pyenv-win_.
4. Create a virtual environment for you project using ``python -m venv`` or Poetry_.
5. Set the virtual environment to use the LibreOffice python installation with tools such as oooenv_.

OR

Alternatively use |pre_cfg|_.

Matching Python Version and LibreOffice Python Version is crucial when using package the have binary dependencies.

Pre-Configured Virtual Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting with the most simple way to get a LibreOffice Python Virtual Environment on Windows.
There are pre-configured virtual environments available for download at |pre_cfg|_.

These virtual environments are created for usage with pip_.

Follow the instruction on the |pre_cfg|_ page to download and install the virtual environment.

A simplified version of the instructions is:

1. Create a directory for your project.
2. Download the virtual environment zip that matches your LibreOffice python version into your project folder.
3. Extract the zip into the project folder ( extracted to ``.venv`` ).
4. Activate the virtual environment by running ``.\.venv\Scripts\activate.ps1`` (PowerShell).
5. Update pip_ ``pip install --upgrade pip``
6. Update oooenv_ ``pip install --upgrade oooenv``
7. Run ``oooenv update --update`` to update the virtual environment to the current version of LibreOffice python.

Manually Creating a Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As mentioned above the basic steps to create a LibreOffice Python Virtual Environment manually are more complex.
This has much to do with the fact that LibreOffice Python is not a standard python installation it is an embedded python.

1. Finding out the version of python for LibreOffice you are using.

.. code-block:: powershell

    &"C:\Program Files\LibreOffice\program\python.exe" --version

Gets a result something like: ``Python 3.8.16``

2. Install the same version of python on your system using tools such as pyenv-win_.

This is out of scope for this guide, but there are many resources on the internet on how to do this.


.. _types-scriptforge: https://pypi.org/project/types-scriptforge/
.. _pyenv-win: https://pypi.org/project/pyenv-win/
.. _poetry: https://python-poetry.org/
.. _oooenv: https://pypi.org/project/oooenv/
.. _pip: https://pypi.org/project/pip/

.. |pre_cfg| replace:: Pre-configured virtual environments for LibreOffice on Windows
.. _pre_cfg: https://github.com/Amourspirit/lo-support_file/tree/main/virtual_environments/windows