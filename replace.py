import re
test = open("./NLP_sample.txt","r")
txt_data = test.read()
test.close()

replace_txt = re.sub(r"[^a-zA-Z\n\t\r\f\v]"," ",txt_data)
replace_txt = re.sub(r"","",replace_txt)
print(replace_txt)

file = open('./NLP_replace.txt','w')
file.write(replace_txt)
file.close()
