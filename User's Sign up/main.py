import sheety

def user_prompt():
    print("Welcome to Mitresh's Flight Club.\nI find the best flight deals and email them to you.")

    first_name = input("What is your first name? ").title()
    last_name = input("What is your last name? ").title()

    email1 = "a"
    email2 = "b"
    while email1 != email2:
      email1 = input("What is your email? ")
      if email1.lower() == "quit" or email1.lower() == "exit":
        exit()
      email2 = input("Please verify your email : ")
      if email2.lower() == "quit" or email2.lower() == "exit":
        exit()

    print("Great! you've successfully joined the club!")
    
    sheety.post_new_row(first_name, last_name, email1)

user_prompt()
