import sys

file_path = sys.argv[1]
f = open(file_path, 'r')
words = f.read()
words = words.split()
words = [word.lower() for word in words]
words = set(words)
print(len(words))
