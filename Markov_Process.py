import random
import re
import sys

num = 1000
D = 0
text = ""
A = ""
fd = 0

args=sys.argv
try:
    if args[1]:
        D=int(args[1])
except:
    print("non-order!!")
    D=3

print("\n--"+str(D)+"-order approximation--\n")

test = open("./txt_data/NLP_replace.txt","r")
txt_data = test.read()
test.close()

M = len(txt_data)
K = random.randrange(M-D)

text += txt_data[K:K+D]
A = txt_data[K+1:K+D]

# for i in range(num):
while len(text) < num:
    K = txt_data.find(A,random.randrange(M-D))+D
    text += txt_data[K+1:K+D]
    A = txt_data[K+1:K+D]


text = re.sub(r"\n"," ",text)
text = re.sub(r"  "," ",text)
print(text)
