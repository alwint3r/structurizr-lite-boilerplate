#!/bin/bash

src_files=$(ls diagrams/*.d2)

# for each file in $src_files
for file in $src_files
do
    # get the filename without the extension
    filename=$(basename "$file")
    filename="${filename%.*}"

    # convert the file to png
    python3 d2_preprocess.py $file && \
    d2 $file out/$filename.png
done