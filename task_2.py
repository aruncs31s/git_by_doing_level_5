## Task 1 of Level 5
import subprocess
from task_1 import get_user_name


def get_sunshine_password():
    commit = subprocess.run(
        ["git", "log" , "--author=sunshine" , "-p"],
        stdout=subprocess.PIPE,
        text=True,
    )
    commit_contents = commit.stdout.strip().split("\n")
    password_line = commit_contents[len(commit_contents) - 1]
    password = password_line[1:].strip()
    return password
# get_sunshine_password()


if __name__ == "__main__":
    print("Level 5".center(50, "="))
    print("Task 2".center(10))
    
    print(f"""
    Hey {get_user_name()} magine someone asked to share their password with everyone. What they did was that , they added their password to password.txt and committed it to the repository. Each of them deleted the previous password that was in the password.txt and added their own password.
    """)
    print("----------------------------------------------------------------")
    name = get_user_name()
    print(f"Hi {name}! To complete this task, you have to find sunshine's password.\n")
    ans_1 = input("Did you find sunshine's password? (n/y): ").strip().lower()
    if ans_1 == "y":
        print("cool.")
        ans_2 = input("what is sunshine's password? ")
        if ans_2 == get_sunshine_password():
            print("cool")
            print("You have completed Task 2 of Level 5.")
            exit(0)
        else:
            print("Incorrect password. Please try again.")
            exit(1)
    else:
        print("You need to find sunshine's password to complete this task.")
        exit(1)