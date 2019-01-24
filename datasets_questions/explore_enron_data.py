#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np
from sklearn import preprocessing
enron_data = pickle.load(open("/home/dieq/ud120-projects/final_project/final_project_dataset.pkl", "rb"))

 
## Total Stock
# poi = []
# max_pay =  max(enron_data["FASTOW ANDREW S"]["total_payments"],
#         enron_data["SKILLING JEFFREY K"]["total_payments"],
#         enron_data["LAY KENNETH L"]["total_payments"])
# count_s = 0
# count_e = 0
# for i in enron_data:
#     if enron_data[i]["total_payments"] == "NaN":
#         count_s+=1
# print(count_s)
# print(len(enron_data))
# print(count_s/float(len(enron_data)) * 100)
stock_opt = []
salary = []
for i in enron_data:
        if enron_data[i]["exercised_stock_options"] != 'NaN':
            stock_opt.append(float(enron_data[i]["exercised_stock_options"]))
        if enron_data[i]["salary"] != 'NaN':
            salary.append(float(enron_data[i]["salary"]))
salary = [min(salary),200000.0,max(salary)]
stock_opt = [min(stock_opt),1000000.0,max(stock_opt)]
salary = np.array([[e] for e in salary])
stock_opt = np.array([[e] for e in stock_opt])
salary_scaler = preprocessing.MinMaxScaler().fit(salary)
stock_scaler = preprocessing.MinMaxScaler().fit(stock_opt)
print(salary_scaler.min_)
salary_test = np.array([[200000.0]])
stock_test = np.array([[1000000.0]])
print(salary_scaler.transform(salary_test))
print(stock_scaler.transform(stock_test))
# salary = []
# ex_stok = []
# for users in enron_data:
#     val = enron_data[users]["salary"]
#     if val == 'NaN':
#         continue
#     salary.append(float(val))
#     val = enron_data[users]["exercised_stock_options"]
#     if val == 'NaN':
#         continue
#     ex_stok.append(float(val))
    
# salary = [min(salary),200000.0,max(salary)]
# ex_stok = [min(ex_stok),1000000.0,max(ex_stok)]

# print (salary)
# print (ex_stok)

# salary = np.array([[e] for e in salary])
# ex_stok = np.array([[e] for e in ex_stok])

# scaler_salary = preprocessing.MinMaxScaler()
# scaler_stok = preprocessing.MinMaxScaler()

# rescaled_salary = scaler_salary.fit_transform(salary)
# rescaled_stock = scaler_salary.fit_transform(ex_stok)

# print (rescaled_salary)
# print (rescaled_stock)
