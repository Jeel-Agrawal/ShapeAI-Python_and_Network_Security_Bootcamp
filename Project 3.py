# Write a program in python to add Salting and Iteration to your hashes
import hashlib
import os

str = input("Enter String for Salting and Iterrations : ")
salt = os.urandom(32)

result = hashlib.pbkdf2_hmac('sha256', str.encode(), salt, 500)
pt = result.hex()
print("The Result after adding Salting and Iterations is : ", pt)