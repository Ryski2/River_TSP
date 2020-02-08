#!/usr/bin/env python
# coding: utf-8
# Author: Ryan Lisowski
# Used to assist in generating GET requests for the bing maps API.
# Requests are used to retrieve labeled maps with route information.

# In[20]:


import csv


# In[28]:


i = 1
pp = ""
csv1 = "rivers_20.csv"
with open(csv1, newline='') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        pp = pp + "pp=" + row['Access_Latitude'] + "," + row['Access_Longitude'] + ";;" + str(i) + "&"
        i += 1


# In[29]:


print(pp)


# In[ ]:


#main:
#https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes/Driving?waypoint.1=47.246021,-123.840561;55;1&waypoint.2=47.5606,-123.887001;55;2&waypoint.3=47.963402,-124.038002;55;3&waypoint.4=47.9604,-124.258003;55;4&key=... = 47.246021,-123.840561
#wp2 = 47.5606,-123.887001
#wp3 = 47.963402,-124.038002
#wp4 = 47.9604,-124.258003

#https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes/Driving?waypoint.1=47.9254,-121.277893&waypoint.2=45.740299,-121.227402&pp=47.9604,-124.258003&pp=46.1506,-122.585999&pp=47.322498,-121.906998&pp=47.857376,-123.943352&pp=47.364529,-123.724533&pp=47.607899,-120.917&pp=46.126099,-121.290001&pp=45.831337,-122.389191&pp=47.5606,-123.887001&pp=46.847198,-122.331001&pp=46.743801,-118.202003&pp=48.0969,-121.389&pp=47.963402,-124.038002&pp=47.9254,-121.277893&pp=45.632401,-116.475998&pp=47.487926,-121.389542&pp=47.971298,-121.700996&pp=47.809694,-120.715098&pp=47.592098,-120.658997&pp=45.851501,-121.509003&dcl=1&key=...

#variation 2
#wp 1 = 47.9254,-121.277893
#wp 2 = 45.740299,-121.227402

#https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/47.319048,-120.44384/7?mapSize=750,500&pp=47.9604,-124.258003;;1&pp=46.1506,-122.585999;;2&pp=47.322498,-121.906998;;3&pp=47.857376,-123.943352;;4&pp=47.364529,-123.724533;;5&pp=47.607899,-120.917;;6&pp=46.126099,-121.290001;;7&pp=45.831337,-122.389191;;8&pp=47.5606,-123.887001;;9&pp=46.847198,-122.331001;;10&pp=46.743801,-118.202003;;11&pp=48.0969,-121.389;;12&pp=47.963402,-124.038002;;13&pp=47.9254,-121.277893;;14&pp=45.632401,-116.475998;;15&pp=47.487926,-121.389542;;16&pp=47.971298,-121.700996;;17&pp=47.809694,-120.715098;;18&pp=47.592098,-120.658997;;19&pp=45.851501,-121.509003;;20&dcl=1&key=...

