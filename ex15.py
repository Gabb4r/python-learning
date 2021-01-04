from sys import argv

script, filename = argv

text = open(filename)

print(f"your file name is {filename} and here is it's content >")

print(text.read())