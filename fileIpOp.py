
a = "Ashish is a person"

# Writing to a file
# with open("text.txt", "w") as f:
#     f.write(a)

# fp = open("test.txt", "w")
# fp.write(a)
# fp.close()

# Reading a file
# with open("text.txt", "r") as f:
#     a = f.read()
#     print(a)

# fp = open("test.txt", "r")
# a = fp.read()
# print(a)
# fp.close()

# Append to a file
with open("text.txt", "a") as f:
    f.write(", Hello Everyone")

with open("text.txt", "r") as fp:
    c = fp.read()
    print(c)