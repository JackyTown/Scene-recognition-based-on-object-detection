f1 = open("a.txt","r")
f2 = open("b.txt","w")
thresh = 0.5
for line in f1.readlines():
    line = line.strip()
    f2.write(line + "," + str(thresh) + "\n")
