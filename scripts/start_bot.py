import subprocess
import time
import logging

def start_bot():
    subprocess.Popen(['python', '-m', 'bot.commands'])

def restart_bot():
    while True:
        start_bot()
        time.sleep(10)

if __name__ == "__main__":
    logging.info("Starting bot...")
    restart_bot()
