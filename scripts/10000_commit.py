import subprocess
from unittest import result
import requests 
import random

# 
def set_user_name(name):
    subprocess.run(
        ["git", "config", "--global", "user.name", name],
        stdout=subprocess.PIPE,
        text=True,
    )
def set_user_mail(name):
    subprocess.run(
        ["git", "config", "--global", "user.email", name],
        stdout=subprocess.PIPE,
        text=True,
    )
def add_file_to_commit(file_path):
    subprocess.run(
        ["git", "add", file_path],
        stdout=subprocess.PIPE,
        text=True,
    )
    print(f"Added {file_path} to commit.")
    return True
def commit_changes(message):
    subprocess.run(
        ["git", "commit", "-m", message],
        stdout=subprocess.PIPE,
        text=True,
    )
    print(f"Committed changes with message: {message}")
    return True

def add_content_to_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Added content to {file_path}.")
    return True
content = requests.get("https://raw.githubusercontent.com/urbanadventurer/username-anarchy/refs/heads/master/names/facebook/lastnames-top10000.txt")

names = content.text.split("\n")

for i in range(10000 - 1) :
    name = names[i]
    new_password = random.randint(10000000, 99999999)
    add_content_to_file("password.txt", str(new_password) + "\n")
    set_user_name(name)
    set_user_mail(name + "@example.com")
    add_file_to_commit("password.txt")
    commit_changes(f"Added {name}'s password to password.txt")
print("All names added and committed successfully.")



