"""
Lab 01 - Static Analysis using the Python ast module
Three examples, each built from real logic inside Project.py.
"""

import ast

# ── Example 1: Simple Expression ───────────────────────────────────────────
# Based on the ID-generation line used in register_user() / add_or_remove_center()
# e.g. Project.py line 135: user_id = max((u["id"] for u in users), default=0) + 1
print("=" * 60)
print("EXAMPLE 1: Simple Expression (ID assignment)")
print("=" * 60)
code1 = "new_id = max_id + 1"
tree1 = ast.parse(code1)
print(ast.dump(tree1, indent=2))


# ── Example 2: Loop and List ────────────────────────────────────────────────
# Based on view_centers() in Project.py, which loops over each center's
# vaccine list and prints it
print("\n" + "=" * 60)
print("EXAMPLE 2: Loop and List (vaccine listing)")
print("=" * 60)
code2 = """
vaccines = ["Pfizer", "Moderna"]
name = "Center A"
for v in vaccines:
    print("{} offers {}".format(name, v))
"""
tree2 = ast.parse(code2)
print(ast.dump(tree2, indent=2))


# ── Example 3: Function Definition ──────────────────────────────────────────
# The actual _hash() function from Project.py
print("\n" + "=" * 60)
print("EXAMPLE 3: Function Definition (_hash from Project.py)")
print("=" * 60)
code3 = """
def _hash(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

hashed = _hash("mypassword", "somesalt")
print(hashed)
"""
tree3 = ast.parse(code3)
print(ast.dump(tree3, indent=2))
