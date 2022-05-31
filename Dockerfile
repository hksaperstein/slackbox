FROM alpine

# Copy src app TODO Not sure how this is gonna work at work
RUN mkdir -p /home/app
COPY ./src /home/app

# Allow Bash commands
RUN apk add --no-cache --upgrade bash

# Setup Python Venv
RUN apk add python3 
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN source $VIRTUAL_ENV/bin/activate
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r /home/app/requirements.txt



CMD ["python3", "/home/app/slackbot.py"]