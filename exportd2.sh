#!/bin/bash

docker run -it --rm -v `pwd`:/usr/local/structurizr structurizr/cli:latest export \
    -workspace /usr/local/structurizr/src/workspace.dsl \
    -format d2 \
    -output /usr/local/structurizr/diagrams