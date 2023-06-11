import sys

file_path = sys.argv[1]
f = open(file_path, 'r')
words = f.read()
words = words.split()
words.sort(key=str.lower)

for word in words:
    print(word)
