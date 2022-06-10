from datetime import datetime

def get_time():
    return datetime.now().strftime("%H:%M %d.%m.%Y")

def get_time_command():
    return datetime.now().strftime("%H:%M:%S.%f")

def get_time_from_unix(unix_time : str):

    return datetime.fromtimestamp(unix_time).strftime("%d/%m/%Y %H:%M:%S")