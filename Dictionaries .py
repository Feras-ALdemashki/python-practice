# =========================
# Python Dictionaries Practice (Quests)
# =========================

users = {
    "u1001": {
        "name": "Amina",
        "age": 27,
        "email": "amina@example.com",
        "active": True,
        "roles": ["user", "editor"],
        "address": {"city": "Amsterdam", "country": "NL"},
        "scores": [88, 91, 73],
    },
    "u1002": {
        "name": "Luca",
        "age": 34,
        "email": "luca@example.com",
        "active": False,
        "roles": ["user"],
        "address": {"city": "Rotterdam", "country": "NL"},
        "scores": [100, 67],
    },
    "u1003": {
        "name": "Mei",
        "age": 19,
        "email": "mei@example.com",
        "active": True,
        "roles": ["user", "admin"],
        "address": {"city": "Utrecht", "country": "NL"},
        "scores": [],
    },
}

# -------------------------
# Level 1: Access + basics
# -------------------------

# 1) Print Mei’s email.
mei_email = users["u1003"]["email"]
print(mei_email)
# 2) Print Luca’s city.
Luca_city= users["u1002"]["address"]["city"]
print(Luca_city)
# 3) Print all user IDs (the keys of users).
for user_id in users:
    print(user_id)
# 4) Print the names of all users.
for user_id in users.values():
    print(user_id["name"])
# 5) Print whether u1002 is active.
if users["u1002"]["active"]:
    print("yes its active")
else:
    print("its not active")
# -------------------------
# Level 2: Update + add + delete
# -------------------------

# 6) Set u1002 to active (True).
    users["u1002"].update(active=True)
    print(users["u1002"]["active"])
# 7) Add a new score 95 to Amina’s scores.
# 8) Add a new field "phone": "+31 6 12345678" to u1001.
# 9) Remove the "email" field from u1003 (only for that user).
# 10) Add a brand-new user u1004 with the same structure (use your own values).

# -------------------------
# Level 3: Loops + filtering
# -------------------------

# 11) Print names of only active users.
# 12) Print user IDs of everyone who has the role "admin".
# 13) Print names of users living in Amsterdam.
# 14) Create a list of emails of active users (skip users if "email" is missing).
# 15) Count how many users are inactive.

# -------------------------
# Level 4: Computations
# -------------------------

# 16) For each user, compute their average score.
#     If a user has no scores, the average should be None.
#
#     Output example (format can differ):
#     averages = {"u1001": 84.0, "u1002": 83.5, "u1003": None}

# 17) Find the user_id with the highest average score (ignore None averages).
# 18) Compute the overall average score across ALL scores from ALL users.
# 19) Make a dictionary user_score_count mapping user_id -> number of scores.
# 20) Return a sorted list of user IDs by age (youngest to oldest).

# -------------------------
# Level 5: Safe dictionary handling (functions)
# -------------------------

# 21) Write a function get_city(users, user_id) that returns the city,
#     or None if the user_id or city is missing.

# 22) Write a function add_role(users, user_id, role) that adds the role
#     only if the user exists and the role isn't already there.

# 23) Write a function remove_user(users, user_id) that deletes a user safely:
#     it should not crash if the user_id doesn't exist.

# 24) Write a function get_email_list(users) that returns a list of emails
#     for users who have an "email" key and it is not None.

# 25) Write a function promote_to_admin(users, user_id) that:
#     - adds "admin" to roles (if missing)
#     - sets active = True
#     - does nothing if user_id doesn't exist

# -------------------------
# Optional: Quick test area
# -------------------------

# Write your solutions below this line.
# Tip: Solve them one by one and print results to check.

# Your code starts here:
