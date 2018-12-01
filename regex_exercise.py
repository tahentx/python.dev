import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My phone number is 281-702-1156')
print('Phone number found: ' + mo.group())

