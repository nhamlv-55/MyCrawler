import urllib
from collections import deque
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
	if len(link)>0 and link[0]=='h':
		return link
	
def crawl(start_link, max_depth):
	counter=0
	depth=0
	to_crawl=[start_link]
	crawled=[]
	next_depth=[]
	while to_crawl and depth<=max_depth:
		link=to_crawl.pop()
		if link not in crawled:
			counter+=1
			print counter, depth, link
			crawled.append(link)
			#~ if link.find("facebook")!=-1:
				#~ return 0
			current=get_url(link)
			for el in current:
				if el not in crawled:
					next_depth.append(el)
		if len(to_crawl)==0:
			to_crawl, next_depth=next_depth, []
			%print to_crawl
			depth+=1
	return 0
seed=raw_input("")
crawl(seed, 5)
#print len(index)
