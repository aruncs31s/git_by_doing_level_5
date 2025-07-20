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
def get_catacutan_password():
    
    commit = subprocess.run(
        ["git", "log" , "--author=catacutan" , "-p"],
        stdout=subprocess.PIPE,
        text=True,
    )
    commit_contents = commit.stdout.strip().split("\n")
    password_line = commit_contents[len(commit_contents) - 1]
    password = password_line[1:].strip()
    return password


if __name__ == "__main__":
    print("Level 5".center(50, "="))
    print("Task 3".center(10))
    
    print(f"""
    The sunshine did delete someone else's password right?.  Because of everyone is rewriting the password.txt file with their own password the old password get deleted.
    """)
    print("----------------------------------------------------------------")
    name = get_user_name()
    
    print(f"Hi {name}! To comple te this task, you have to find the user name and password of the person before sunshine.\n")
    ans_1 = input("Did you find specified user name and password? (n/y): ").strip().lower()
    if ans_1 == "y":
        print("cool.")
        ans_2 = input("what is the username? ")
        if ans_2 == "catacutan":
            print("cool")
            ans_3 = input("what is the password? ")
            if ans_3 == get_catacutan_password():
                print("cool")
                print("You have completed Task 2 of Level 5.")
                exit(0)
            else:
                print("Incorrect password. Please try again.")
                exit(1)
            exit(0)
        else:
            print("Incorrect password. Please try again.")
            exit(1)
    else:
        print("You need to find sunshine's password to complete this task.")
        exit(1)