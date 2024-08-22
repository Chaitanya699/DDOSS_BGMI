from . import bot

def start_attack_reply(message, target, port, time):
    markup = types.InlineKeyboardMarkup()
    stop_button = types.InlineKeyboardButton("Stop Attack", callback_data="stop_attack")
    markup.add(stop_button)
    bot.send_message(message.chat.id, f"Attack started on {target}:{port} for {time} seconds.", reply_markup=markup)
