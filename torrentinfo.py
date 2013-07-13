import bencode
from time import gmtime
from hashlib import sha1

def sizeof_fmt(num):
    for x in ['bytes','KB','MB','GB','TB']:
        if num < 1024.0:
            return "%3.2f %s" % (num, x)
        num /= 1024.0
		
class torrentinfo:
	name = None
	hash = None
	length = 0
	name = None
	files = None
	comment = None
	date = None
	def __init__(self, filename = None, url  = None):
		filestream = None
		if filename <> None:
			filestream = open(filename, "rb").read()			
		elif url <> None:
			pass
			#TODO: add url download
		else:
			raise Exception('initial error')		
		metainfo = bencode.bdecode(filestream)
		info = metainfo['info']
		startpos = filestream.find(":infod")
		if startpos != -1 :			
			hashstring = filestream[startpos+5:startpos+5+len(bencode.bencode(info))]
		else :
			hashstring = bencode.bencode(info)
		self.hash = sha1(hashstring).hexdigest().upper()	
		if 'files' in info:
			self.files = info['files']
			for i in self.files:
				self.length += i['length']
		else:			
			self.length = info['length']
			self.files = ({'path':(info['name'],),'length':info['length']},)
		self.comment = metainfo['comment']
		currenttime = gmtime(metainfo['creation date'])
		self.date = "%02i.%02i.%i" % (currenttime.tm_mday,currenttime.tm_mon,currenttime.tm_year)
		self.name = info['name']