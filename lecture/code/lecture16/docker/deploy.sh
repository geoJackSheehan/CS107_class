#!/usr/bin/env bash
set -e

# Always update this if you made changes to the Dockerfile
TAG=1.0.2

export BUILDAH_FORMAT=docker
docker build \
    -t "iacs/cs107_lecture16:${TAG}" \
    -t "iacs/cs107_lecture16:latest" .

docker login docker.io
docker push "iacs/cs107_lecture16:${TAG}"
docker push "iacs/cs107_lecture16:latest"

docker rmi -f iacs/cs107_lecture16:${TAG}
