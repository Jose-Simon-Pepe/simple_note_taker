import os
from crontab import CronTab

opts = [10,30,50]
my_cron = CronTab(user=os.getenv('USER'))
task = my_cron.new(command="")


def show_opts(opts:list):
    print("Choose backup frequency")
    it:int = 0
    for opt in opts:
        print(str(it) +": "+ str(opt))
        it+=1

def select_opt(opts:list):
    freq = int(input("What frequency do you want the backup to be updated? (30 mins)"))
    if freq<0 or freq>2 :
        print("Bad value, using default (30)")
        freq = opts[1]
    else:
        freq = str(opts[freq])
    
    print("Crontab will be setted with: "+freq)
    task.minute.every(freq)

show_opts(opts)
select_opt(opts)
