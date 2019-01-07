from collections import Counter
import pprint

data = open("./txt_data/NLP_replace.txt","r")
txt_data = data.read()
data.close()

words = txt_data.split()
words_list = Counter(words)

pprint.pprint(words_list)

