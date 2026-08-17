"""
Lab 01 - Dynamic Analysis using sys.settrace()
Traces real functions from the Vaccination Scheduling System project:
_valid_email() and _hash() from Project.py
"""

import os
import sys
from Project import _valid_email, _hash

# Only trace frames belonging to our own files (Project.py and this file),
# not the internals of Python's re/hashlib modules.
OWN_FILES = {
    os.path.abspath("Project.py"),
    os.path.abspath(__file__),
}


def my_tracer(frame, event, arg=None):
    code = frame.f_code
    if os.path.abspath(code.co_filename) not in OWN_FILES:
        return None  # don't trace into standard-library internals
    func_name = code.co_name
    line_no = frame.f_lineno
    print(f"A {event} event encountered in {func_name}() at line number {line_no}")
    return my_tracer


def check_registration(email, password):
    """Mimics the validation step inside register_user() from Project.py."""
    is_valid = _valid_email(email)
    hashed_password = _hash(password, "demo_salt")
    return is_valid, hashed_password


sys.settrace(my_tracer)  # START tracing
result = check_registration("student@iut-dhaka.edu", "mypassword123")
sys.settrace(None)       # STOP tracing

print("\nResult:", result)
