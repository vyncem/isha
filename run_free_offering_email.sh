# /usr/bin/env bash

export FREE_OFFERING_WORKSPACE=~/free-offering
python3.6 ${FREE_OFFERING_WORKSPACE}/update_isha_list.pyc
grep -e 'INFO Event:' -e '------' ${FREE_OFFERING_WORKSPACE}/events.log | grep `date +'%F'` > ${FREE_OFFERING_WORKSPACE}/.email
