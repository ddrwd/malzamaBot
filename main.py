from telebot import TeleBot
from telebot.types import BotCommand


bot =TeleBot('5733456744:AAFlMB3RDLR3ys44sQna7sSXpBZVnmUzuIk')



@bot.message_handler(["start"])
def welcome(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.send_message (chat_id=chat_id,text=f" {first_name} بەخێربەی \n\n ئەم بۆتە تەنها بەشێوەیەکی تاقیکاری دروست کراوە تکایە لە کەم و کوری ببورن \nCreated by DRUD" )


@bot.message_handler(["programming"])
def programming(message):
    chat_id = message.chat.id
    bot.send_message (chat_id,text=f" Practical lec 1\n https://www.mediafire.com/file/iz159um4nek7f0j/Practical_lec_1.pdf/file\nT1-lecture-1\nhttps://www.mediafire.com/file/40z7tybxret98dz/T1-lecture-1.ppt/file\n T2-lecture-2\nhttps://www.mediafire.com/file/eutxwzvf26uanga/T2-lecture-2.pptx/file\nT3-lecture-3\nhttps://www.mediafire.com/file/8625pixdg7sqvqe/T3-lecture-3.ppt/file\nT4-lecture-4\nhttps://www.mediafire.com/file/ncu0h4jfnfp39ot/T4-lecture-4.ppt/file" )
    
    
print("bot is runing...")    
bot.infinity_polling()