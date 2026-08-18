"""
Lab 04 - Reverse Engineering using Python's built-in dis module.
Disassembles real functions from Project.py into their bytecode
representation, and shows cross-references (which names/functions
each function calls) via co_names -- the Python-native equivalent
of IDA's disassembly + cross-reference analysis.

This file lives in a subfolder (root/RR/dis_demo.py), while
Project.py lives in the project root -- so the parent directory is
added to sys.path before importing.
"""

import os
import sys

# Add the parent folder (project root, where Project.py lives) to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dis
from Project import _hash, register_user, _find_reservation_by_user_id

print("=" * 60)
print("DISASSEMBLY: _hash()")
print("=" * 60)
dis.dis(_hash)

print("\n" + "=" * 60)
print("DISASSEMBLY: _find_reservation_by_user_id()")
print("=" * 60)
dis.dis(_find_reservation_by_user_id)

print("\n" + "=" * 60)
print("CROSS-REFERENCES: names referenced by register_user()")
print("=" * 60)
print(register_user.__code__.co_names)