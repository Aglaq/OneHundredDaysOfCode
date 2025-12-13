#!/bin/bash

# Check if the user provided a day number
if [ -z "$1" ]; then
    echo "Usage: ./new_day.sh <day_number>"
    exit 1
fi

DAY="Day$1"

# Create the folder
mkdir -p "$DAY"
cd "$DAY" || exit

echo "Created folder: $DAY"

# Create virtual environment
python3 -m venv .venv
echo "Virtual environment created."

# Create main.py
echo 'print("Hello from Day '$1'!")' > main.py
echo "Created main.py"

# Activate venv
source .venv/bin/activate
echo "Virtual environment activated."

# Upgrade pip
python -m pip install --upgrade pip > /dev/null
echo "Pip upgraded."

# Open VS Code in this folder
code .

echo "-----------------------------------------------------"
echo "Day $1 is ready!"
echo "Now in VS Code, press CMD + SHIFT + P"
echo "Choose: Python: Select Interpreter"
echo "Then select: .venv/bin/python"
echo "-----------------------------------------------------"
