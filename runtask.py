from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from taskmain import taskmain as job
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', hour=7)
scheduler.add_job(job, 'cron', hour=8)
scheduler.add_job(job, 'cron', hour=9)
scheduler.add_job(job, 'cron', hour=13)
scheduler.add_job(job, 'cron', hour=14)
scheduler.add_job(job, 'cron', hour=15)
scheduler.add_job(job, 'cron', hour=19)
scheduler.add_job(job, 'cron', hour=20)
scheduler.add_job(job, 'cron', hour=21)
scheduler.start()