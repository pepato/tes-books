#!/usr/local/bin/python
# coding: utf-8
# a small script by Fra Enrico aka Pepato to handle and edit Elder Scrolls book texts from The Imperial Library
from __future__ import print_function # to write to file with Python 3 syntax - this needs to go on top
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# let's open our index-list file
# soup = BeautifulSoup(open("by-title-skyrim.html")) #remeber to use the right index file according to the books you want to import
soup = BeautifulSoup(open("by-title-oblivion.html")) #remeber to use the right index file according to the books you want to import

ldir = []
for link in soup.find(id='content').find_all("a"):
	# print(link.get("href")) # test
	ldir.append(link.get("href"))

# print(ldir) #test

# function to read the file, clean it up and create the prettified output
def zupparic(file_book):
	# open the file to edit
	source = open("./"+file_book+".html")

	# telling SoupStrainer what I want from the source html
	main = SoupStrainer(id='main')

	# making the soup
	content = BeautifulSoup(source, "html.parser", parse_only=main) #need to specify the parser cause html5 doesn't work with SoupStrainer

	# cleaning away with decompose the stuff I don't need
	content.find("div", id="main").unwrap() #stripping away the container tag, cause the epub chapter must begin with h1

	# since not all files are equal, I must handle exceptions
	try:
		content.find("div", class_="breadcrumb").decompose()
	except AttributeError:
		pass
	try:
		content.find("div", class_="node-submitted").decompose()
	except AttributeError:
		pass
	try:
		content.find("div", class_="field-field-comment").decompose()
	except AttributeError:
		pass
	try:
		content.find("div", class_="book-navigation").decompose()
	except AttributeError:
		pass
	try:
		content.find("div", class_="terms terms-inline").decompose()
	except AttributeError:
		pass
	try:
		content.find("img").decompose()
	except AttributeError:
		pass

	# prettify everything
	final = content.prettify("utf-8")

	# writing the file
	# watch out the directories of input and output, make sure the paths are correct: uri names must be built right
	file_out = "./out"+str(file_book)+".html" #renaming files
	pretty = open(file_out,"w")
	print(final, file=pretty)
	pretty.close()
	# maybe you can do this with fewer lines, but whatever
	# now the /out folder should contain all the books ready to be imported. You will need to delete *manually* the ones you don't want

# zupparic("gods-and-worship.html") # test

# running the function ricoursively on each file
for book in ldir:
	zupparic(book)

