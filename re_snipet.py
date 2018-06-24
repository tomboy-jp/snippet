import re
import string

target = string.printable

re.findall('\d', target)
re.findall('\w', target)
re.findall('\s' ,target)
