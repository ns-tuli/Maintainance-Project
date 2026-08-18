"""
Lab 01 - Static Analysis using the Python ast module
Parses the REAL Project.py file directly (not reconstructed snippets)
and extracts three real nodes from its actual AST.
"""

import ast
import sys

# Project.py itself contains Unicode box-drawing characters (e.g. the "==="
# banner in main()). Windows terminals default to the cp1252 codepage for
# both reading and printing, which can't handle those characters. Force
# UTF-8 for stdout the same way Project.py itself already does.
if sys.platform.startswith("win"):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

with open("Project.py", "r", encoding="utf-8") as f:
    source = f.read()

tree = ast.parse(source, filename="Project.py")


# -- Example 1: Simple Expression --------------------------------------------
# The real ID-generation line inside register_user() (Project.py, line 135):
#     user_id = max((u["id"] for u in users), default=0) + 1
print("=" * 60)
print("EXAMPLE 1: Simple Expression (real Assign+BinOp node, line 135)")
print("=" * 60)
for node in ast.walk(tree):
    if isinstance(node, ast.Assign) and isinstance(node.value, ast.BinOp) and node.lineno == 135:
        print(ast.dump(node, indent=2))
        break


# -- Example 2: Loop and List -------------------------------------------------
# The real loop inside view_centers() (Project.py, line 326):
#     for c in centers: ...
print("\n" + "=" * 60)
print("EXAMPLE 2: Loop and List (real For node, line 326, inside view_centers())")
print("=" * 60)
for node in ast.walk(tree):
    if isinstance(node, ast.For) and node.lineno == 326:
        print(ast.dump(node, indent=2))
        break


# -- Example 3: Function Definition -------------------------------------------
# The real _hash() function definition, extracted directly from Project.py
print("\n" + "=" * 60)
print("EXAMPLE 3: Function Definition (real _hash() node from Project.py)")
print("=" * 60)
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == "_hash":
        print(ast.dump(node, indent=2))
        break