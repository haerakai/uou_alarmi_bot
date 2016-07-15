# -*- encoding:utf-8 -*-

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import MySQLdb.cursors
token = '222290220:AAHE2Hpa5SQDFkaWximJB9FY5Y3dNxW8C0M'


def broad():
	try:
		conn = MySQLdb.connect(user='molkoo', passwd='7qmffor', db='uou_alarmi', host='localhost', charset='utf8', use_unicode='True')
		cursor = conn.cursor()
		cursor.execute("select arbeit, room, barter from uou_alarmi_last")
		last = cursor.fetchone()

		cursor.execute("select userid from uou_alarmi_userdb")
		user = cursor.fetchall()
		
		cursor.execute("select * from uou_alarmi_arbeit where num>%s" % last[0])
		arbeit_data = cursor.fetchall()
		
		cursor.execute("select * from uou_alarmi_room where num>%s" % last[1])
		room_data = cursor.fetchall()

		cursor.execute("select * from uou_alarmi_barter where num>%s" % last[2])
		barter_data = cursor.fetchall()
	
		#cursor.execute("update uou_alarmi_last set arbeit=%s, room=%s, barter=%s",(arbeit_data[0][5], room_data[0][6], barter_data[0][5]))
		#conn.commit()
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit(1)

	
	for i in user:
		for data in arbeit_data:
			msg = '등록일 : ' + data[1].encode('utf-8') + '\n' + '회사명 : ' + data[2].encode('utf-8') + '\n' + '업무내용 : ' + data[3].encode('utf-8') + '\n' + '바로가기 : ' + data[4].encode('utf-8')
			updater.bot.sendMessage(chat_id=i[0].encode('utf-8'), text=msg)
		for data in room_data:
			msg = '등록일 : ' + data[1].encode('utf-8') + '\n' + '위치 : ' + data[2].encode('utf-8') + '\n' + '제목 : ' + data[3].encode('utf-8') + '\n' + '가격대(만원) : ' + data[4].encode('utf-8') + '\n' + '바로가기 : ' + data[5].encode('utf-8')
			updater.bot.sendMessage(chat_id=i[0].encode('utf-8'), text=msg)
		for data in barter_data:
			msg = '등록일 : ' + data[1].encode('utf-8') + '\n' + '제목 : ' + data[2].encode('utf-8') + '\n' + '글쓴이 : ' + data[3].encode('utf-8') + '\n' + '바로가기 : ' + data[4].encode('utf-8')
			updater.bot.sendMessage(chat_id=i[0].encode('utf-8'), text=msg)
updater = Updater(token)

broad()

os._exit(0)
