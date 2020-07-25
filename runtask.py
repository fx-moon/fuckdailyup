from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from taskmain import taskmain as job
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', hour=7)
scheduler.add_job(job, 'cron', hour=13)
scheduler.add_job(job, 'cron', hour=19)
scheduler.start()