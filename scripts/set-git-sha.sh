#!/bin/bash

# Get the current git SHA
GIT_SHA=$(git rev-parse --short HEAD)

# Export it as an environment variable
export GIT_SHA

# Run Hugo with the environment variable
hugo server -D 