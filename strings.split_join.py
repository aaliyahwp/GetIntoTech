line = 'root::0:0:superuser:/root:/bin/sh'
# this is a string- showing who the user is and what their permissions are
elems = line.split(':')
#elems- element splitting it up into component parts

elems[0] = 'avatar'
elems[4] = "The super-user (zero)"
line = ':'.join(elems)
print(line)

#elems are elements

# take all the parts and join them all together

