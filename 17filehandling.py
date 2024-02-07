#Reading a file

f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# Writing a file
f = open('myfile2.txt', 'w')
f.write("Hello, World")
f.close()

# Appending a file
f = open('myfile2.txt', 'a')
f.write("Hello, World")
f.close()