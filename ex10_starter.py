import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# have we used Glob in the correct way
# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

print(sys.platform)
glob.glob(hdir)

print(glob.glob(hdir))
print(hdir)
print(os.environ)

print(os.path.getsize(hdir))
#add a 'for' loop to iterate each individual file - print it's name and print it's size
# This is the size of the size of the whole of Users/awe35

file = glob.glob(pattern)
# finding any file or directory that is in my file directory
file_name = 'ex10_starter.py'
file_stats = os.stat(file_name)
print(file_stats)
print(os.path.getsize(file_name))
# Think that these sizes are in bytes and not in the same units- one is bytes and one is megabutes
# TODO: use os.path.getsize to find each file's size

# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

# unable to check for files that were not in the directory

# Unsure about the values of
