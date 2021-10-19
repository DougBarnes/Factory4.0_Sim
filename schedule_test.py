"""
Demonstrates how to schedule a job to be run in a process pool on 3 second intervals.
"""

from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler

choice = ''

def firsttick():
    print('First Tick!: %s' % datetime.now())

def secondtick():
    print('Second Tick!: %s' % datetime.now())

def thirdtick():
    print('Third Tick!: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_executor('processpool')
    scheduler.add_job(firsttick, 'interval', seconds=3)
    scheduler.add_job(secondtick, 'interval', seconds=3)
    scheduler.add_job(thirdtick, 'interval', seconds=3)

    scheduler.start()

    
'''
    while choice != 'q':
        choice = input("Waiting for input: ")

        if choice == '1':
            print("scheduler start...")
            scheduler.start()

        elif choice == 'q':
            print("Exiting...")
'''
'''
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
'''