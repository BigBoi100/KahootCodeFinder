Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests
import random

print('Welcome to the kahoot hacker!! ')
print('I am not responsible for any damage or trouble you get after using this')


digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
print('															
      
      					FINDING KAHOOT CODES... PLEASE WAIT!!
      ')


def is_code_valid(code):
  request = requests.get("https://kahoot.it/reserve/session/" + code)
  return request

while True:
	code = ""
	for i in range(6):
		code += random.choice(digits)
	result = is_code_valid(code)
	if result.status_code == 200:
		with open("games.txt", "a") as file:
			file.write(code + "\n")
		print(code)
      
