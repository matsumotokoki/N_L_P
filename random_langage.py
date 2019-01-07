import random

num = 100
D = 1
str = ""

test = open("./txt_data/NLP_replace.txt","r")
txt_data = test.read()
test.close()

M = len(txt_data)

for i in range(num):
    K = random.randrange(M)
    if K < D:
        str += txt_data[K:K+D]
    else: 
        str +=  txt_data[K-D:K]

print(str)
