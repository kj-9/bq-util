# bq-util

[![PyPI](https://img.shields.io/pypi/v/bq-util.svg)](https://pypi.org/project/bq-util/)
[![Changelog](https://img.shields.io/github/v/release/kj-9/bq-util?include_prereleases&label=changelog)](https://github.com/kj-9/bq-util/releases)
[![Tests](https://github.com/kj-9/bq-util/actions/workflows/test.yml/badge.svg)](https://github.com/kj-9/bq-util/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/kj-9/bq-util/blob/master/LICENSE)



## Installation

Install this tool using `pip`:

    pip install bq-util

## Usage

For help, run:

    bq-util --help

You can also use:

    python -m bq_util --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd bq-util
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test,dev]'

To run the tests:

    pytest
