#!/bin/bash

# Directory where screenshots will be saved
SAVE_DIR="$HOME/Pictures/screenshots"

# Create the directory if it doesn't exist
mkdir -p "$SAVE_DIR"

# Generate a unique filename based on the current timestamp
FILENAME=$(date +'Shot__%Y-%m-%d__%H-%M-%S').png

# Full path to save the screenshot
FULL_PATH="$SAVE_DIR/$FILENAME"

# Take a screenshot of the entire screen
import -window root "$FULL_PATH"

