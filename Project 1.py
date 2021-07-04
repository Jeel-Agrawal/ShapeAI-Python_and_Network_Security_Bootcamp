# Write a program in python to generate MD5 of string data
import hashlib

string = input("Enter any String : ")

result = hashlib.md5(string.encode())
print("The MD5 of entered String Data is : ",result.hexdigest())