# -*- encoding:utf-8 -*-

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import MySQLdb.cursors
token = 'insert token'

def send_arbeit():
        for data in arbeit_data:
                msg = '등록일 : ' + data[0].encode('utf-8') + '\n' + '회사명 : ' + data[1].encode('utf-8') + '\n' + '업무내용 : ' + data[2].encode('utf-8') + '\n' + '바로가기 : ' + data[3].encode('utf-8')
                for u in user:
			if u[1]==1:
                        	updater.bot.sendMessage(chat_id=u[0].encode('utf-8'), text=msg)

def send_room():
        for data in room_data:
                msg = '등록일 : ' + data[0].encode('utf-8') + '\n' + '위치 : ' + data[1].encode('utf-8') + '\n' + '제목 : ' + data[2].encode('utf-8') + '\n' + '가격대(만원) : ' + data[3].encode('utf-8') + '\n' + '바로가기 : ' + data[4].encode('utf-8')
                for u in user:
			if u[2]==1:
                        	updater.bot.sendMessage(chat_id=u[0].encode('utf-8'), text=msg)

def send_barter():
        for data in barter_data:
                msg = '등록일 : ' + data[0].encode('utf-8') + '\n' + '제목 : ' + data[1].encode('utf-8') + '\n' + '글쓴이 : ' + data[2].encode('utf-8') + '\n' + '바로가기 : ' + data[3].encode('utf-8')
                for u in user:
			if u[3]==1:
                        	updater.bot.sendMessage(chat_id=u[0].encode('utf-8'), text=msg)

def send_cicweb():
	for data in cicweb_data:
		msg = '등록일 : ' +  data[0].encode('utf-8') + '\n' + '제목: ' + data[1].encode('utf-8') + '\n' + '글쓴이 : ' + data[2].encode('utf-8') + '\n' + '바로가기 : ' + data[3].encode('utf-8')
		for u in user:
			if u[4]==1:
				updater.bot.sendMessage(chat_id=u[0].encode('utf-8'), text=msg)
def broad():
	try:
		conn = MySQLdb.connect(user='alarmi', passwd='alarmi', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
		cursor = conn.cursor()

		cursor.execute("select userid, arbeit, room, barter, cicweb from uou_alarmi_userdb")
		global user
		user = cursor.fetchall()
		
		cursor.execute("select * from uou_alarmi_arbeit")
		global arbeit_data
		arbeit_data = cursor.fetchall()
		
		cursor.execute("select * from uou_alarmi_room")
		global room_data
		room_data = cursor.fetchall()

		cursor.execute("select * from uou_alarmi_barter")
		global barter_data
		barter_data = cursor.fetchall()
		
		cursor.execute("select * from uou_alarmi_cicweb")
		global cicweb_data
		cicweb_data = cursor.fetchall()

	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)
	
	if arbeit_data != None:
		send_arbeit()

	if room_data != None:
		send_room()

	if barter_data != None:
		send_barter()
	
	if cicweb_data != None:
		send_cicweb()

updater = Updater(token)

broad()

os._exit(0)
