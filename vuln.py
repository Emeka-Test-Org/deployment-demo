import subprocess

def run_user_code(user_input):
    eval(user_input)

def bad():
    user_input = input("Run: ")
    subprocess.call(user_input, shell=True)  # Dangerous: shell injection
