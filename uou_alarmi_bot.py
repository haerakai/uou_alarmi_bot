# -*- encoding:utf-8 -*-
__author__ = 'haerakai & molkoo'

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

token = 'input your token'

home = os.path.expanduser("~")
path_userdb = home + '/uou_alarmi_bot/userdb'

def init_users():
	if os.path.exists(path_userdb):
		with open(path_userdb, 'r+') as f:
			global users
			users = f.read().splitlines()
	else:
		with open(path_userdb, 'w') as f:
			global users
			users = []

def start(bot, update):
	user_id = update.message.chat_id
	if not str(user_id) in users:
		with open(path_userdb, 'a') as f:
			f.write(str(user_id)+'\n')
		users.append(str(user_id))
		msg = '가입 완료. 울산대 알리미가 알림을 시작합니다.'
	else:
		msg = '이미 가입하셨습니다.'
	
	bot.sendMessage(chat_id=user_id, text=msg)

def stop(bot, update):
	user_id = update.message.chat_id
	if str(user_id) in users:
		users.remove(str(user_id))
		with open(path_userdb, 'w+') as f:
			for user in users:
				f.write(str(user)+'\n')
		msg = '탈퇴 완료. 울산대 알리미가 더이상 알림을 보내지 않습니다.'
	else:
		msg = '아직 가입하지 않으셨습니다.'
	
	bot.sendMessage(chat_id=user_id, text=msg)

updater = Updater(token)
dispatcher = updater.dispatcher

init_users()

start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)

updater.start_polling()
