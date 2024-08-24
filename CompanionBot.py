import telebot
import time
from random import randrange
print("Im companion and game bot in telegram!")
print("This is not ai!")
print("Support only russian messages")
token = input("Enter token:")
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, 'Привет друг!')
    elif message.text == "Как дела?":
        sleep(5)
        bot.send_message(message.chat.id, 'Вроде ок.')
        
    elif message.text == "Привет!":
        sleep(5)
        bot.send_message(message.chat.id, 'Привет друг!.')
        
    elif message.text == "Рандомное число":
    	bot.send_message(message.chat.id, f'Рандомное число от 1 до 100:' +str(randrange(1,100)))
    	
    elif message.text == "Брось кубик":
    	bot.send_message(message.chat.id, "Бросаю кубик...")
    	value = bot.send_dice(message.chat.id, emoji='🎲').dice.value
    	time.sleep(1)
    	bot.send_message(message.chat.id, f'Вам выпало {value}!')

    elif message.text == "Что делаешь?":
        sleep(2)
        bot.send_message(message.chat.id, 'С тобой говорю.')
    elif message.text == "Бот":
      	bot.send_message(message.chat.id, 'Да да я тут')
    elif message.text == "Пинг":
     	bot.send_message(message.chat.id, 'Понг')
    elif message.text == "Мой id":
     	bot.send_message(message.chat.id, f'Твой telegram id:' +str(message.from_user.id))
    elif message.text == "/start":
     	bot.send_message(message.chat.id, "Привет я очень крутой бот!")
    elif message.text == "Бот твои комманды":
    	bot.send_message(message.chat.id, "Ты можешь написать Пинг или Бот а ещё Мой id или например Рандомное число а так же Брось кубик тоже весело и конечно же Бот твои комманды ну или просто можешь пообщаться со мной:)")
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял.')
bot.polling(none_stop=True, interval=0)