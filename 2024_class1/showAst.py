#!/usr/bin/env python3
import ast

with open("m.py", "r") as fp:
    contents = fp.read()

print(ast.dump(ast.parse(contents), indent=4))