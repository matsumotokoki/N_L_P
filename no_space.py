import re
test = open("./txt_data/NLP_sample.txt","r")
txt_data = test.read()
test.close()

replace_txt = re.sub(r"[^a-zA-Z\t\r\f\v]","",txt_data)
replace_txt = re.sub(r"","",replace_txt)
print(replace_txt)

file = open('./txt_data/NLP_nospace.txt','w')
file.write(replace_txt)
file.close()
