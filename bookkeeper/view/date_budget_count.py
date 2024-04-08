import datetime



def date_dif(date1, date2):
    dt1=datetime.datetime(year=int(date1.split(" ")[0].split("-")[0]),
                          month=int(date1.split(" ")[0].split("-")[1]),
                          day=int(date1.split(" ")[0].split("-")[2]),
                          hour=int(date1.split(" ")[1].split(":")[0]),
                          minute=int(date1.split(" ")[1].split(":")[1]),
                          second=int(date1.split(" ")[1].split(":")[2]))
    dt2=datetime.datetime(year=int(date2.split(" ")[0].split("-")[0]),
                          month=int(date2.split(" ")[0].split("-")[1]),
                          day=int(date2.split(" ")[0].split("-")[2]),
                          hour=int(date2.split(" ")[1].split(":")[0]),
                          minute=int(date2.split(" ")[1].split(":")[1]),
                          second=int(date2.split(" ")[1].split(":")[2]))
    return dt1-dt2

def date_dif_now(date1):
    dt1=datetime.datetime(year=int(date1.split(" ")[0].split("-")[0]),
                          month=int(date1.split(" ")[0].split("-")[1]),
                          day=int(date1.split(" ")[0].split("-")[2]),
                          hour=int(date1.split(" ")[1].split(":")[0]),
                          minute=int(date1.split(" ")[1].split(":")[1]),
                          second=int(date1.split(" ")[1].split(":")[2]))
    delta=datetime.datetime.now()-dt1
    flag=[False, False, False]
    if delta<datetime.timedelta(weeks=0, days=1, hours=0,
                         minutes=0, seconds=0):flag[0]=True
    if delta<datetime.timedelta(weeks=0, days=7, hours=0,
                         minutes=0, seconds=0):flag[1]=True
    if delta<datetime.timedelta(weeks=0, days=30, hours=0,
                         minutes=0, seconds=0):flag[2]=True
    return flag
