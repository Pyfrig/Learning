
import re
import pyperclip

#regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000. 555-0000 ext 1234, ext. 12345, x12345
(
(((\d\d\d) | ((\(\d\d\d\))))? 
                   #area code
(\s | -)                   #first seperator
(\d\d\d)                    #first 3 digits
-                    #separator
(\d\d\d\d) )                   #last for digits
(((ext(\.)?\s) |x)     (\d{2,5}))?                    #extension
)


''', re.VERBOSE)

# regex for email
emailRegex = re.compile('''
# some.+_thing@some.+_thing.com

[a-zA-Z0-9_.+]+      #name part
@
[a-zA-Z0-9_.+]+ 
''', re.VERBOSE)
#get text off clipboard
text = pyperclip.paste()

#TODO extract email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumbers in extractedPhone:
    allPhoneNumbers.append(phoneNumbers[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print(extractedPhone)
print(extractedEmail)
print(allPhoneNumbers)


#TODO copy the extracted email/phone to the clipboard

