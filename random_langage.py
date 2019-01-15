import random

num = 100
D = 1
str_w = ""

test = open("./txt_data/NLP_replace.txt","r")
txt_data = test.read()
test.close()

M = len(txt_data)

for k in range(10):
    print(str(k+1)+" times\n")
    for i in range(num):
        K = random.randrange(M)
        if K < D:
            str_w += txt_data[K:K+D]
        else: 
            str_w +=  txt_data[K-D:K]
    print(str_w+"\n")
    print("--------------------------------\n")
