#use triple quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

for x in "banana":
  print(x)

for j in "sphere":
  print(j)

#To get the length of a string, use the len() function.
a = "onyx"
print(len(a))

#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

txt="My name is David"
print("John" in txt)

#if
txt="video games are useless"
print(txt)
if "video" in txt:
  print("word 'video' is used in this sentence.")

#not in
txt = "The best things in life are free!"
print("expensive" not in txt)

#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])


#Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])


a = "his name is John Cena"
print(a[-21:-9])

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

G = "coding is amazing"
print(G.upper())

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "dog"
print(a.replace("d", "f"))


a = "Hello, World!"
print(a.split(",")) 
# returns ['Hello', ' World!']