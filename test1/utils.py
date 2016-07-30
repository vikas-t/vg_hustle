#!/usr/bin/python

import sys,re, urllib
from bs4 import BeautifulSoup as bs

exclude_words = ["href=", "<", ">", ":", "/", '\\']
try:
	url = sys.argv[1]
except:
	pass

def scrape_web(url):
	res = []

	#url = "http://www.indiabix.com/computer-science/database-systems/"
	r = urllib.urlopen(url).read()
	soup = bs(r, "html.parser")
	data =  soup.prettify().encode("utf-8")
	r_ex = r"(.+\?).*[\n\s ]*?<"

	for ques in re.findall(r_ex, data):
		flag = True
		for word in exclude_words:
			if word in ques:
				flag = False
		if flag:
			res.append(ques)
	return res
	