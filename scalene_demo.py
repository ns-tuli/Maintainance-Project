"""
Lab 01 - Dynamic Analysis using the Scalene Profiler
Generates a memory- and CPU-intensive workload by exercising real
functions from the Vaccination Scheduling System (Project.py):
_hash(), _valid_email(), _valid_phone(), _valid_national_id()
"""

from Project import _hash, _valid_email, _valid_phone, _valid_national_id


def generate_bulk_users(n):
    """Simulates bulk user registration validation + password hashing."""
    users = []
    for i in range(n):
        email = f"user{i}@example.com"
        phone = f"+2010{i % 10000000:07d}"
        national_id = str(10000000000000 + i)
        password = f"password{i}"

        if _valid_email(email) and _valid_phone(phone) and _valid_national_id(national_id):
            hashed = _hash(password, "demo_salt")
            users.append({
                "id": i,
                "email": email,
                "phone": phone,
                "national_id": national_id,
                "password": hashed,
            })
    return users


def process_users(users):
    """Simulates a post-processing pass over all validated users."""
    return [u["password"].upper() for u in users]


def calculate_stats(users):
    """Simulates a reporting pass, similar to list_users_and_reservations()."""
    return len(users)


users = generate_bulk_users(200000)
processed = process_users(users)
total = calculate_stats(users)

print(f"Total users generated: {total}")
print(f"Sample processed hash: {processed[0]}")
