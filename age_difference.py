from datetime import datetime

def age(boy_birthday, girl_bithday):
    start = datetime.strptime(boy_birthday, "%d-%m-%Y")
    end =   datetime.strptime(girl_bithday, "%d-%m-%Y")
    diff = start.date() - end.date()
    return int(diff.days)