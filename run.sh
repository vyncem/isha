# /usr/bin/env bash

docker build -t eb .

docker run -it --rm -e EVENTBRITE_TOKEN=$EVENTBRITE_TOKEN \
                    -e MAILCHIMP_TOKEN=$MAILCHIMP_TOKEN \
                    -e MAILCHIMP_LIST_ID=$MAILCHIMP_LIST_ID \
                    -e EVENTBRITE_START=$EVENTBRITE_START \
                    -e EVENTBRITE_END=$EVENTBRITE_END \
                    -e EVENTBRITE_ORG_ID=$EVENTBRITE_ORG_ID \
                    -v $DATA:/data \
                    eb
