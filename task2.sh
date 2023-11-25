#!/bin/bash

#Problem was that the python interpreter was interpreting the entire string
#as a file path and trying to open it, which leads to an error.
#To execute Python code directly from a string stored in an environment 
#variable, you can use the -c option with the Python interpreter.
#the -c option allows you to specify the
#Python code as a command-line argument.
#double quotes around $PYCODE are necessary 
#to preserve the spaces and special characters in the Python code.

python3 -c "$PYCODE"