from __future__ import print_function
from nltk.metrics import accuracy,precision,recall,f_measure

training='PERSON OTHER PERSON OTHER OTHER ORGANIZATION'.split()
testing='PERSON OTHER OTHER OTHER OTHER OTHER'.split()

print(accuracy(training,testing))

trainset=set(training)
testset=set(testing)
print(precision(trainset,testset)) # 准确率
print(recall(trainset,testset))  # 召回率
print(f_measure(trainset,testset))


# 计算 编辑距离 复制 cost为0, 替换、删除、插入cost为1
from nltk.metrics import edit_distance
print(edit_distance('relate','relation'))
print(edit_distance('suggestion','calculation'))

# 使用Jaccard系数执行相似性度量 , ｜X 交 Y｜/｜X 并 Y｜ 
from nltk.metrics import jaccard_distance
X=set([10,20,30,40])
Y=set([20,30,60])
print(jaccard_distance(X,Y))

# 二进制距离算法度量 便签相同返回0.0，否则1.0
from nltk.metrics import binary_distance
print(binary_distance(X,Y))

# 存在多个标签，Masi距离算法
from nltk.metrics import masi_distance
print(masi_distance(X,Y))