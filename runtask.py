from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from taskmain import taskmain as job
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', hour=14)
scheduler.add_job(job, 'cron', hour=15)
scheduler.start()