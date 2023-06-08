# DIAGNOSIS BACKEND SYSTEM

[![diagnosis CI](https://github.com/horlali/diagnosis-backend/actions/workflows/diagnosis-ci.yml/badge.svg)](https://github.com/horlali/diagnosis-backend/actions/workflows/diagnosis-ci.yml)
[![codecov](https://codecov.io/gh/horlali/diagnosis-backend/branch/main/graph/badge.svg?token=PYZ7F49U17)](https://codecov.io/gh/horlali/diagnosis-backend)

Personalized fashion redesigned

## Getting Started

Clone repository to your local and navigate into the folder

```bash
git clone https://github.com/horlali/diagnosis-backend
cd diagnosis-backend/
```

Build and start the application with docker-compose
Obtain or create necessary environment files

```bash
./script/run-docker.sh  --dev
```

To run the application in production mode run the script with the `--prod` flag

```bash
./scripts/run-docker --prod
```

You can also add the `-d` flag to run the docker container as a daemon

```bash
./scripts/run-docker --prod -d
```

## Known issues

- Due to the disparity in how windows and linux handle line ending you might run into a line ending error which cause the container to fail on start up. See likely error below.

```bash
diagnosis-api | exec ./scripts/run-server.sh: no such file or directory
```

To fix the error run the following command in the project root.

```bash
sed -i -e 's/\r$//' scripts/*
```

This should fix the issues. Rerun `./script/run-docker.sh --dev` to start the application

## Application Docs

## Dev Toolchain

- [docker](https://www.docker.com/) containerization
- [python ^3.11](https://www.python.org/) main programming language
- [poetry](https://python-poetry.org/) for dependency management
- [black](https://github.com/psf/black) for code styling
- [isort](https://pycqa.github.io/isort/) for import sorting styling
- [flake8](https://flake8.pycqa.org/en/latest/) for linting

In the `scripts/` folder there are 3 scripts that can be used to check and correct formatting, styling and standards problems `run-black.sh`, `run-flake8.sh`, `run-isort.sh`. The scripts will only check by default, if you would like to correct the errors you need to pass the `--fix` option. If you are using `zsh` and got some errors, consider execution via `bash`

## Setup Local Environment

```bash
poetry install
poetry shell
```

## Running tests

In the root of the repository `:~/diagnosis-backend` run the scripts below

```bash
./scripts/run-tests.sh
```

## Running linters

In the root of the repository `:~/diagnosis-backend` run the scripts below

```bash
./scripts/run-black.sh # add --fix flag to fix black formatting issues
./scripts/run-isort.sh # add --fix flag to fix isort linting issues
./scripts/run-flake8.sh
```

or yo can simply run all the linters by using the `run-linters.sh` scripts

```bash
./scripts/run-linters.sh # add --fix flag to automatically fix linting and formatting issues
```

## Sample Request

Once the application is up and running, visit <http://127.0.0.1:8000/> or <localhost:8000> or in your browser

You should see a Swagger Documentation Page like this

![Alt text](screenshots/home.png)
