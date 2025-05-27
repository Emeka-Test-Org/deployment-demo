import os

# BAD: Arbitrary command execution
user_input = input("Enter your name: ")
os.system(f"echo Hello {user_input}")

# BAD: Hardcoded credentials
username = "admin"
password = "password123"

# BAD: Hardcoded AWS secret
AWS_SECRET = "AKIA1234567890SECRET"
