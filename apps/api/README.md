# API

# Contributing

## Local environment setup

### Prerequisite

- [pyenv](https://github.com/pyenv/pyenv)
- [poetry](https://github.com/python-poetry/poetry)

Install required python version and set it as local

```bash
$ pyenv install 3.9.9
$ pyenv local 3.9.9
```

Create virtualenv with the local python version

```bash
$ poetry env use $(pyenv which python)
```

Install project required packages

```bash
$ poetry install
```

Activate virtualenv

```bash
$ poetry shell
```

## Code verification

### Prerequisite

- [tox](https://github.com/tox-dev/tox)
- [pipx](https://github.com/pypa/pipx)

```bash
$ pipx install tox
```

Before pushing changes one need to check if the code meets the project's requirements:

```bash
$ tox -p auto
```
