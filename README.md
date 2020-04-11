# Files
folders:
src: 网络各层的代码  
obj: 各层网络编译后生成的目标文件  
example: 完整的网络实例代码   
cfg: darknet支持的各类网络的架构文件   
data: 各数据集的信息(标签、类别名)  

bedroom、kitchen、livingroom：各类别图片素材    
predictions.jpg：网络的输出图片

kic_times.py: 确定训练的图片次数(何时主特征物体的频率趋于稳定)  
kic_times.txt: 训练n次时，图片主特征的出现频率
terminal.py: 场景识别训练脚本(统计各类物体在图片集中的出现频率)   
train.txt: 每类训练100张图片后的统计结果   
train-200.txt: 每类训练200张图片后的统计结果   
test.py: 场景识别测试脚本 (基于朴素贝叶斯公式，计算图片属于各个类别的概率) 

video.py: 视频场景识别脚本
middle.jpg: 从视频流中截取的中间帧  
test.mp4: 源视频文件  
detection.avi: 场景识别输出视频文件 
