from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import aiml
import time
import threading

profile = FirefoxProfile("../../.mozilla/firefox/hrishi")
d = webdriver.Firefox(profile)
d.implicitly_wait(30)
d.get("https://web.whatsapp.com")

_B = '\033[1m'
B_ = '\033[0m'
ON = u"\u2022"

last_seen = 0

currentChat = ""
currentChatState = 0

bot = aiml.Kernel()
bot.learn("bot/eng.xml")

def get_time():
	return int(round(time.time()))

last_seen = get_time()

class myThread(threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self._stop = threading.Event()
	def run(self):
		respond_unread(self.threadID, self.stopped)
	def stop(self):
		self._stop.set()
	def stopped(self):
		return self._stop.isSet()

def select_chat(Chat):
	global currentChat
	global currentChatState
	if Chat.lower() in currentChat.lower():
		return
	try:
		inp = d.find_elements_by_class_name('input')
		inp[0].send_keys(' ')
		d.find_element_by_class_name('icon-search-morph').click()
		inp[0].send_keys(Chat)
		time.sleep(0.2)
		chat = d.find_elements_by_class_name('infinite-list-item')
		chatName = chat[0].find_element_by_class_name('emojitext').get_attribute('title')
		if Chat.lower() in chatName.lower():
			currentChat=chatName
			chat[0].click()
			chat_state = d.find_elements_by_class_name('pane-header')[1]
			state = chat_state.find_elements_by_class_name('emojitext')[1].get_attribute('title')
			currentChatState = (state=="online")
			print "Chat "+currentChat+" selected"
		else:
			print "Failed to select Chat "+Chat
	except:
		print "Failed to select Chat "+Chat

def send_message(msg):
	try:
		inp = d.find_elements_by_class_name('input')
		inp[1].send_keys(msg)
		d.find_element_by_class_name('send-container').click()
	except:
		print "Failed to send message"

def send_message_to(chat, msg):
	try:
		select_chat(chat)
		send_message(msg)
	except:
		print "Failed to send message"

def get_unread():
	global last_seen
	script = open("js/get_unread.js", "r").read()
	script = "var last_seen = "+str(last_seen)+";\n"+script
	script = "var currentChat = \""+currentChat+"\";\n"+script	
	last_seen = get_time()
	chats =  d.execute_script(script)
	return chats

def print_unread():
	try:
		chats = get_unread()
		s = ""
		i=0
		for unread in chats:
			chat = unread['name']
			for msg in unread['messages']:
				s += _B+chat.encode('utf-8')+" : "+B_
				s += msg['msg'].encode('utf-8')+"\n"
				i += 1
		r = str(i)+" messages"
		if i>0:
			r += " from "+str(len(chats))+" chats"
		print "\n"+r+"\n"
		if len(s):
			print s
	except:
		print "Failed to get unread messages"

def respond_unread(threadID, isDead):
	while not isDead():
		chats = get_unread()
		for unread in chats:
			chat = unread['name']
			for msgs in unread['messages']:
				msg = msgs['msg']
				res = bot.respond(msg)
				if len(res)>0 and  'nOaNsWeR' not in res:
					#print "msg :"+msg
					#print "res :"+res+"\n"
					send_message_to(chat, res)
		time.sleep(10)

query = ""

botThread = myThread(1, "hrily")

while query!="quit":
	if len(currentChat)>0:
		if currentChatState:
			query = raw_input(ON.encode('utf=8')+' '+currentChat.encode('utf-8')+" # ")
		else:
			query = raw_input(currentChat.encode('utf-8')+" # ")
	else:
		query = raw_input("# ")
	query = query.strip()
	q = query[0:3].strip()
	s = query[3:].strip()
	if q=="bot":
		if s=="start" and botThread.stopped()==0:
			try:
				botThread.start()
				print "Bot started"
			except:
				print "Failed to start Bot"
		elif s=="stop":
			try:
				botThread.stop()
				print "Bot stopped"
			except:
				print "Failed to stop Bot"
		else:
			print "Invalid input"
	elif q=="cc":
		chat = s
		select_chat(chat)
	elif q=="sm":
		msg = s
		send_message(msg)
	elif q=="un":
		print_unread()
	elif query!="quit" and len(query)>0:
		print "Invalid input"
		#if len(currentChat)>0:
			#send_message(s)
		#else
			#print "No current chat set"

if botThread.stopped()==0:
	botThread.stop()
d.quit()