#!/bin/bash

input_file='test/data/christmas.jpeg'
thumb_size=25

generate_mosaic() {
    echo "Creating $2..."
    "./photomosaic.py" -i "$input_file" \
        -s "$1" \
        -t "$thumb_size" \
        -o "$2"
}

cd "$(dirname "$0")/.."

generate_mosaic 'none' 'test/data/out/mosaic_no_image.jpeg'
