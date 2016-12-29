#!/bin/sh

echo "Project contains $(cat *.py | sed '/\s*#/d;/^\s*$/d' | wc -l) lines of code\n"

echo "Executing all tests:"
py.test *_test.py

