#!/bin/bash

# 1. Activate the virtual environment
# We check if the folder exists and handle the Windows/Linux naming difference
if [ -d "venv/Scripts" ]; then
    source venv/Scripts/activate
elif [ -d "venv/bin" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found!"
    exit 1
fi

# 2. Execute the test suite
# We use 'python -m pytest' to be safe about pathing
python -m pytest test_app.py

# 3. Return the correct exit code
# $? stores the exit code of the last command (pytest)
TEST_RESULT=$?

if [ $TEST_RESULT -eq 0 ]; then
    echo "CI SUCCESS: All tests passed."
    exit 0
else
    echo "CI FAILURE: Tests failed with exit code $TEST_RESULT."
    exit 1
fi