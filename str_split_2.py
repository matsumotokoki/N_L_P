import re
from collections import Counter
import pprint

data = open("./txt_data/NLP_nospace.txt","r")
txt_data = data.read()
data.close()

word2 = re.split('(..)',txt_data)[1::2]
word2_list = Counter(word2)

pprint.pprint(word2_list)
