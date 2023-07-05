import re

string = "The fack world."
pattern = r"brown.fox"

match = re.search(pattern, string)
if match:
	print("Match found!")
else:
	print("Match not found.")
