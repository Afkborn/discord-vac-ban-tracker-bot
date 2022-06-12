from datetime import datetime, timedelta
from time import time
def get_time():
    return datetime.now().strftime("%H:%M %d.%m.%Y")

def get_time_command():
    return datetime.now().strftime("%H:%M:%S.%f")

def get_time_from_unix(unix_time : str):

    return datetime.fromtimestamp(unix_time).strftime("%d/%m/%Y %H:%M:%S")

def get_relevant_last_online_date(lastOnlineDate : int):
    sonOnlineTarihi = time() - lastOnlineDate
    dt = timedelta(seconds=sonOnlineTarihi)
    fullText = ""
    if (dt.days != 0):
        fullText += str(dt.days) + " days "
    if (dt.seconds != 0):
        hour = dt.seconds // 3600
        minute = (dt.seconds % 3600) // 60
        second = dt.seconds % 60
        fullText += f"{hour} hour, {minute} minute, {second} second"
    return fullText

def get_relevant_time_created(time_created:int):
    uyeOlmaTarihi = time()  - time_created
    dt = timedelta(seconds=uyeOlmaTarihi)
    years = 0
    if (dt.days > 365):
        years += dt.days // 365
    if years == 0:
        return dt.days, "day(s)"
    return years, "year(s)"
    
    
