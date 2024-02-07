# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break


# f = open('myfile.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks of students {i} in maths is: {m1}")
#     print(f"marks of students {i} in english is: {m2}")
#     print(f"marks of students {i} in science is: {m3}")
#     if not line:
#         break
#     print(line)
#

f = open('myfile2.txt', 'w')
lines = ['line 1/n', 'line 2/n', 'line 3/n']
f.writelines(lines)
f.close()
