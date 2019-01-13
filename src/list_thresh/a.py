import sys
f1 = open("b.txt","r+") 
d = dict()
for line in f1.readlines():                          
    line = line.strip() 
    list_line = line.split(',')
    t1 = list_line[0]
    t2 = list_line[1]
    d[t1] = t2                          
 
target = sys.argv[1]
thresh = sys.argv[2]
d[target] = thresh

f2 = open("c.txt","w")
# for k,i in [d.keys(),d.values()]:
for k,i in d.items():
    f1.write(k+","+i+"\n")
    f2.write(str(i) + "\n")
    
