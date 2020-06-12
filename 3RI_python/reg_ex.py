

import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
abcd78.54xy@gail.com
coreyms.com
321-555-4321
123.555.1234
123*555*12349090
800-555-12
900-555-1234
a98-878-9090
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr 
Mr. T
'''
sent="she sells the shells on sea shore"
sentence = 'Start a sentence and then bring it to an end.'
#pattern = re.compile(r'[8-9a-z1]\d\d.\d\d\d.\d\d\d\d\b')
#pattern = re.compile(r'\d{3}.\d{3}.\d{2,9}')
pattern = re.compile(r'Mr[^s].?')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
