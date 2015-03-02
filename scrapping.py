import urllib
import re

#connect to a URL
url= "" 			#add the url
website = urllib.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall(r'"[-_a-zA-Z0-9]+.pdf"', html)

for i in links:	
	file= url+i.strip('\"')
	name=i.strip('\"')
	testfile=urllib.URLopener()
	testfile.retrieve(file,name)
	print file+name
print "done=========================================="