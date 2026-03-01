def  frequency(teachers_file):


    teachers_name=list()

    for line in teachers_file:
        line=line.rstrip()
        if not line.startswith("Applied Mathematics"):
            names=line.split()
            for name in names:
                if name not in teachers_name: teachers_name.append(name)

    teachers_name.sort()
    return teachers_name 
#print(teachers_name)

teachers_file= open("amth.txt")
a=frequency(teachers_file)
print(a)