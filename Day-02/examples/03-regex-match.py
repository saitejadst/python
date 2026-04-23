import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

text = "Today is awesome"
pattern = r"Today"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
