#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("/home/dieq/ud120-projects/final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL")
data = featureFormat(data_dict, features)
enron_data = pickle.load(open("/home/dieq/ud120-projects/final_project/final_project_dataset.pkl", "rb"))


### your code below 

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
max_bonus = max(item[1] for item in data)
max_salary = max(item[0] for item in data)
for i in enron_data:
    if enron_data[i]["salary"] == max_salary and enron_data[i]["bonus"] == max_bonus:
        print (i)
