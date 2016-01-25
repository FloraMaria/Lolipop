import libtorrent as lt
import time
import sys
import requests
import urllib
from lxml import html
import searchmodules
import searchmodules_ero
import os

def Torrent(num, titles, download_links):
	# Fetch the torrent file.
	urllib.urlretrieve(download_links[num], "torrent.torrent")
	
	# Initiate the libtorrent session.
	session = lt.session()
	session.listen_on(6881, 6891)
	
	# Begin downloading.
	info = lt.torrent_info("torrent.torrent")
	h = session.add_torrent({'ti': info, 'save_path': './'})
	print 'starting', h.name()
	
	while (not h.is_seed()):
		s = h.status()

		state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
		print '\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]),
		sys.stdout.flush()

		time.sleep(1)

		print h.name(), 'complete'
	
	# Gotta remove that torrent file.
	os.remove('torrent.torrent')
	searchmodules.search()
	
def Torrent_Ero(num, titles, download_links):
	urllib.urlretrieve(download_links[num], "torrent.torrent")
	
	session = lt.session()
	session.listen_on(6881, 6891)
	
	info = lt.torrent_info("torrent.torrent")
	h = session.add_torrent({'ti': info, 'save_path': './'})
	print 'starting', h.name()
	
	while (not h.is_seed()):
		s = h.status()

		state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
		print '\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]),
		sys.stdout.flush()

		time.sleep(1)

		print h.name(), 'complete'
	
	os.remove('torrent.torrent')
	searchmodules_ero.search()
	
