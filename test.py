import os
def process(r):
    dic_each = dict()
    count = 0
    info = r.readlines()  #读取命令行的输出到一个list
    for line in info:  #按行遍历
        line = line.strip('%\r\n')
        if(count != 0):
            res = line.split(':')
            r = res[0] #提取图像中的物体
            temp = r in dic_each.keys() #判断字典中有没有该物体
            if(temp == False): 
                dic_each[r] = 1 #在字典中创建该物体
            else:
                dic_each[r] += 1 #该物体的出现次数加一 
        count += 1
    return dic_each
 
def scene(num1,num2,sce,res):
    classification = []
    for i in range(num1,num2):
        s = './darknet detect cfg/yolov3.cfg yolov3.weights '+ sce+'/'+ str(i+1) +'.jpg'
        r = os.popen(s)
        dic_each = process(r) #统计该图片里各物体的出现次数
        category = []
        for j in range(len(res)):
            category.append(1)
            for key in dic_each.keys():
                temp = key in res[j]
                if(temp == True):
                    category[j] *= res[j][key] #如果物体出现过，依据计算公式，乘上其出现频率
                else:
                    category[j] *= 0.003 #如果该物体未曾出现过，将其出现频率设为0.003
        if(category[0] > category[1] and category[0] > category[2]):
            classification.append('kitchen')
        elif(category[1] > category[0] and category[1] > category[2]):
            classification.append('livingroom')
        elif(category[2] > category[0] and category[2] > category[1]):
            classification.append('bedroom')
        else:
            classification.append('failure') #每个场景的概率都为0，标签记为failure
    return classification

res = []
f = open("train.txt","r")
for line in f.readlines():
    line.strip()
    dic = eval(line)   
    res.append(dic) #读取出三类图片集对应的字典，将其拼接为字典数组
c1 = scene(201,241,'kitchen',res) #测试厨房类图片的识别率
c2 = scene(201,241,'livingroom',res) #测试客厅类图片的识别率
c3 = scene(201,241,'bedroom',res) #测试卧室类图片的识别率
