#how to generate a random strong password in python
import random 
import string
def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password
# Example usage
password_length = 12
strong_password = generate_password(password_length)
print("Generated strong password:", strong_password)
#how to manage the generated password
import os
def save_password(password, filename):
    with open(filename, 'w') as file:
        file.write(password)    
# Example usage
filename = 'password.txt'
save_password(strong_password, filename)
print(f"Password saved to {filename}")    
      

