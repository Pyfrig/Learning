#! python3
import webbrowser, sys, pyperclip

sys.argv #['mapit.py, '870 'Valencia']
# check if passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print('passed')
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/
webbrowser.open('https://www.google.com/maps/place/'+ address)

#bat files: @py c:\filsti .py fil  %*
#@pause

