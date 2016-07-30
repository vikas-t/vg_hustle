#!/usr/bin/python

import sys,re, urllib
from bs4 import BeautifulSoup as bs

exclude_words = ["href=", '\\']

def scrape_web(url):
	res = []
	r_ex = r"(.+\?)[^<>;]*?<"
	
	r = urllib.urlopen(url).read()
	if not r:
		return False
	soup = bs(r, "html.parser")
	data =  soup.prettify().encode("utf-8")
	for ques in re.findall(r_ex, data):
		flag = True
		for word in exclude_words:
			if word in ques:
				flag = False
		if flag:
			res.append(ques.strip())
	return res
	