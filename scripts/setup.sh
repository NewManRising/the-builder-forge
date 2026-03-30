#!/bin/bash
# The Builder Forge — Project Setup Script
# Run this after cloning to set up the development environment

echo "Setting up The Builder Forge..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 not found. Install it first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate and install dependencies
echo "Installing dependencies..."
source .venv/bin/activate
pip install -r requirements.txt --quiet

# Run environment check
echo ""
python scripts/hello_forge.py

echo ""
echo "Setup complete. Run 'source .venv/bin/activate' to start working."