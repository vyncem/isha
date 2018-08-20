# /usr/bin/env bash

docker build -t eb .

docker run -it --rm -e EVENTBRITE_TOKEN=$EVENTBRITE_TOKEN -e MAILCHIMP_TOKEN=$MAILCHIMP_TOKEN -v $DATA:/data eb