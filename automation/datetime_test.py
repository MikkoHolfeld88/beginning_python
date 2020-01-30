import datetime, time

while True:
    jetzt = datetime.datetime.now()
    print(jetzt.hour, jetzt.minute, jetzt.second)
    time.sleep(1)
