# Write a program in python to generate hashes of string data using 3 algorithms from hashlib.
import hashlib
str_data = input("Enter your name : ")

result1 = hashlib.sha256(str_data.encode())
print(result1.hexdigest())

result2 = hashlib.sha384(str_data.encode())
print(result2.hexdigest())

result3 = hashlib.sha224(str_data.encode())
print(result3.hexdigest())