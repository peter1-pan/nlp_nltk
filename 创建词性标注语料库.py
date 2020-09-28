import nltk
import os,os.path

create = os.path.expanduser('./nltkdoc')
if not os.path.exists(create):
    os.mkdir(create)
print(os.path.exists(create)) # 文件夹是否被创建

import nltk.data
print(create in nltk.data.path) # false,说明数据目录未被创建，需要手动创建