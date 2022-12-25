#!/usr/bin/env bash
set -e
export BUILDAH_FORMAT=docker
docker build -t 'iacs/cs107_lecture16:latest' .
