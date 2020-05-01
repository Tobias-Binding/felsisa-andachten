# https://www.codementor.io/@garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay

bot_token = '928443335:AAH8VvwhChNjUGsUowILZsWN_hBfOrtRo_M'
chat_id = '417547423'

get_updates = 'https://api.telegram.org/bot{}/getUpdates'.format(bot_token)

text = 'Test Reply'
send_message = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(bot_token, chat_id, text)