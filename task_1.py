## Task 1 of Level 5
import subprocess


def get_user_name():
    user_name = subprocess.run(
        ["git", "config" , "--get" , "user.name"],
        stdout=subprocess.PIPE,
        text=True,
    )
    user_name = user_name.stdout.strip()
    return user_name
def get_user_email():
    user_email = subprocess.run(
        ["git", "config" , "--get" , "user.email"],
        stdout=subprocess.PIPE,
        text=True,
    )
    user_email = user_email.stdout.strip()
    return user_email

if __name__ == "__main__":
    print("Level 5".center(50, "="))
    print("Task 1".center(10))
    print("""
    To complete this task, you have to properly configure you git user name and email.\n
    .""")
    print("----------------------------------------------------------------")
    name = input("What is your name? ")
    email = input("What is your email? ")
    if get_user_name() == name:
        print(f"Hello, {name}!  ")
        print("Your git user.name match your name. ")
        if get_user_email() == email:
            print("You have successfully completed Task 1 of Level 5.")
    else:
        print(f"Hello, {name}! \n ")
        print("Your git user.name does not match your name.")
        print("also your git user.email does not match your email.")
        exit(1)