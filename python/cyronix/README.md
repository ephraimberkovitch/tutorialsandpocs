# Cyronix Test
## Exercise 1
The task is to extract and save data from an accessible cloud account (Gmail, Google Drive),
assuming we have a standard logged on user (our own google cookie or API token).

- a description of the research steps you took.
- a description of the different security measures you observed.
- a description of the possible ways to bypass or get around those security measures.
- a description of google’s behaviour - how exactly can you get the relevant information? how is the data extracted using automatic methods different than data accessible with a standard interactive method?
- blockage from the service can be irreversible - you have to stay undetected

0) pay an attention, that we have google cookie or API token,
and not user name + password (plain credentials). This forces us research in certain direction
1) how can we impersonate a user? this is not necessary for this specific exercise,
but we have try at least to figure out the main steps for getting credentials - phishing, etc.
2) where and how do we store data? RDBMS, No-SQL? Where do we store assets? AWS S3?
3) scalability of this service - not required here, but has to be figured out at least in main steps
4) where the code is running?
5) is it scheduled to run every X minutes? or running in an infinite loop?
6) does it create an instance / process / thread for each user, we are scraping his data?
7) what are we interested to extract:
    1) emails
    2) contacts
    3) calendar
    4) Google drive items
    5) tasks
    6) passwords to external services - FB, Twitter, etc.?
8) does google recognise and block rate limiting?
9) how often the security token is refreshed
10) is getting client api key for our app with google dangerous, and we should try bypass it?

### Setup virtual environment
1. python3.7 -m pipenv install requests --python 3.7
2. pipenv install