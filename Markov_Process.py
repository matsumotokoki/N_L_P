import random
import re

num = 100
D = 20
str = ""
A = ""
fd = 0

test = open("./txt_data/NLP_replace.txt","r")
txt_data = test.read()
test.close()

M = len(txt_data)
K = random.randrange(M-D)

str += txt_data[K:K+D]
A = txt_data[K+1:K+D]

for i in range(num):
    K = txt_data.find(A,random.randrange(M-D))+D
    str += txt_data[K+1:K+D]
    A = txt_data[K+1:K+D]


str = re.sub(r"\n"," ",str)
print(str)
