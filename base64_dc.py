#!/usr/bin/python3
import base64

f = open('flag.txt', 'r')
text = f.read()

while 1:
    text = base64.b64decode(text).decode('utf-8')

    if '{' in text:
        print(text)
        #continue
        break
