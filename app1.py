'''


'''
import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data=json.load(open("data.json"))

def find_mean(word):
	word=word.lower()
	if word in data:
		mean=data[word]
		return mean
	elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
		word=word.title()
		return data[word]
	elif word.upper() in data: #in case user enters words like USA or NATO
		word=word.upper()
		return data[word]
	else:
		try:
			mean=get_close_matches(word,data.keys())[0]
			w=input("You Mean To that:"+str(mean)+"?? 'Y' for Yes and 'N' for No:  ")
			if w.lower() == 'y':
				return data[mean]
			else:
				return "Sorry!! Try Again.. May be its not exit"
		except:
			return "Words Not Exist"	

			
#code is return here
while(1):
	word=input("Write Down the word you want??		")
	mean=find_mean(word)
	if type(mean)==list:
			for i in mean :
				print("\t",i,end="\n\n")
	else:
		print("\t",mean)
	ans=input("Did You want to continue? Y/N	")
	if ans=='N' or ans=='n':
		break