#-*- coding: utf-8 -*-
import urllib
import string
import progressbar
import time
import sys
from time import sleep

# parsing function
def funcParse(verse):
	global chapter
	global Page
	global pNum

	findingStr = '>' + verse
	
	# find the words
	pNum = string.find(Page, '>' + chapter + ':')
	if int(verse) == int(chapter) and verse != '1' : 
		pNum = pNum + 1
	if verse != '1' : 
		pNum = string.find(Page, findingStr, pNum) # go to specific verse
		
	pNum = string.find(Page, "</span>", pNum)
	pStart = pNum
	
	pEnd = string.find(Page, '\n', pStart)
	

	return Page[pStart:pEnd]
	
	
	
def funcModify(Word):
	# remove <i>
	Word = string.replace(Word, '<i>' , '')
	Word = string.replace(Word, '</i>', '')
	# replace &#8220; and stuffs
	Word = string.replace(Word,'&#8220;', '"')
	Word = string.replace(Word,'&#8221;', '"')
	Word = string.replace(Word,'&#8217;', "'")
	Word = string.replace(Word,'&#8216;', "'")
	Word = string.replace(Word, ',&nbsp;', " ")
	Word = string.replace(Word, '&nbsp;', "")
	# remove span
	eraseStart = 0
	eraseEnd = 0
	eraseFlag = 0
	pointer = 0
	
	while 1:
		if pointer >= len(Word):
			break
		if Word[pointer] == '<':
			eraseFlag = 1
			eraseStart = pointer
		elif Word[pointer] == '>':
			eraseFlag = 2
			eraseEnd = pointer
		if eraseFlag == 2:
			Word = Word[:eraseStart] + Word[eraseEnd+1:]
			pointer = pointer - (1+eraseEnd-eraseStart)
			eraseFlag = 0
		pointer+=1
			
			
	string.find(Word, '<span')
	
	#remove spaces at head
	for i in Word:
		if i == ' ' :
			Word = string.lstrip(Word)
		elif i != ' ' : 
			break
		
	
	
	return Word
	
def funcAddrTrans(addr, book):
	Kor = ['Ã¢', 'Ãâ', '·¹', '¹Î', '½Å', '¼ö', '»ñ', '·í', '»ï»ó', '»ïÇÏ', 
		   '¿Õ»ó', '¿ÕÇÏ', '´ë»ó', '´ëÇÏ', '½º', '´À', '¿¡', '¿é', '½Ã', 'Àá',
		   'Àü', '¾Æ', '»ç', '·½', '¾Ö', '°Ö', '´Ü', 'È£', '¿ç', '¾Ï',
		   '¿É', '¿æ', '¹Ì', '³ª', 'ÇÕ', '½À', 'ÇÐ', '½»', '¸»', '¸¶',
		   '¸·', '´ª', '¿ä', 'Çà', '·Ò', '°íÀü', '°íÈÄ', '°¥', '¿¦', 'ºô',
		   '°ñ', '»ìÀü', '»ìÈÄ', 'µõÀü', 'µõÈÄ', 'µó', '¸ó', 'È÷', '¾à', 'º¦Àü',
		   'º¦ÈÄ', '¿äÀÏ', '¿äÀÌ', '¿ä»ï', 'À¯', '°è'
		   ]
	Eng = ['Gen', 'Exo', 'Lev', 'Num', 'Deut', 'Josh', 'Judg', 'Rth', '1Sam', '2Sam',
	       '1Kgs', '2Kgs', '1Ch', '2Ch', 'Ezra', 'Neh', 'Esth', 'Job', 'Pslm', 'Prov',
		   'Ecc', 'Song', 'Isa', 'Jer', 'Lam', 'Ezek', 'Dan', 'Hos', 'Joel', 'Amos',
		   'Obad', 'Jon', 'Micah', 'Nah', 'Hab', 'Zeph', 'Hag', 'Zech', 'Mal', 'Mt',
		   'Mrk', 'Luk', 'Jhn', 'Acts', 'Rom', '1Co', '2Co', 'Gal', 'Eph', 'Php',
		   'Col', '1Th', '2Th', '1Ti', '2Ti', 'Tit', 'Phm', 'Heb', 'Jas', '1Pe',
		   '2Pe', '1Jn', '2Jn', '3Jn', 'Jud', 'Rev'
		   ]
		   
	
	try : 
		return Eng[Kor.index(book)]
	except ValueError :
		addr = string.rstrip(addr)
		print "We found %s is not in the bible" % book
		print "Check if typed right"
		print "the whole address you enter was : '%s'" % addr
		sys.exit(1)
		time.sleep(3)
		
		
''' 
		MAIN PROJECT STARTS HERE
'''

	
# start progress ( calculate with progress bar )
from progressbar import ProgressBar
pbar = ProgressBar()	
	
# read file 
try: 
	f = open("input.txt", 'r')
	print "READING COMPLETE"
	time.sleep(0.1)
	addrList = f.readlines()
except IOError: 
	print ("'input.txt' file does not exist")
	print ("Please create one to proceed")
	sys.exit(3)
	time.sleep(3)
 
# Output File
output = open("output.txt", 'w')

# loop by each input
print "EXTRACTING..."

for addr in pbar(addrList) :
	flag = 0
	book = ''
	chapter = ''
	vStart = ''
	vEnd = ''
	
	''' updated since v 1.1 
	
	# show word address in Korean first ( write to the file )
	addr = string.rstrip(addr)
	output.write(addr)
	output.write('\n')
	'''
	
	# parsing address 
	for i in addr :
		if i == ' ' :
			continue
		if i == '\n' :
			break
		if i >= '0' and i <= '9' and flag == 0 :  
			chapter += i
		elif i == ':' or i == ';' : 
			flag = 1
		elif i == '~' or i == '-' :
			flag = 2
		elif flag == 1 and i>= '0' and i <= '9' :
			vStart += i
		elif flag == 2 and i>= '0' and i <= '9' :
			vEnd += i
		else :
			book += i
	
	book = funcAddrTrans(addr, book)
	urlStr = "http://nasb.literalword.com/?q="
	urlStr = urlStr + book + '+' + chapter
	ur = urllib.urlopen(urlStr)
	Page = ur.read()

	# put pointer to the proper point by setting findingStr
	if vEnd : 
		cnt = int(vEnd) - int(vStart) + 1
		for i in range(cnt) :
			Word = funcModify(funcParse(str(i+int(vStart))))
			OutputAddr = '(' + book + ' ' + chapter + ':' + str ( int(vStart) + i ) + ')'
			output.write(OutputAddr + ' ' + Word + '\n')
	else :
		Word = funcModify(funcParse(vStart))
		OutputAddr = '(' + book + ' ' + chapter + ':' + vStart + ')'
		output.write(OutputAddr + ' ' + Word + '\n')
		
	output.write('\n')
	
print "CONGRATS! ALL EXTRACTION COMPLETE!!!"
print "SOLI DEO GLORIA !!!"

output.close()
f.close()

time.sleep(3)
		
	
	
 


