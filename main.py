# Lolipop by RgTQUg, 2016
# Feel free to use/modify as you wish, just don't claim you made it yourself or anything.

from modules import searchmodules, searchmodules_ero
import sys

def Search():
	try:
		choice = raw_input("> ")
		if choice == '1':
			print "Please enter your search terms."
			searchTerm = raw_input("> ")
			page_no = 1
			searchmodules.FetchResults(searchTerm, page_no)
		elif choice == '2':
			print "Please enter your search terms."
			searchTerm = raw_input("> ")
			page_no = 1
			searchmodules_ero.FetchResults(searchTerm, page_no)
		else:
			print "Please enter a valid choice."
			Search()
	except KeyboardInterrupt:
		print "Goodbye!"
		sys.exit()

#This is all really bare bones. Take a look at the 'modules' folder for a more in-depth documentation.

print "SFW or NSFW?\n1.Safe\n2.Explicit"
Search()
