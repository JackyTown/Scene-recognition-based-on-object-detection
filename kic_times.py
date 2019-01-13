import os
f = open("kic_times.txt","w")
def process(r,dic_total):
    dic_each = dict()
    count = 0
    info = r.readlines()  #读取命令行的输出到一个list
    for line in info:  #按行遍历
        line = line.strip('%\r\n')
        if(count != 0):
            #print(line)
            res = line.split(':')
            r = res[0]
            temp = r in dic_each.keys()
            if(temp == False):
                dic_each[r] = 1
            else:
                dic_each[r] += 1
        count += 1
    print (dic_each)
    for key in dic_each.keys():
        temp = key in dic_total.keys()
        if(temp == False):
            dic_total[key] = 1
        else:
            dic_total[key] += 1

def scene(num,sce):
# os.system("./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg")
    dic_total = dict()
    for i in range(1,num):
        s = './darknet detect cfg/yolov3.cfg yolov3.weights '+ sce+'/'+ str(i) +'.jpg'
        r = os.popen(s)
        process(r,dic_total)
        print(i)
        print(dic_total)
        if(i % 10 == 0):
            f.write(str(i) + ": " + str(float(dic_total['oven']/i)))
            f.write('\n')
    for key in dic_total.keys():
        dic_total[key] = float(dic_total[key]/num)
    return dic_total

os.system("ls")
# f = open("kic_times.txt","w")
dic_kitchen = scene(301,'kitchen')
f.write(str(dic_kitchen))
f.write('\n')
# dic_liv = scene(100,"livingroom")
# f.write(str(dic_liv))
# f.write('\n')
# dic_bed = scene(100,"bedroom")
# f.write(str(dic_bed))
# f.write('\n')
print(dic_kitchen)
# print(dic_liv)
# print(dic_bed)

