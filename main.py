import telebot
import telegram
from telebot import types


bot = telebot.TeleBot('TOKEN')


print('[~] Бот успешно запущен | Версия: 1.0.0')


@bot.message_handler(commands=['start'])
def start_menu(message):
    chat_id = message.chat.id
    bot.send_message(message.chat.id, "Для смены разрешений напишите /change_permissions")


@bot.message_handler(commands=['change_permissions'])
def info(message):
    msg = bot.send_message(message.chat.id, "Введите значения разрешений\n (can_send_messages,\n can_send_media_messages,\n can_send_polls,\n can_send_other_messages,\n can_add_web_page_previews,\n can_change_info,\n can_invite_users,\n can_pin_messages)\nПример: 0:0:0:0:0:0:0:0")
    bot.register_next_step_handler(msg, change_permissions)


def change_permissions(message):
    if message.content_type == 'text':
        value = message.text
        value = value.split(":")
        a = telegram.ChatPermissions()
        a.can_send_messages = bool(int(value[0]))
        a.can_send_media_messages = bool(int(value[0]))
        a.can_send_polls = bool(int(value[0]))
        a.can_send_other_messages = bool(int(value[0]))
        a.can_add_web_page_previews = bool(int(value[0]))
        a.can_change_info = bool(int(value[0]))
        a.can_invite_users = bool(int(value[0]))
        a.can_pin_messages = bool(int(value[0]))
        bot.set_chat_permissions(message.chat.id, permissions=a)
        bot.send_message(message.chat.id, "✅Выполено")
    else:
        bot.reply_to(message, '❌Данные введены неверно')


if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True)
