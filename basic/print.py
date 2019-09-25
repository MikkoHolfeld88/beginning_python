print("a","b")

# sep - determines what serves as a seperation item

print("a","b",sep=" / ")

# end="" -> no linebreak 

print("a","b", end="")

# print without a new line but with a space

print("Good Morning!"),
print("What a wonderful day!")

# no endl

for i in range(4):
    print(i, end=" ")

# sending print output to a different stream

fh = open("test.txt", "w")
print("Dies ist nur ein winziger Test!", file = fh)
fh.close()
