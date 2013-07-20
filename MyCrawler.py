import urllib
 
def get_page(url):#This function is just to return the webpage contents; the source of the webpage when a url is given.
	try:
		f = urllib.urlopen(url)
		page = f.read()
		f.close()
  #print page
		return page
	except: 
		return ""
	return ""

def get_url(link):	
	page=get_page(link)

	links=[]
	start_pos=page.find('<a href=');
	if start_pos==-1:
		return links
	while True:
		link= extract(start_pos, page)
		if link:
			links.append(link)
		start_pos=page.find('<a href="', start_pos+1)
		if start_pos==-1:
			break
	return links
		
def extract(start_pos, page):
	start_pos=page.find('"', start_pos)
	end_pos=page.find('"', start_pos+1)
	link = page[start_pos+1: end_pos]
	if link[0]=='h':
		return link
	
for url in get_url('https://github.com/nhamlv-55/MyCrawler'):
	print url
