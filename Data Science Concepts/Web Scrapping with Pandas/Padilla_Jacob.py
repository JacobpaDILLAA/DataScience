#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
from os.path import join
import requests
from bs4 import BeautifulSoup

professor_path = "professors/"

req = requests.get("https://www.utep.edu/cs/people/index.html")
soup = BeautifulSoup(req.text, 'lxml') # HTML text and lxml parser

#Traversing the HTML Tree
divs = soup.findAll("div", {"class": "col-md-6"}) #Grabs info of faculty

raw1=[]
raw2=[]
raw3=[]
raw4=[]
raw5=[]
raw6=[]

for div in divs: 
    #Name
    facultyName = div.find("h3", {"class":"name"})
    
    #Office
    facultyAddress = div.find("span", {"class":"address"})
    
    #Email
    facultyEmail = div.find("span", {"class":"email"})
    
    #Phone
    facultyPhone = div.find("span", {"class":"phone"})
    
    #extract username from email
    UserEmail = div.find("span", {"class":"email"})
      
    #Title
    facultyTitle = div.find("span", {"class": "Title"})
    if facultyTitle is not None:
        if "Professor" in facultyTitle.text:
            
            raw2.append(facultyTitle.text)
        
            if facultyName is not None:
                raw1.append(facultyName.text)
    
            if facultyAddress is not None:
                raw3.append(facultyAddress.text)
    
            if facultyEmail is not None:
                raw4.append(facultyEmail.text)
        
            if facultyPhone is not None:
                #res = [re.findall(r'(\w+?)(\d+)', facultyPhone.text)[0] ]
                raw5.append(facultyPhone.text)
        
    
            #if UserEmail is not None:
            temp = UserEmail.text.split("@")[0]
            
            # Web Page
            facultyWeb = div.findAll('a')
            facultyURL = facultyWeb[len(facultyWeb) - 1].get("href")
            #if len(facultyURL) > 0 :
            if len(facultyURL) is not None:
                raw6.append(facultyURL)
                if len(facultyURL) > 0:
                    WebPageContent = requests.get(facultyURL) #html format
                    content = BeautifulSoup(WebPageContent.text, "lxml") #plain text
                    name = temp+".txt" #name of professor
                    file = open(join(professor_path,name),'w') #open professor folder on Desktop
                    n = file.write(content.text)
                    file.close()
                

raw_data = {'Name':raw1[0:], 'Title':raw2[0:], 'Office':raw3[0:], 
            'Email':raw4[0:], 'Phone':raw5[0:], 'website':raw6[0:]}

professor_dataframe = pd.DataFrame(raw_data)
professor_dataframe.to_pickle("./professors.pkl")
professor_dataframe
#unpickled_professors = pd.read_pickle("./professors.pkl")
#unpickled_professors


# In[22]:


import os
import time

#search term
text = input("Enter Search term  ")
start = time.time()  #start timer
term = text.split()[0]

#store filename as id and num of times word appears
mapping = dict()
directory = '/professors'
for filename in os.walk(directory):
    if filename.endswith(".txt"):
        file = open(filename) #open file in directory
        for i in file:
            temp = file
            count = 0 
            if temp[i] == term:
                count += 1
                mapping.append(count)
end = time.time() #end timer
total = end-start #calculate time took to compute operation
            
            
#print(mapping)
print("The term searched:",term ," took ",total)



# In[ ]:





# In[ ]:




