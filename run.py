from apscheduler.schedulers.blocking import BlockingScheduler
from slackbot import bot

scheduler = BlockingScheduler()

# 5초 interval로 slack에 메세지를 보내는 scheculer job 생성
scheduler.add_job(bot.sendMessage, 'interval', seconds=5)

# 스케줄러 start
scheduler.start()