address_parts = [1, "Road", "Town", "Greater London", "E14 7RT"]

address = " "

for item in address_parts:
    address = address + str(item) + " "

print(address)
# Strings are imutable- they can't be changed

# This is inefficient use join() str method instead


concatenated_address = ", ".join(address_parts)
print(concatenated_address)

print('Aaliyah says "hi!" to the class')

print("Victoria's peas were gross")

print("""Victoria's peas were gross" and she said "yuck"!""")
# In python you can have triple double quotes """  """
# You use triple double quotes when you have single quotes and double quotes or double quotes and apostraphes

word = "spam "
print(word, word, word, word)
# it would be easier to use a multiply operator

print(word * 12)

# Operator overloading is when an operator does different things depending on its operands
# Operands are the things either side of the operator
# + with numeric operands means add
# + with string operands means concatenate

sentence = """Victoria's peas were gross" and she said "yuck"!"""
# n equals a method- methods belong to objects

sentence_as_uppercase = sentence.upper()
print(sentence_as_uppercase)

gross = sentence.find('gross')
print(gross)
# Gives you an integer showing the position of the word

toria = sentence.find('toria')
print(toria)

Aaliyah = sentence.find('Aaliyah')
print(Aaliyah)
# If it's not found it says minus one