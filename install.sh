#!/bin/bash

echo "Starting installation of dlmv..."

# Ensure the script is executable
chmod +x dlmv.py

# Move the script to /usr/local/bin
sudo cp dlmv.py /usr/local/bin/dlmv

echo "Installation complete! You can now run 'dlmv' from the terminal."
