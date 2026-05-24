import re
import json

# read file
file = open("../input/raw-text.txt", "r")
text = file.read()
file.close()

# patterns
email_pattern = r"\b[\w\.-]+@[\w\.-]+\.\w+\b"
card_pattern = r"\b(?:\d{4}[- ]?){3}\d{4}\b"
url_pattern = r"https?://\S+"
phone_pattern = r"\+?\d[\d\s()-]{7,}\d"

# find data
emails = re.findall(email_pattern, text)
cards = re.findall(card_pattern, text)
urls = re.findall(url_pattern, text)
phones = re.findall(phone_pattern, text)

# email groups
official = []
alumni = []
si = []
others = []

for e in emails:
    if e.endswith("@alueducation.com"):
        official.append(e)
    elif e.endswith("@alumni.alueducation.com"):
        alumni.append(e)
    elif e.endswith("@si.alueducation.com"):
        si.append(e)
    else:
        others.append(e)

# clean cards (mask)
safe_cards = []
for c in cards:
    c = c.replace("-", "").replace(" ", "")
    if len(c) == 16 and c.isdigit():
        safe_cards.append("**** **** **** " + c[-4:])

# result
data = {
    "emails": {
        "official": official,
        "alumni": alumni,
        "si": si,
        "others": others
    },
    "cards": safe_cards,
    "urls": urls,
    "phones": phones
}

# save
with open("../output/sample-output.json", "w") as f:
    json.dump(data, f, indent=4)

print("done")