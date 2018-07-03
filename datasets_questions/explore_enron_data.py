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

print("Number of people in the dataset is {0}".format(len(enron_data)))
print("Number of features is {0}".format(len(enron_data.values()[0])))

count = 0
for person in enron_data.values():
	if person['poi'] == 1:
		count = count + 1
print("Number of POI (person of interest) is {0}".format(count))
# print(enron_data)

print("Total value of the stock belonging to James Prentice is {0}".format(enron_data['PRENTICE JAMES']['total_stock_value']))
print("Number of email messages from Wesley Colwell to persons of interest is {0}".format(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))
print("Value of stock options exercised by Jeffrey K Skilling is {0}".format(enron_data['SKILLING JEFFREY K']['exercised_stock_options']))

most_payed = {}
leaders = ['FASTOW ANDREW S', 'LAY KENNETH L', 'SKILLING JEFFREY K']
for leader in leaders:
	most_payed[leader] = enron_data[leader]['total_payments']
print("Most money was made by: {0}".format(sorted(most_payed, key=most_payed.__getitem__, reverse=True)))

not_defined = "?"
for person in enron_data.values():
	tsv = str(person['total_stock_value'])
	if not tsv.isdigit():
		not_defined = tsv
		break
print ("Not defined values are respresented by: {0}".format(not_defined))

count = 0
for person in enron_data.values():
	if person['salary'] != 'NaN':
		count = count + 1
print("Number of defined salaries is {0}".format(count))

count = 0
for person in enron_data.values():
	if person['email_address'] != 'NaN':
		count = count + 1
print("Number of defined emails is {0}".format(count))

count = 0
for person in enron_data.values():
	if person['total_payments'] == 'NaN':
		count = count + 1
print("Number of undefined total payments is {0}, which is {1}% of all people".format(count, round(count*100.0/len(enron_data), 3)))

count = 0
for person in enron_data.values():
	if person['total_payments'] == 'NaN' and person['poi'] == 1:
		count = count + 1
print("Number of POI with undefined total payments is {0}, which is {1}% of all people".format(count, round(count*100.0/len(enron_data), 3)))