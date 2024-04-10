import random
import string
desired_length = int(input("Enter the desired length of the password: "))
characters = string.ascii_letters + string.digits + string.punctuation
generated_password = ''.join(random.choice(characters) for _ in range(desired_length))
print("Generated password: ", generated_password)
