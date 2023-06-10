# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# import os
import sys
from pathlib import Path

_DOCS_PATH = Path(__file__).parent
_ROOT_PATH = _DOCS_PATH.parent
sys.path.insert(0, str(_ROOT_PATH))

project = "RST Scratch"
copyright = "2022-2023, Scratch Editor"
author = "Scratch Editor"
release = "0.1.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_toolbox.collapse",
    "sphinx_toolbox.more_autodoc.autonamedtuple",
    "sphinx_toolbox.more_autodoc.typevars",
    "sphinx_toolbox.more_autodoc.autoprotocol",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_tabs.tabs",
    "sphinx_design",
    "sphinxcontrib.spelling",
    "sphinx_copybutton",
]

# "sphinx.ext.linkcode",
# sphinx_tabs.tabs docs: https://sphinx-tabs.readthedocs.io/en/latest/

# "sphinx_design"
# https://sphinx-design.readthedocs.io/en/rtd-theme/get_started.html

# region spelling
# https://sphinxcontrib-spelling.readthedocs.io/en/latest/


def get_spell_dictionaries() -> list:
    p = _DOCS_PATH.absolute().resolve() / "internal" / "dict"
    dict_gen = p.glob("spelling_*.*")
    return [str(d) for d in dict_gen if d.is_file()]


spelling_word_list_filename = get_spell_dictionaries()

spelling_show_suggestions = True
spelling_ignore_pypi_package_names = True
spelling_ignore_contributor_names = True
spelling_ignore_acronyms = True

# https://sphinxcontrib-spelling.readthedocs.io/en/latest/customize.html
spelling_exclude_patterns = [".venv/"]

# spell checking;
#   run sphinx-build -b spelling . _build
#       this will check for any spelling and create folders with *.spelling files if there are errors.
#       open each *.spelling file and find any spelling errors and fix them in corresponding files.
#
# spelling_code.txt contains all spelling exceptions related to python doc strings.

# endregion spelling

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"]
if html_theme == "sphinx_rtd_theme":
    html_css_files.append("css/readthedocs_custom.css")

if "sphinx_rtd_dark_mode" in extensions:
    html_css_files.append("css/readthedocs_dark.css")

html_css_files.append("css/style_custom.css")

html_js_files = [
    "js/custom.js",
]

# Napoleon settings
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_google_docstring = True
napoleon_include_init_with_doc = True

# https://fossies.org/linux/Sphinx/doc/usage/extensions/autodoc.rst
# This value controls how to represent typehints. The setting takes the following values:
autodoc_typehints = "description"

# see: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_mock_imports
# see: https://read-the-docs.readthedocs.io/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
autodoc_mock_imports = []

# autodoc_type_aliases
# The key of each entry is the type hint as written in the source,
# the value is how it will be written in the generated documentation.
# autodoc_type_aliases = {
#     "Column": "Column",
#     "DictRow": "DictRow",
#     "DocOrCursor": "DocOrCursor",
#     "DocOrText": "DocOrText",
#     "FloatList": "FloatList",
#     "FloatTable": "FloatTable"
# }
autodoc_type_aliases = {}
autodoc_typehints_format = "short"

# https://stackoverflow.com/questions/9698702/how-do-i-create-a-global-role-roles-in-sphinx
# custom global roles or any other rst to include

# sphinx includes s5defs.txt that has baked in roles but must be included.
# style_custom.css contains the colors that match these roles
# https://stackoverflow.com/questions/3702865/sphinx-restructuredtext-set-color-for-a-single-word/60991308#60991308

# https://pypi.org/project/sphinx-copybutton/
# copybutton_exclude = '.linenos, .gp, .go'
copybutton_prompt_text = r">>> ?|\.\.\. ?|\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True


rst_prolog_lst = [
    ".. include:: <s5defs.txt>",
    "",
]
# rst_prolog_lst.append(f".. |app_ver| replace:: {__version__}\n")

# add extra roles for custom theme colors.
# unlike the colors style_custom.css, these colors can be change by
# changing colors css vars that start with -t-color-
rst_prolog = ""

if html_theme == "sphinx_rtd_theme":
    with open("roles/theme_color_roles.txt", "r") as file:
        rst_prolog += file.read()
        rst_prolog += "\n"

with open("roles/custom_roles.txt", "r") as file:
    rst_prolog += file.read()
    rst_prolog += "\n"


rst_prolog += "\n" + "\n".join(rst_prolog_lst)

rst_prolog_lst = [
    ".. include:: <s5defs.txt>",
    "",
    ".. role:: event(doc)",
    "",
    ".. role:: eventref(ref)",
    "",
    ".. |app_name| replace:: OOO Development Tools",
    "",
    ".. |app_name_bold| replace:: **OOO Development Tools**",
    "",
    ".. |odev| replace:: OooDev",
    ".. _odev: https://python-ooo-dev-tools.readthedocs.io/en/latest/index.html",
    "",
    ".. |ooouno| replace:: ooouno library",
    ".. _ooouno: https://pypi.org/project/ooouno/",
    "",
]
rst_prolog += "\n" + "\n".join(rst_prolog_lst)

# set if figures can be referenced as numbers. Default is False
numfig = True

# set is todo's will show up.
# a master list of todo's will be on bottom of main page.
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#module-sphinx.ext.todo
todo_include_todos = False

# https://documentation.help/Sphinx/extlinks.html
# extlinks = {}
