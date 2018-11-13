import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
	word=word.lower()
	try:
		if word in data:
			return data[word]
		else:
			guess=get_close_matches(word,data.keys(),cutoff=0.8)[0]
			print("Is this what you want to know about ? : ",guess)
			confirm=input("Y or N")
			if confirm is 'Y' or confirm is 'y':
				return data[guess]	
			else:
				return ["Enter Again"]	
	except:	
		return ["Does Not Exist"]
word=input("Enter Word : ")
meaning=translate(word)
for i in meaning:
	print(i)