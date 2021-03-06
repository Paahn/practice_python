# Write a password generator in Python.
# Be creative with how you generate passwords - strong
# passwords have a mix of lowercase letters, uppercase
# letters, numbers, and symbols. The passwords should
# be random, generating a new password every time the
# user asks for a new password. Include your run-time code in a main method.
# Ask the user how strong they want their password to be. For weak passwords,
# pick a word or two from a list.
import random
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
symbols = "!?@#$%^&*()_-+="
passw_leng = int(input("Password length: "))
passw = "".join(random.sample(lowercase+uppercase+nums+symbols, passw_leng))

print("Here is you new password: {}".format(passw))

