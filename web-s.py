# Uses https://www.edureka.co/blog/web-scraping-with-python/ as a base
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

URL_BASE = 'https://www.americanwhitewater.org'
FLOW_CUTOFF = 1000

# Requires that the chrome webdriver is in the PATHS variable on your OS
driver = webdriver.Chrome()

driver.get(URL_BASE + '/content/River/state-summary/?state=WA')
print(driver.current_url);
	
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

river_names = []
river_diffs = []
river_lengths = []
river_access_lats = []
river_access_longs = []
river_takeout_lats = []
river_takeout_longs = []
river_urls = []

for river in soup.find_all('tr'):
	flowts = river.select('.gauge_info > a')
	for flowt in flowts:
		flowstr = flowt.text.strip().split(' ')[0]
		if (flowstr.isnumeric() and int(flowstr) >= FLOW_CUTOFF):
			name = river.find('a', attrs = {'class': 'rivername'})
			subname = river.select('.river_extra > a')
			river_names.append(name.text.strip() + ' (' + subname[0].text.strip() + ')')
			river_urls.append(name['href'])

for url in river_urls:
	driver.get(URL_BASE + url);
	print(driver.current_url);
	
	content = driver.page_source
	soup = BeautifulSoup(content, 'html.parser')

	maininfos = soup.select('#river-main td')
	river_diffs.append(maininfos[1].text)
	river_lengths.append(maininfos[3].text.strip().split(' ')[0])

	accessinfo = soup.select('#access .sectionContent > a')

	accesscoords = accessinfo[0].text.split(',')
	river_access_lats.append(accesscoords[0].strip())
	river_access_longs.append(accesscoords[1].strip())

	takeoutcoords = accessinfo[1].text.split(',')
	river_takeout_lats.append(takeoutcoords[0].strip())
	river_takeout_longs.append(takeoutcoords[1].strip())

driver.quit()

print(river_names)
print(river_diffs)
print(river_lengths)
print(river_access_lats)
print(river_access_longs)
print(river_takeout_lats)
print(river_takeout_longs)

df = pd.DataFrame({
	'River_Name': river_names, 
	'Difficulties': river_diffs, 
	'Length(Miles)': river_lengths, 
	'Access_Latitude': river_access_lats,
	'Access_Longitude': river_access_longs,
	'Takeout_Latitude': river_takeout_lats,
	'Takeout_Longitude': river_takeout_longs})
df.to_csv('rivers.csv', index=False, encoding='utf-8')