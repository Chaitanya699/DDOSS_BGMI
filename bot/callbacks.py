from . import bot

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "stop_attack":
        bot.answer_callback_query(call.id, "Attack stopped.")
