import datetime

bgmi_cooldown = {}

def check_cooldown(user_id):
    if user_id in bgmi_cooldown:
        time_since_last = (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds
        return time_since_last < 10
    bgmi_cooldown[user_id] = datetime.datetime.now()
    return False
