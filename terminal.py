import os
def process(r,dic_total):
    dic_each = dict()
    count = 0
    info = r.readlines()  #读取命令行的输出到一个list
    for line in info:  #按行遍历
        line = line.strip('%\r\n')
        if(count != 0):
            res = line.split(':')
            r = res[0]
            temp = r in dic_each.keys() #判断字典中有没有该物体
            if(temp == False):
                dic_each[r] = 1 #在字典中创建该物体
            else:
                dic_each[r] += 1 #该物体的出现次数加一 
        count += 1
    print (dic_each)
    for key in dic_each.keys(): #利用该图片的统计结果，更新总字典
        temp = key in dic_total.keys() #判断字典中有没有图片中的某物体
        if(temp == False):
            dic_total[key] = 1 #在字典中创建该物体
        else:
            dic_total[key] += 1 #该物体的出现次数加一

def scene(num,sce):
    dic_total = dict()
    for i in range(num):
        s = './darknet detect cfg/yolov3.cfg yolov3.weights '+ sce+'/'+ str(i+1) +'.jpg'#定义将图片送入网络的命令
        r = os.popen(s) #执行命令，截取命令行输出
        process(r,dic_total) #根据命令行输出，更改物体在图片类中的出现结果
        print(i)
        print(dic_total)
    for key in dic_total.keys():
        dic_total[key] = float(dic_total[key]/num)
    return dic_total

f = open("train-200.txt","w")
dic_kitchen = scene(200,'kitchen')  #统计各类物体在厨房图片类中的出现频率
f.write(str(dic_kitchen)) #将厨房类图片的统计字典写入文件
f.write('\n')
dic_liv = scene(200,"livingroom") #统计各类物体在客厅图片类中的出现频率
f.write(str(dic_liv)) #将客厅类图片的统计字典写入文件 
f.write('\n')
dic_bed = scene(200,"bedroom") #统计各类物体在卧室图片类中的出现频率
f.write(str(dic_bed)) #将卧室类图片的统计字典写入文件 
f.write('\n')


