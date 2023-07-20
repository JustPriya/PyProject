import xml.etree.ElementTree as ET
import csv
import pandas as pd
import numpy as np

# print("Hello World!")

xml_data ='sample-data.xml'
tree = ET.parse(xml_data)

# python list of table nmaes
table_names = ['request', 'planSponsorsContacts', 'contacts', 'general']
tb2 = []              
               
for elem in tree.iter():
    if elem.tag in table_names:
        tb2.append(elem.tag)

table_index = 0
result_arr = []
# table = str(tb2[0])
for table in tb2:
    table_index += 1
    record_id = 0 # table_value_index
    value_id = -1
    record_arr = []
    table_arr = []

    for elem in tree.iter(table):
        print('elem', elem)
        for el in elem.iter():
            print('el', el)
            if el.tag == "record" and len(record_arr) > 0 :
                record_id += 1
            else:
                value_id += 1
                if el.tag == "record" and len(record_arr) == 0:
                    record_id = 1
                record_arr.append((table_index,table, record_id, value_id, el.tag, el.text))
    record_arr = record_arr[1:]
    result_arr.extend(record_arr)
print(result_arr)
# upto this cdoe extractind data from xml is done

headerList = ['Table_Index', 'Table_Name', 'Table_Value_Index', 'Value_index', 'XML_Name', 'XML_Value']
pd.DataFrame(result_arr).to_csv('Sample2.csv', header = headerList, encoding='utf8', index=False )
allData = pd.read_csv( "Sample2.csv")
print (allData)

# def Save_data(allData, myFile, table_index): 
#     print('running from inside the function')
#     file = open(myFile, 'w', newline='') 
#     writer = csv.writer(file)
#     writer.writerow(headerList)
#     result = []
	
	
        
#     for i in range(len(allData)):
#         if (allData.iloc[i,0] == table_index):
#              result = allData.iloc[i,:]
#              result_array = np.array(result)
#              myList = result_array.tolist()
#              writer.writerow(myList)

# # to find the total number of Table_names
# count = 1
# i = 1
# for i in range(allData.shape[0]-1):
#      if allData.iloc[i]['Table_Name'] == allData.iloc[i+1]['Table_Name']:
#           continue
#      else:
#           count = count + 1

# # call the function to create csv file
# for i in range(count):
#      Save_data(allData, 'file' + str(i+1) + '.csv', i+1)
#      if i > count:
#                break
               