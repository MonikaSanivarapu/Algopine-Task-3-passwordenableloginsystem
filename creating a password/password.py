def login():  
    username = input("Enter username: ")  
    password = input("Enter password: ")  
  
    # Assuming we have a list of valid usernames and passwords  
    valid_users = ["raji", "sirisha", "lishi"]  
    valid_passwords = ["6584", "9874", "0124"]  
  
    if username in valid_users and password == valid_passwords[valid_users.index(username)]:  
        print("Login successful!")  
        # Add code to redirect to main application or perform other actions here  
    else:  
        print("Invalid username or password.")  
        # Add code to handle incorrect login attempts here  
  
login()  