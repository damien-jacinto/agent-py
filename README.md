# agent-py

## Requirements

- Python 3.X
- virtualenv [intall](https://virtualenv.pypa.io/en/latest/installation.html)

## Run project

```sh
make environment
make help
make run
```

## Configuration

Environment variable:

- ENV: local/dev/prod
- VERSION: app version, default 1.0.0, endpoint /version
- DESCRIPTION: app description

local : enable reload mode (default)
prod : disable api doc

## Usage

Run project with `make run` and consult url in log for api doc at `/docs` or `/redoc`.

Application is running 2 threads, one for the API to expose metrics and one for collecting metrics.

