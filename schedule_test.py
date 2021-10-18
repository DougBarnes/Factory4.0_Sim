#https://www.youtube.com/watch?v=zF_DroDICaM
import schedule
import time

def job():
    print("Reading time ...")

def coding():
    print("Coding time ...")

def playing():
    print("Playing time ...")

#time
schedule.every(5).seconds.do(job)
schedule.every(10).seconds.do(coding)
schedule.every().day.at("11:39").do(playing)

while True:
    schedule.run_pending()
    time.sleep(1)