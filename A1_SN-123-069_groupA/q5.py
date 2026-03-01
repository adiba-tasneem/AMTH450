email=[]
filename= input("enter file:")
with open(filename) as mailFile:
    for line in mailFile:
        if line.startswith("From "):
            email.append(line.split()[1])
for mails in email:
    print(mails)
count=len(email)
print(f"There were {count} lines in the file with \"From\" as the first word")

