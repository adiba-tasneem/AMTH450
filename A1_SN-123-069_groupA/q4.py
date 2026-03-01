count=0
avg=0
total=0
with open("mbox.txt") as abc:
    for line in abc:
        if line.startswith("X-DSPAM-Confidence:"): 
                val = float(line.strip().split(":")[1])  
                total += val 
                count += 1  

avg= total/count
print(f"averge of the numbers is:{avg:.2f}")
print(f"there are total of {count} floating point values in file.")
