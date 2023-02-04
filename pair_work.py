text = 'hello world'

print(text.count('o'))
# counting how many o's there are in the string

if text.startswith('hell'):
    print("it's hell in there")
# startswith is a method to match the parameter- creating a conditional based on if the string starts with hell

if text.isalpha() :
    print('string is all alpha')
# .isalpha is a method to check if all characters are in the alphabet, The space acts as a character here- it is not all alphabetic

text = ' \t\r\n'
print(text)
if text.isspace():
    print('string is white space')

string.format (field_values)
# Call the format method on a string




