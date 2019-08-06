import re

string = "The quick brown fox jumped over the lazy dog"
match = re.search(r"the", string)

if match:
    print("Found"), match.group()
else:
    print("Did not find")