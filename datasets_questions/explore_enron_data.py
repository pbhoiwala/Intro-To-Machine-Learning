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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#enron_data = pickle.load(open("../final_project/poi_names.txt", "r"))
print(enron_data)
#print(enron_data["SKILLING JEFFREY K"]["total_payments"])

salaryCtr = emailCtr = paymentCtr = 0
for person,data in enron_data.items():
    #print(person)
    if data["salary"] != 'NaN':
        salaryCtr+=1
    if data["email_address"] != 'NaN':
        emailCtr+=1
    if data["total_payments"] == 'NaN':
        paymentCtr+=1
print(salaryCtr)
print(emailCtr)
print(len(enron_data))