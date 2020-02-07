#!/usr/bin/env python
# coding: utf-8

# In[336]:


import csv
import requests
import json
import numpy


# In[256]:



url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key=AkWqfa4EZTXRUDeYQOQZoqXWBM20PutZT9k3og1gNb-b7MVhsr15Q4zQ_UkH_uBA"
orS1 = "{\n\t\"origins\": ["
destS1 = "\"destinations\": ["
travS = "\n\"travelMode\": \"driving\"\n}"
orS2 = "{\n\t\"origins\": ["
destS2 = "\"destinations\": ["
orS3 = "{\n\t\"origins\": ["
destS3 = "\"destinations\": ["
#startS = "&startTime=2020-02-2T12:00:00-07:00"
csv1 = "rivers1.csv"
with open(csv1, newline='') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        destS1 = destS1 + "\n\t{\n\t\t \"latitude\": " + row['Access_Latitude'] + ",\n\t\t \"longitude\": " +  row['Access_Longitude'] + "\n\t },"
        orS1 = orS1 + "\n\t{\n\t\t \"latitude\": " + row['Takeout_Latitude'] + ",\n\t\t \"longitude\": " +  row['Takeout_Longitude'] + "\n\t },"

csv2 = "rivers2.csv"
with open(csv2, newline='') as csvfile2:
    reader2 = csv.DictReader(csvfile2)
    for row in reader2:
        destS2 = destS2 + "\n\t{\n\t\t \"latitude\": " + row['Access_Latitude'] + ",\n\t\t \"longitude\": " +  row['Access_Longitude'] + "\n\t },"
        orS2 = orS2 + "\n\t{\n\t\t \"latitude\": " + row['Takeout_Latitude'] + ",\n\t\t \"longitude\": " +  row['Takeout_Longitude'] + "\n\t }," 
        
csv3 = "rivers3.csv"
with open(csv3, newline='') as csvfile3:
    reader3 = csv.DictReader(csvfile3)
    for row in reader3:
        destS3 = destS3 + "\n\t{\n\t\t \"latitude\": " + row['Access_Latitude'] + ",\n\t\t \"longitude\": " +  row['Access_Longitude'] + "\n\t },"
        orS3 = orS3 + "\n\t{\n\t\t \"latitude\": " + row['Takeout_Latitude'] + ",\n\t\t \"longitude\": " +  row['Takeout_Longitude'] + "\n\t },"    


# In[257]:


orS1 = orS1[:-1] + "],\n"
destS1 = destS1[:-1] + "],"
orS2 = orS2[:-1] + "],\n"
destS2 = destS2[:-1] + "],"
orS3 = orS3[:-1] + "],\n"
destS3 = destS3[:-1] + "],"
 
payload1 = orS1 + destS1 + travS
payload2 = orS1 + destS2 + travS
payload3 = orS1 + destS3 + travS
payload4 = orS2 + destS1 + travS
payload5 = orS2 + destS2 + travS
payload6 = orS2 + destS3 + travS
payload7 = orS3 + destS1 + travS
payload8 = orS3 + destS2 + travS
payload9 = orS3 + destS3 + travS


# In[258]:


print(payload4)


# In[259]:


headers = {
  'Content-Length': '10000',
  'Content-Type': 'application/json'
}

response1 = requests.request("POST", url, headers=headers, data = payload1)
response2 = requests.request("POST", url, headers=headers, data = payload2)
response3 = requests.request("POST", url, headers=headers, data = payload3)
response4 = requests.request("POST", url, headers=headers, data = payload4)
response5 = requests.request("POST", url, headers=headers, data = payload5)
response6 = requests.request("POST", url, headers=headers, data = payload6)
response7 = requests.request("POST", url, headers=headers, data = payload7)
response8 = requests.request("POST", url, headers=headers, data = payload8)
response9 = requests.request("POST", url, headers=headers, data = payload9)


# In[262]:


