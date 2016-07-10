# -*- encoding:utf-8 -*-

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

token = 'input your token'

home = os.path.expanduser("~")
path_userdb = home + '/uou_alarmi_bot/userdb'
path_crawldb = home + '/uou_alarmi/uou_alarmi/spiders/crawldb'

def init_users():
	if os.path.exists(path_userdb):
		with open(path_userdb, 'r+') as f:
			global users
			users = f.read().splitlines()
	else:
		with open(path_userdb, 'w') as f:
			global users
			users = []

def broad():
	dates = []
	names = []
	titles = []
	links = []

	with open(path_crawldb, 'r+') as f:
		data = f.read().splitlines()

	n = len(data)
	for i in range(0,n,4):
		msg = '등록일 : ' + data[i] + '\n' + '회사명 : ' + data[i+1] + '\n' + '업무내용 : ' + data[i+2] + '\n' + '바로가기 : http://www.ulsan.ac.kr/utopia/info/arbeit/' + data[i+3]
		for user in users:
			updater.bot.sendMessage(chat_id=user, text=msg)

updater = Updater(token)

init_users()
broad()

os._exit(0)
