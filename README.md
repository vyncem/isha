# isha-offering-sessions

Automation of the management of Free offering session management. Motivated by:

1. GDPRS
  1. phasing out of guest cards
1. Scaling up of free offering sessions ~10 per month


## Procedure
1. Guests register on Eventbrite
1. Guests marked as attended or missed on Eventbrite after session
1. Thank you emails sent to attendees
1. Missed you emails sent to missed
1. Stats of numbers and locations sent to Isha

## Considerations
1. Localisation and Internationalisation of emails
1. Configurability of automation, e.g.
  1. Turn specific session email sending off
  1. Specify time of emailing

## Dev

## Dockerization
### playground
`docker run -it --rm -v $(pwd):/usr/src/app python:2.7 bash`

### production
`docker build -t eb .`

`docker run -it --rm -e EVENTBRITE_TOKEN=$EVENTBRITE_TOKEN -v $DATA:/data eb`

### Env
1. [pyenv](https://github.com/pyenv/pyenv) and `.python-version` used to track python version.
2. `pip install -r requirements.txt` to install required packages.

### Test
- To run tests type `behave` in the root directory
- BDD using [Behave](https://github.com/behave/behave)
- Simplify and seed up http request using [VCR](https://github.com/kevin1024/vcrpy)
