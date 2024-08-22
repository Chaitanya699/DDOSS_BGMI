import logging

logging.basicConfig(level=logging.INFO)

def log_command(user_id, command):
    logging.info(f"User {user_id} issued command: {command}")
