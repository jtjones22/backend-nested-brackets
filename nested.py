#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "???"

import sys


def is_nested(line):
    """Validate a single input line for correct nesting"""
    openers = ("(", "(*", "[", "{", "<")
    closers = (")", "*)", "]", "}", ">")
    stack = []
    index = 0
    balanced = True
    while line:
        current_char = line[0]
        if line.startswith("(*"):
            current_char = "(*"
        elif line.startswith("*)"):
            current_char = "*)"
        index += 1
        line = line[len(current_char):]
        if current_char in openers:
            stack.append(current_char)
        elif current_char in closers:
            if len(stack) == 0:
                balanced = False
                break
            elif stack[-1] == openers[closers.index(current_char)]:
                stack.pop()
            else:
                balanced = False
                break
    if balanced and len(stack) == 0:
        return "YES\n"
    else:
        return "NO {}\n".format(index)
    balanced = True


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open("input.txt", "r") as f:
        with open("output.txt", "w") as w_f:
            text = f.readlines()
            for line in text:
                result = is_nested(line)
                w_f.write(str(result))


if __name__ == '__main__':
    main(sys.argv[1:])
