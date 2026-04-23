import re

text = "There are nearly 10 good teammembers"
pattern = r"10"

search = re.search(pattern, text)
if search:
    print("goodteam found count:", search.group())
else:
    print("goodteam not found")

text = "There are nearly 5 bad teammembers"
pattern = r"5"

search = re.search(pattern, text)
if search:
    print("badteam found count:", search.group())
else:
    print("badteam not found")
