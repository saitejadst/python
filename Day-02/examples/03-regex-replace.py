import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

text = "The quick red fox jumps over the yello brown dog"
pattern = r"red|yello"

replacement = "orange"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
