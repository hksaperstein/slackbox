import slack
import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask
from slackeventsapi import SlackEventAdapter

# def main():
# Env var config
env_path = os.path.dirname(os.path.abspath(__file__)) +'/.env'
load_dotenv(dotenv_path=env_path)

# Webserver initiation
app = Flask(__name__)

# Slack initiation
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call('auth.test')['user_id']
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'],'/slack/events', app)


@slack_event_adapter.on('message')
def message(payload):
    print("here")

    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    if not BOT_ID == user_id:
        client.chat_postMessage(channel=channel_id, text=text)

    # Start Webserver


if __name__ == "__main__":
    # main()
    app.run(debug=True)
