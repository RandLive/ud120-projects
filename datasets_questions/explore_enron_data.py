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
print (enron_data)

num_ppl = len(enron_data.items())
print ('The total number of people is', num_ppl)

num_features = len(enron_data["METTS MARK"])
print ('The total number of features is', num_features)

all_names = (enron_data.keys())

numPOIs = 0
for name in enron_data:
    person = enron_data[name]
    person_name = all_names
    if person['poi']:
        numPOIs += 1

print ('Number of poi is ', numPOIs, 'and they are:', person_name)

text_file = open("../final_project/poi_names.txt", "r")
# print ('ppl in the text file are', text_file.read())

dictList = []
with open("../final_project/poi_names.txt", "r") as f:
    for line in f:
        elements = line.rstrip().split()[2]
        # print (elements)
        dictList.append(elements)
print ('The dictionary of POI in the .txt file', dictList)
print(len(dictList))

print ('The sales worth under James Prentice is', enron_data["PRENTICE JAMES"]["total_stock_value"])
print ('The Number of Emails Wesley Colwell sent to poi is', enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print ('The Value of .. of Jeffrey K Skilling is', enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])


print ('LAY money back', enron_data["LAY KENNETH L"]["total_payments"])
print ('SKILLING money back', enron_data["SKILLING JEFFREY K"]["total_payments"])
print ('Fastow money back', enron_data["FASTOW ANDREW S"]["total_payments"])

num_Payments = 0
for name in enron_data:
    person = enron_data[name]
    person_name = all_names
    if person['salary'] != "NaN":
        num_Payments += 1
print ('The number of of PPl got payments is', num_Payments)

num_Emails = 0
for name in enron_data:
    person = enron_data[name]
    person_name = all_names
    if person['email_address'] != "NaN":
        num_Emails += 1
print ('The number of of PPl got payments is', num_Emails)

#
num_Xxx = 0
for name in enron_data:
    person = enron_data[name]
    person_name = all_names
    # if person['poi']:
    #     if person['total_payments'] == "NaN":
    if person['poi'] and person['total_payments'] == "NaN":
            num_Xxx += 1
print ('The number of of PPl Xxx', num_Xxx)

