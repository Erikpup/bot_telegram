import bs4
import telebot
import confing 
import requests
bot = telebot.TeleBot(confing.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, Я бот, который может говорить погоду.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if 'прив' in str(message.text).lower():
        bot.reply_to(message, "Привет, я пишу тебе из облака. Спроси про погоду.")
    elif 'погод' in str(message.text).lower():
        url = requests.get('https://www.gismeteo.ru/weather-krasnodar-5136/10-days/', headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
})
        info = bs4.BeautifulSoup(url.text, "html.parser")
        date = info.find(class_='widget-row widget-row-days-date')
        date = date.find_all('a')
        state = info.find_all(class_='weather-icon tooltip')
        text = ''
        temperature_max = info.find_all(class_='maxt')
        temperature_min = info.find_all(class_='mint')
        for i in range(10):
            date_i = date[i].find(class_='day').text
            if len(date[i].find(class_='date').text.split(' ')[0])==1:
                date_i_1 = date[i].find(class_='date').text.split(' ')[0]+' '
            else:
                date_i_1 = date[i].find(class_='date').text.split(' ')[0]
            state_i = state[i]['data-text']
            temperature_max_i=temperature_max[i].find(class_='unit unit_temperature_c').text
            temperature_min_i=temperature_min[i].find(class_='unit unit_temperature_c').text
            text += f"{date_i}" \
                    f" {date_i_1}  \n" \
                    f"От:{temperature_max_i} " \
                    f"До:{temperature_min_i}\n" \
                    f"{state_i}\n\n"
        bot.reply_to(message, f"{text}")
    else:
        bot.reply_to(message, f"Создатель меня еще не научил отвечать на '{message.text}'")
        
if __name__ == '__main__':
    bot.infinity_polling()
