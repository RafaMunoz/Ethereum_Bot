#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import telebot
import requests
from telebot import types


# -------------------- SETTINGS --------------------
# Your Ethereum wallet.
wallet = "0x947edcaa3c9b63e3ccf2d5e148bf62674f519f34"

# Telegram bot Token.
token = "378572660:AAHaLn4NylzJuv4kl4XusEtG3LeDqafjA75"

# List with the telegram id of the allowed users.
id_admins = [15288736, 16278436]

# Your Pool. 0 = Ethermine | 1 = Ethpool
pool = 0
# --------------------------------------------------




list_pools = ["https://api.ethermine.org", "http://api.ethpool.org"]
web = ["https://ethermine.org", "https://eth.nanopool.org"]

# View the wallet data on Ethermine.
def ethermine(id_user):
    url = list_pools[pool] + "/miner/" + wallet + "/currentStats"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            response_json = response.json()
            hash_rate = round(float(response_json["data"]["reportedHashrate"]) / (10 ** 6), 2)
            active_workers = response_json["data"]["activeWorkers"]
            unpaid = round(float(response_json["data"]["unpaid"]) / (10 ** 18), 5)

            prices = cryptocompare(id_user, 1)

            generate_euro = round(float(prices[0]) * unpaid, 2)
            generate_dolar = round(float(prices[1]) * unpaid, 2)
            generate = "*Generate:* ``` " + u"\u20AC " + str(generate_euro) + " = " + u"\u0024 " + str(
                generate_dolar) + "```"

            text_send = "*Hashrates:* ``` " + str(
                hash_rate) + " MH/s```\n" + "*Active Workers:* ```" + str(
                active_workers) + "```\n" + "*Unpaid:* ``` " + str(unpaid) + " ETH```\n" + generate
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

        except:
            text_send = u"\u26A0 The wallet does not exist on " + web[pool]
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")


# Consult current price of Ethereum.
def cryptocompare(id_user, control):
    url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD,EUR"
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        price_euro = response_json["DISPLAY"]["ETH"]["EUR"]["PRICE"]
        change_euro = response_json["DISPLAY"]["ETH"]["EUR"]["CHANGEPCT24HOUR"]
        price_dolar = response_json["DISPLAY"]["ETH"]["USD"]["PRICE"]
        change_dolar = response_json["DISPLAY"]["ETH"]["USD"]["CHANGEPCT24HOUR"]

    if control == 0:
        if float(change_euro) > 0:
            emoji_euro = u"\U0001F53A"

        else:
            emoji_euro = u"\U0001F53B"

        if float(change_dolar) > 0:
            emoji_dolar = u"\U0001F53A"

        else:
            emoji_dolar = u"\U0001F53B"

        euro = "``` " + price_euro + "  " + emoji_euro + change_euro + "%\n```"
        dolar = "``` " + price_dolar + "  " + emoji_dolar + change_dolar + "%```"
        text_send = "*Ethereum - ETH*\n" + euro + dolar
        bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

    else:
        price_euro = float(price_euro.replace(u"\u20AC ", ""))
        price_dolar = float(price_dolar.replace(u"\u0024 ", ""))

        return [price_euro, price_dolar]


# We check if the user has permission.
def check_admin(id_user):
    check = id_user in id_admins
    return check


# Keyboard Telegram Bot
def keyboard(chat_id, textoEnvio):
    r1 = ["Mined", "Price"]
    keyboard = [r1]
    news_keyboard = {'keyboard': keyboard, 'resize_keyboard': True}
    bot.send_message(chat_id, textoEnvio, None, None, json.dumps(news_keyboard))


if __name__ == "__main__":
    bot = telebot.TeleBot(token)


    # Welcome message.
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        id_user = message.chat.id
        permitted = check_admin(id_user)

        if (permitted == True):
            name = message.chat.first_name
            text_send = "Welcome " + name + "!!"
            keyboard(id_user, text_send)


    # Other messages.
    @bot.message_handler()
    def main(message):

        id_user = message.chat.id
        permitted = check_admin(id_user)

        if (permitted == True):
            text = message.text

            # Mine button.
            if text == "Mined":
                ethermine(id_user)

            # Price button.
            if text == "Price":
                cryptocompare(id_user, 0)


    bot.polling(none_stop=True)
