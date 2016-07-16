# -*- encoding:utf-8 -*-
__author__ = 'haerakai & molkoo'

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os, urllib3
import MySQLdb.cursors

urllib3.disable_warnings()

token = 'insert token'

def start(bot, update):
	try:
		conn = MySQLdb.connect(user='alarmi', passwd='alarmi', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
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
			msg = '가입 완료. 울산대 알리미가 알림을 시작합니다.\n\n----UOU알라미 Command----\n시작하기 : /start\n중지하기 : /stop\n도움말 : /help\n문수장터 알림 : /sale\n문수알바 알림 : /arbeit\n문수복덕방 알림 : /room\ncicweb 공지 : /cic'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	conn.close()
	bot.sendMessage(chat_id=user_id, text=msg)
	
def stop(bot, update):
	try:
		conn = MySQLdb.connect(user='alarmi', passwd='alarmi', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
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

def help(bot, update):
	user_id = update.message.chat_id
	msg = '----UOU알라미 Command----\n시작하기 : /start\n중지하기 : /stop\n도움말 : /help\n문수장터 알림 : /sale\n문수알바 알림 : /arbeit\n문수복덕방 알림 : /room\ncicweb 공지 : /cic'
	bot.sendMessage(chat_id=user_id, text=msg)

def arbeit(bot, update):
	try:
		conn = MySQLdb.connect(user='alarmi', passwd='alarmi', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
		cursor = conn.cursor()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)


	user_id = update.message.chat_id

	try:
		cursor.execute("""select arbeit from uou_alarmi_userdb where userid=%s""" % str(user_id))
		result = cursor.fetchone()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	
	if result[0]==1:
		try:
			cursor.execute("""update uou_alarmi_userdb set arbeit = 0 where userid=%s""" % str(user_id))
			conn.commit()
			msg = '문수알바 알림을 해제합니다.'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	else:
		try:
			cursor.execute("""update uou_alarmi_userdb set arbeit = 1 where userid=%s""" % str(user_id))
			conn.commit()
			msg = 'UOU알라미가 최신 문수알바 내용을 알려줍니다.'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	conn.close()
	bot.sendMessage(chat_id=user_id, text=msg)

def room(bot, update):
	try:
		conn = MySQLdb.connect(user='alarmi', passwd='alarmi', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
		cursor = conn.cursor()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)


	user_id = update.message.chat_id

	try:
		cursor.execute("""select room from uou_alarmi_userdb where userid=%s""" % str(user_id))
		result = cursor.fetchone()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	
	if result[0]==1:
		try:
			cursor.execute("""update uou_alarmi_userdb set room = 0 where userid=%s""" % str(user_id))
			conn.commit()
			msg = '문수복덕방 알림을 해제합니다.'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	else:
		try:
			cursor.execute("""update uou_alarmi_userdb set room = 1 where userid=%s""" % str(user_id))
			conn.commit()
			msg = 'UOU알라미가 최신 문수복덕방 내용을 알려줍니다.'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	conn.close()
	bot.sendMessage(chat_id=user_id, text=msg)

def barter(bot, update):
	try:
		conn = MySQLdb.connect(user='alarmi', passwd='alarmi', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
		cursor = conn.cursor()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)


	user_id = update.message.chat_id

	try:
		cursor.execute("""select barter from uou_alarmi_userdb where userid=%s""" % str(user_id))
		result = cursor.fetchone()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	
	if result[0]==1:
		try:
			cursor.execute("""update uou_alarmi_userdb set barter = 0 where userid=%s""" % str(user_id))
			conn.commit()
			msg = '문수장터 알림을 해제합니다.'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	else:
		try:
			cursor.execute("""update uou_alarmi_userdb set barter = 1 where userid=%s""" % str(user_id))
			conn.commit()
			msg = 'UOU알라미가 최신 문수장터 내용을 알려줍니다.'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	conn.close()
	bot.sendMessage(chat_id=user_id, text=msg)

def cicweb(bot, update):
	try:
		conn = MySQLdb.connect(user='alarmi', passwd='alarmi', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
		cursor = conn.cursor()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)


	user_id = update.message.chat_id

	try:
		cursor.execute("""select cicweb from uou_alarmi_userdb where userid=%s""" % str(user_id))
		result = cursor.fetchone()
	
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	
	if result[0]==1:
		try:
			cursor.execute("""update uou_alarmi_userdb set cicweb = 0 where userid=%s""" % str(user_id))
			conn.commit()
			msg = 'cicweb 공지사항 알림을 해제합니다.'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	else:
		try:
			cursor.execute("""update uou_alarmi_userdb set cicweb = 1 where userid=%s""" % str(user_id))
			conn.commit()
			msg = 'UOU알라미가 최신 cicweb 공지사항 내용을 알려줍니다.'
		
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)

	conn.close()
	bot.sendMessage(chat_id=user_id, text=msg)

updater = Updater(token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)
help_handler = CommandHandler('help', help)
arbeit_handler = CommandHandler('arbeit', arbeit)
room_handler = CommandHandler('room',room)
barter_handler = CommandHandler('sale',barter)
cicweb_handler = CommandHandler('cic',cicweb)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(arbeit_handler)
dispatcher.add_handler(room_handler)
dispatcher.add_handler(barter_handler)
dispatcher.add_handler(cicweb_handler)


updater.start_polling()
