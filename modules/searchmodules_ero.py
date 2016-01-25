import requests
import re
from lxml import html
import sys
import HTMLParser
import torrentmodules
import os

# The 'half-page' flag.
pageHalf = False
# Yes, this is the same as searchmodules.py, but for pornographic responses.

def TopBar(pg):
	print "Page: " + str(pg)
	print "No.  \tTitle\t\t\t\t\t\t\t\t\t\t\tSize\t\tType\t\t\t\tSeeders"
	print "=" * 175

def FetchResults(searchTerm, page_no):

	tmp = os.system('cls')
	tmp2 = os.system('clear')
	
	TopBar(page_no)
	search_term_array = searchTerm.split()
	search_site = "http://sukebei.nyaa.se/?page=search&cats=0_0&filter=0&term="
	
	for term in search_term_array:
		appended_string = "+" + term
		search_site += appended_string
		
	if page_no != 1:
		search_site += ("&offset=" + str(page_no))
		
	search_site += "&sort=2"
	page = requests.get(search_site)

	site = html.fromstring(page.content)
	titles = site.xpath('//td[@class="tlistname"]/a/text()')
	seeders_no = site.xpath ('//td[@class="tlistsn"]/text()')
	download_links = site.xpath('//td[@class="tlistdownload"]/a/@href')
	sizes = site.xpath('//td[@class="tlistsize"]/text()')
	types = site.xpath('//td[@class="tlisticon"]/a/img/@alt')
	links = site.xpath('//td[@class="tlistname"]/a/@href')
	
	i = 0
	for title in titles:
		if i <= 39:
			titleB = title.encode('ascii','ignore')
			info = (titleB[:73] + '...') if len(titleB) > 73 else titleB
			fin_title = info + (" " * (73 - len(info)))
			
			a_type = types[i]
			type_ = (a_type[:24] + '...') if len(a_type) > 24 else a_type
			fin_type = type_ + (" " * (24 - len(type_)))
			
			if i < 9:
				print str(i + 1) + "  |\t" + fin_title + "\t\t" + (sizes[i] + (" " * (9 - len(sizes[i])))) + "\t" + fin_type + "\t" + seeders_no[i]
			elif i >= 9:
				print str(i + 1) + " |\t" + fin_title + "\t\t" + (sizes[i] + (" " * (9 - len(sizes[i])))) + "\t" + fin_type + "\t" + seeders_no[i]
			i += 1
		else:
			break
			
	searchMenu(searchTerm, page_no, titles, seeders_no, download_links, types, sizes, links)
		
def SearchPage_SecondHalf(searchTerm, page_no):
	tmp = os.system('cls')
	tmp2 = os.system('clear')
	TopBar(page_no)
	
	search_term_array = searchTerm.split()
	search_site = "http://sukebei.nyaa.se/?page=search&cats=0_0&filter=0&term="
	
	for term in search_term_array:
		appended_string = "+" + term
		search_site += appended_string
		
	if page_no != 1:
		search_site += ("&offset=" + str(page_no))
		
	search_site += "&sort=2"
	page = requests.get(search_site)

	site = html.fromstring(page.content)
	titles = site.xpath('//td[@class="tlistname"]/a/text()')
	seeders_no = site.xpath ('//td[@class="tlistsn"]/text()')
	download_links = site.xpath('//td[@class="tlistdownload"]/a/@href')
	sizes = site.xpath('//td[@class="tlistsize"]/text()')
	types = site.xpath('//td[@class="tlisticon"]/img/@alt')
	
	i = 40
	for title in titles:
		if title is not titles[i]:
			continue
		elif i <= 79:
			titleB = title.encode('ascii','ignore')
			info = (titleB[:73] + '...') if len(titleB) > 73 else titleB
			fin_title = info + (" " * (73 - len(info)))
			
			a_type = types[i]
			type_ = (a_type[:24] + '...') if len(a_type) > 24 else a_type
			fin_type = type_ + (" " * (24 - len(type_)))
			
			if i < 49:
				print str(i - 39) + "  |\t" + fin_title + "\t\t" + (sizes[i] + (" " * (9 - len(sizes[i])))) + "\t" + fin_type + "\t" + seeders_no[i]
			elif i >= 49:
				print str(i - 39) + " |\t" + fin_title + "\t\t" + (sizes[i] + (" " * (9 - len(sizes[i])))) + "\t" + fin_type + "\t" + seeders_no[i]
			i += 1
		else:
			break
	
	searchMenu(searchTerm, page_no, titles, seeders_no, download_links, types, sizes, links)
			
# If/else statement after a search is brought up.
def searchMenu(searchTerm, page_no, titles, seeders_no, download_links, types, sizes, links):
	global pageHalf
	print "Enter a number to view that file. Enter \'e\' to exit the program. Enter \'s\' to search again. Enter \'n\' to go to the next page, and \'p\' to go to the previous.\n"
	while True:
		choice = raw_input("> ")

		try:
			if choice == 'e':
				print "Goodbye!"
				sys.exit()
			elif choice == 's':
				search()
			elif choice == 'n' and page_no < 5:
				if pageHalf == True:
					pageHalf = False
					page_no = page_no + 1
					FetchResults(searchTerm, page_no)
				else:
					pageHalf = True
					SearchPage_SecondHalf(searchTerm, page_no)
			elif choice == 'n' and page_no >=5:
				page_no = 1
				FetchResults(searchTerm, page_no)
			elif choice == 'p' and page_no > 1:
				if pageHalf == True:
					pageHalf = False
					page_no = page_no - 1
					FetchResults(searchTerm, page_no)
				else:
					pageHalf = True
					SearchPage_SecondHalf(searchTerm, page_no)
			elif choice == 'p' and page_no <= 1:
				page_no = 3
				FetchResults(searchTerm, page_no)
			else:
				num = int(choice) - 1
				viewFile(titles, seeders_no, download_links, types, sizes, num, links)
		except KeyboardInterrupt:
			print "Goodbye!"
			sys.exit()
		except:
			print "Invalid choice. Please re-enter your selection."
		
def search():
	tmp = os.system('cls')
	tmp2 = os.system('clear')
	print "Please enter your search terms."
	searchTerm = raw_input("> ")
	page_no = 1
	FetchResults(searchTerm, page_no)
	
def viewFile(titles, seeders_no, download_links, types, sizes, num, links):
	p_page = links[num] + "&showfiles=1"
	page = requests.get(p_page)
	page = html.fromstring(page.content)
	
	desc = page.xpath('//div[@class="viewdescription"]/text()')
	files = page.xpath('//td[@class="fileentryname"]/text()')

	print "=" * 175
	print "Info |"
	print "=" * 175
	print titles[num]
	print "Seeders: " + seeders_no[num]
	print types[num]
	print "Size: " + sizes[num]
	print "=" * 175
	print "Description |"
	print "=" * 175
	for lines in desc:
		print lines
	print "=" * 175
	print "Files Included in Torrent |"
	print "=" * 175
	for file_entries in files:
		print file_entries
		
	print "Would you like to download this file? (y/n)"
	while True:
		choice = raw_input("> ")
		
		if choice == 'y' or choice == 'Y':
			torrentmodules.Torrent_Ero(num, titles, download_links)
		elif choice == 'n' or choice == 'N':
			search()
		else:
			print "Please enter a valid choice."
