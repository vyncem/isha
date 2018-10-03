FROM python:2.7.15

ENV APP_HOME=/usr/src/app

RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

COPY ./requirements.txt $APP_HOME/

RUN pip install -r ./requirements.txt

COPY . $APP_HOME/

ENV DATA=/data

RUN mkdir -p $DATA

# CMD ["./eventbrite.py"]
# CMD ["./mailchimp.py"]
CMD ["./update_isha_list.py"]