dict11 = response1.json().get('resourceSets')[0].get('resources')[0].get('results')
dict12 = response2.json().get('resourceSets')[0].get('resources')[0].get('results')
dict13 = response3.json().get('resourceSets')[0].get('resources')[0].get('results')
dict21 = response4.json().get('resourceSets')[0].get('resources')[0].get('results')
dict22 = response5.json().get('resourceSets')[0].get('resources')[0].get('results')
dict23 = response6.json().get('resourceSets')[0].get('resources')[0].get('results')
dict31 = response7.json().get('resourceSets')[0].get('resources')[0].get('results')
dict32 = response8.json().get('resourceSets')[0].get('resources')[0].get('results')
dict33 = response9.json().get('resourceSets')[0].get('resources')[0].get('results')


# In[315]:


distanceMatrix = numpy.empty([114,114])
timeMatrix = numpy.empty([114,114])


# In[316]:


j = 0
k = 0
for i,data in enumerate(dict11):
    if i % 50 == 0 and i != 0:
        k = 0
        j += 1    
    distanceMatrix[j][k] = data.get('travelDistance')
    timeMatrix[j][k] = data.get('travelDuration')
    k += 1


# In[317]:


j = 0
k = 0
for i,data in enumerate(dict12):
    if i % 50 == 0 and i != 0:
        k = 0
        j += 1    
    distanceMatrix[j][k + 50] = data.get('travelDistance')
    timeMatrix[j][k + 50] = data.get('travelDuration')
    k += 1


# In[318]:


j = 0
k = 0
for i,data in enumerate(dict13):
    if i % 14 == 0 and i != 0:
        k = 0
        j += 1    
    distanceMatrix[j][k + 100] = data.get('travelDistance')
    timeMatrix[j][k + 100] = data.get('travelDuration')
    k += 1


# In[319]:


j = 0
k = 0
for i,data in enumerate(dict21):
    if i % 50 == 0 and i != 0:
        k = 0
        j += 1    
    distanceMatrix[j + 50][k] = data.get('travelDistance')
    timeMatrix[j + 50][k] = data.get('travelDuration')
    k += 1


# In[320]:


j = 0
k = 0
for i,data in enumerate(dict22):
    if i % 50 == 0 and i != 0:
        k = 0
        j += 1    
    distanceMatrix[j + 50][k + 50] = data.get('travelDistance')
    timeMatrix[j + 50][k + 50] = data.get('travelDuration')
    k += 1


# In[321]:


j = 0
k = 0
for i,data in enumerate(dict23):
    if i % 14 == 0 and i != 0:
        k = 0
        j += 1    
    distanceMatrix[j + 50][k + 100] = data.get('travelDistance')
    timeMatrix[j + 50][k + 100] = data.get('travelDuration')
    k += 1


# In[322]:


j = 0
k = 0
for i,data in enumerate(dict31):
    if i % 50 == 0 and i != 0:
        k = 0
        j += 1    
    distanceMatrix[j + 100][k] = data.get('travelDistance')
    timeMatrix[j + 100][k] = data.get('travelDuration')
    k += 1


# In[323]:


j = 0
k = 0
for i,data in enumerate(dict32):
    if i % 50 == 0 and i != 0:
        k = 0
        j += 1    
    distanceMatrix[j + 100][k + 50] = data.get('travelDistance')
    timeMatrix[j + 100][k + 50] = data.get('travelDuration')
    k += 1


# In[324]:


j = 0
k = 0
for i,data in enumerate(dict33):
    if i % 14 == 0 and i != 0:
        k = 0
        j += 1    
    distanceMatrix[j + 100][k + 100] = data.get('travelDistance')
    timeMatrix[j + 100][k + 100] = data.get('travelDuration')
    k += 1


# In[339]:


print(distanceMatrix)


# In[326]:


print(timeMatrix)


# In[338]:


numpy.savetxt('DistanceMatrix.csv', distanceMatrix, delimiter=',')
numpy.savetxt('TimeMatrix.csv', timeMatrix, delimiter=',')


# In[ ]:




