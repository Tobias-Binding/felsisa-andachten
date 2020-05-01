import requests

bot_token = '928443335:AAH8VvwhChNjUGsUowILZsWN_hBfOrtRo_M'
bot_chatID = '417547423'

def telegram_bot_sendtext(bot_message, bot_token, bot_chatID):
    baseurl = 'https://api.telegram.org/bot'
    send_text = '{}{}/sendMessage?chat_id={}&parse_mode=Markdown&text={}'.format(baseurl, bot_token, bot_chatID, bot_message)
    response = requests.get(send_text)
    return response.json()

# Test the send text function
#test = telegram_bot_sendtext("Reformatted message 2", bot_token, bot_chatID)
#print(test)

def sendImage(bot_token, bot_chatID, image):
    url = "https://api.telegram.org/bot{}/sendPhoto".format(bot_token)
    files = {'photo': open(image, 'rb')}
    data = {'chat_id' : bot_chatID}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)

image = r'C:\repos\Image Recognition\Sample_image.jpg'

sendImage(bot_token, bot_chatID, image)

# Done! Congratulations on your new bot. You will find it at t.me/Bindingsaibot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 928443335:AAH8VvwhChNjUGsUowILZsWN_hBfOrtRo_M
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

# https://api.telegram.org/bot928443335:AAH8VvwhChNjUGsUowILZsWN_hBfOrtRo_M/getUpdates

# https://api.telegram.org/bot928443335:AAH8VvwhChNjUGsUowILZsWN_hBfOrtRo_M/getUpdates
# https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e