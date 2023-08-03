ARG PYTHON_VERSION
FROM mcr.microsoft.com/devcontainers/python:${PYTHON_VERSION}

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=root

# Python and poetry installation
USER $USER
ARG HOME="/root"

RUN apt update \
    && apt -y install enchant-2

# COPY ./.devcontainer/root/rc.sh /etc/profile.d/10bashrc.sh
COPY ./.devcontainer/root/bashrc_custom.sh $HOME/.bashrc_custom

ENV LANG=C.UTF-8 \
    PYENV_ROOT="${HOME}/.pyenv"

ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /workspace/python_rst_scratch
COPY ./pyproject.toml ./poetry.lock ./

RUN poetry config virtualenvs.in-project true \
    && poetry install $(test "$RUN_ENV" == production && echo "--no-dev") --no-interaction --no-ansi --no-root --no-cache

# Cannot persist python version into build here so, get the python version and run all the commands the use it.
RUN MY_PY_VER=$(python -c "import sys; major, minor = sys.version_info[:2]; print(f'{major}.{minor}');" ) \
    && echo "Python version: $MY_PY_VER" \
    && echo "/workspace/python_rst_scratch" >> "/workspace/python_rst_scratch/.venv/lib/python$MY_PY_VER/site-packages/python_rst_scratch.pth"

ENV VIRTUAL_ENV=/workspace/python_rst_scratch/.venv \
    PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./.devcontainer/startup.sh /usr/local/bin/startup.sh
RUN chmod +x "/usr/local/bin/startup.sh"