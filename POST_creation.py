# coding: utf-8
# Author: Ryan Lisowski 2/2020
# Post_creation retrieves distance and travel time data from the microsoft distancematrix API. It creates a .JSON file
# by reading in latitude,longitude pairs from a .csv file. Outputs distance and travel time matrices to .csv files.


import csv
import requests
import numpy
import math


# URL string and key for API requests
url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key=..."

# Strings for origins and destinations with start of JSON formatting
orS1 = "{\n\t\"origins\": ["
destS1 = "\"destinations\": ["
# Specifies travel time should be calculated for driving
travS = "\n\"travelMode\": \"driving\"\n}"

# .csv file with access and takeout latitude and longitudes.
csv1 = "rivers_20.csv"
with open(csv1, newline='') as csvfile1:
    reader = csv.DictReader(csvfile1)
    # retrieve access, takeout coordinates for each river section, add them to a JSON formatted string.
    for row in reader:
        destS1 = destS1 + "\n\t{\n\t\t \"latitude\": " + row['Access_Latitude'] + ",\n\t\t \"longitude\": " +  row['Access_Longitude'] + "\n\t },"
        orS1 = orS1 + "\n\t{\n\t\t \"latitude\": " + row['Takeout_Latitude'] + ",\n\t\t \"longitude\": " +  row['Takeout_Longitude'] + "\n\t },"


# Remove comma from end of strings, add content ending characters.
orS1 = orS1[:-1] + "],\n"
destS1 = destS1[:-1] + "],"

# Create payload string (string in JSON format)
payload1 = orS1 + destS1 + travS

# Headers for POST API request
headers = {
  'Content-Length': '3500',
  'Content-Type': 'application/json'
}

# Make POST request, store API response
response1 = requests.request("POST", url, headers=headers, data = payload1)

# Extract dictionary of travel times and distances from API response
dict11 = response1.json().get('resourceSets')[0].get('resources')[0].get('results')

# Size of distance matrix
rivers = int(math.sqrt(len(dict11)))

# Preallocate empty matrices for distances and travel times.
distanceMatrix = numpy.empty([rivers,rivers])
timeMatrix = numpy.empty([rivers,rivers])

# row index
j = 0
# column index
k = 0

# Iterate through nested dictionaries in API response
for i,data in enumerate(dict11):
    # after retrieving all data for one origin
    if i % rivers == 0 and i != 0:
        # reset column index
        k = 0
        # increment row index
        j += 1

    # populate matrices
    distanceMatrix[j][k] = data.get('travelDistance')
    timeMatrix[j][k] = data.get('travelDuration')
    # increment column index
    k += 1

# Output matrices to .csv files
numpy.savetxt('DistanceMatrix.csv', distanceMatrix, delimiter=',')
numpy.savetxt('TimeMatrix.csv', timeMatrix, delimiter=',')






