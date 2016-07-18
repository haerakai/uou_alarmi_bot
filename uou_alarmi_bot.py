# -*- encoding:utf-8 -*-
__author__ = 'haerakai & molkoo'

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os, urllib3
import MySQLdb.cursors

urllib3.disable_warnings()

token = 'your_token'

def start(bot, update):
	try:
		conn = MySQLdb.connect(user='user', passwd='passwd', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
		cursor = conn.cursor()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)


	user_id = update.message.chat_id

	try:
		cursor.execute("""select * from uou_alarmi_userdb where userid=%s""" % str(user_id))
		result = cursor.fetchone()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	
	if result:
		msg = '이미 가입하셨습니다.'
	
	else:
		try:
			cursor.execute("""insert into uou_alarmi.uou_alarmi_userdb (userid) values (%s)""" % str(user_id))
			conn.commit()
			msg = '가입 완료. 울산대 알리미가 알림을 시작합니다.'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	conn.close()
	bot.sendMessage(chat_id=user_id, text=msg)
	
def stop(bot, update):
	try:
		conn = MySQLdb.connect(user='molkoo', passwd='7qmffor', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
		cursor = conn.cursor()
		
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)

	user_id = update.message.chat_id

	try:	
		cursor.execute("""select * from uou_alarmi_userdb where userid = %s""" % str(user_id))
		result = cursor.fetchone()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	
	if result:
		try:
			cursor.execute("""delete from uou_alarmi_userdb where userid = %s""" % (str(user_id)))
			conn.commit()
			msg = '탈퇴 완료. 울산대 알리미가 더이상 알림을 보내지 않습니다.'
	
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	else:	
		msg = '탈퇴 불가. 가입되어 있지 않습니다.'
	
	conn.close()
	bot.sendMessage(chat_id=user_id, text=msg)

updater = Updater(token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)

updater.start_polling()
