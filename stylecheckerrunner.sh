#!/usr/bin/env bash
isort
black . --diff
pylint app/