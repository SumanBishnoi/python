f= open("sb.txt", "rt")
#for priting only 5 text
# char=f.read(20)
# print(char)

#if we again use read command it will read next text
# char2= f.read()
# print(char2)

#for printing character by character
# for line in char2:
#     print(line)

#for printing line by line
# for line in f:
#     print(line)

#readline function
# print(f.readline())
# print(f.readline())
print(f.readlines())
print(f.tell()) #tells where the pointer is
f.seek(10)
print(f.tell())



f.close()