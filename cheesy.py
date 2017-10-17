#!/usr/bin/python
import telebot
import random
from pickupLine import getPickupLine
from jokes import getJoke
from comic import getComic
from dirty import getDirtyLine

bot = telebot.TeleBot("332198864:AAEH01RJoUuXH6VhJKK-rBcxbgBNWLUK1jw")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	cid = message.chat.id
	bot.send_message(cid, "Commands : \n /joke \n /comic \n /cheesy \n /dirty \n")

@bot.message_handler(commands=['joke'])
def send_joke(message):
	cid = message.chat.id
        joke = getJoke()
        bot.send_message(cid, joke)

@bot.message_handler(commands=['comic'])
def send_comic(message):
	cid = message.chat.id
	getComic()
	img = open('img.png', 'rb')
	bot.send_photo(cid, img)

@bot.message_handler(commands=['cheesy'])
def send_cheesy(message):
	cid = message.chat.id
	pickupLine = getPickupLine()
	bot.send_message(cid, pickupLine)

@bot.message_handler(commands=['dirty'])
def send_dirty(message):
	cid = message.chat.id
	dirtyLine = getDirtyLine()
	bot.send_message(cid, dirtyLine)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	cid = message.chat.id
	print cid
	bot.send_message(cid, "Try /help")

bot.polling()

