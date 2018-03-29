# Import necessary selenium libraries
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Python Module libraries
import time
import threading
import os
import subprocess

# Argument Parse for Parsing whether to use Chrome Driver or Geckodriver
import argparse

# Start the argparse
parser = argparse.ArgumentParser()
parser.add_argument("--chrome", help="Using Chrome Driver")
parser.add_argument("--mozilla", help="Using Gecko Driver")
args = parser.parse_args()
if args.chrome:
	d = webdriver.Chrome('drivers/chromedriver')  
elif args.mozilla:
	d = webdriver.Chrome('drivers/geckodriver')  
else:
	print("Select a valid option")
	exit(0)

# Start the browser and get Whatsapp Web
d.get('https://web.whatsapp.com')
d.implicitly_wait(10)
d.get("https://web.whatsapp.com")

# Encoding Values
_B = '\033[1m'
B_ = '\033[0m'
ON = u"\u2022"

# Global Variables
last_seen = 0
currentChat = ""
currentChatState = 0

# Get Time for the chat
def get_time():
	return int(round(time.time()))

last_seen = get_time()

def select_chat(Chat):
	global currentChat
	global currentChatState
	if Chat.lower() in currentChat.lower():
		return
	try:
		inp = d.find_elements_by_class_name('input')
		inp[0].send_keys(' ')
		d.find_element_by_class_name('chat-body').click()
		inp[0].send_keys(Chat)
		time.sleep(1)
		chat = d.find_elements_by_class_name('infinite-list-item')
		chatName = chat[0].find_element_by_class_name('emojitext').get_attribute('title')
		print(chatName)
		if Chat.lower() in chatName.lower():
			currentChat=chatName
			chat[0].click()
			chat_state = d.find_elements_by_class_name('pane-header')[1]
			state = chat_state.find_elements_by_class_name('emojitext')[1].get_attribute('title')
			currentChatState = (state=="online")
			print("Chat "+currentChat+" selected")
		else:
			print("Failed to select Chat "+ Chat)
	except:
		print("Failed to select Chat "+ Chat)

def send_message(msg):
	try:
		inp = d.find_elements_by_class_name('input')
		inp[1].send_keys(msg)
		d.find_element_by_class_name('compose-btn-send').click()
	except:
		print("Failed to send message")

def send_message_to(chat, msg):
	try:
		select_chat(chat)
		send_message(msg)
	except:
		print("Failed to send message")

def get_unread():
	global last_seen
	script = open("js/get_unread.js", "r").read()
	script = "var last_seen = "+str(last_seen)+";\n"+script
	script = "var currentChat = \""+currentChat+"\";\n"+script	
	last_seen = get_time()
	chats =  d.execute_script(script)
	return chats

def get_read():
	global last_seen
	script = open("js/get_read.js", "r").read()
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
		print("\n" + r + "\n")
		if len(s):
			print(s)
	except:
		print("Failed to get unread messages")

def write2file():
	try:
		chats = get_read()
		i=0
		for unread in chats:
			s = ""
			chat = unread['name']
			f = open("chats/"+ chat.encode('utf-8'), "w")
			for msg in unread['messages']:
				s += msg['msg'].encode('utf-8')+"\n"
				i += 1
			if len(s):
				f.write(s)
			f.close()
	except:
		print("Failed to get messages")

query = ""

while query!="quit":
	if len(currentChat)>0:
		if currentChatState:
			query = input(ON.encode('utf=8')+' '+currentChat.encode('utf-8')+" # ")
		else:
			query = input(currentChat.encode('utf-8')+" # ")
	else:
		query = input("# ")
	query = query.strip()
	q = query[0:3].strip()
	s = query[3:].strip()
	if q=="sc":
		chat = s
		select_chat(chat)
	elif q=="sm":
		msg = s
		send_message(msg)
	elif q=="um":
		print_unread()
	elif q=="gc":
		write2file()
		print("All chats are now accessible ...")
		subprocess.Popen(["scripts/read.sh"])
	elif query!="quit" and len(query)>0:
		print("Invalid input")

# Close the Web Driver
d.quit()