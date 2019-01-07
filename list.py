from collections import Counter
import pprint

test = open("./txt_data/NLP_sample.txt","r")
txt_data = test.read()
test.close()

c = Counter(txt_data)
pprint.pprint(c.most_common())
