total=0
count=0

print("The numbers in the file are:")
file= open("regex-sum-42.txt","r")

for line in file:
    line=line.split()
    for words in line:
        if words.isdigit():
            print(int(words))
            total+=int(words)
            count+=1


print(f"There are {count} numbers in file.")
print("Sum of all the numbers is: ",total)

    




