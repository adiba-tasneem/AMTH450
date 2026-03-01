filename=input("enter file:")
email_count = {}


with open(filename) as file:
    for line in file:
        if line.startswith("From "):

            email = line.split()[1]
            email_count[email] = email_count.get(email, 0) + 1



max_email = None
max_count = 0

for email, count in email_count.items():
    if count> max_count:
        max_email = email
        max_count = count
print(max_email, max_count)
