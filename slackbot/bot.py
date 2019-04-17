from slacker import Slacker
from slackbot import settings

def sendMessage() : 
    slack = Slacker(settings.API_TOKEN)
    message = "Hello, Slack!!"
    slack.chat.post_message(settings.CHANNELS['general'], message)