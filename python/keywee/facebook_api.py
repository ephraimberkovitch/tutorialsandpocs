import json
import requests

posts = []
access_token = "EAACEdEose0cBABFk8aurX9hWWsZCGoqs0AWtsVhHES8IbG7isdvKZBDzbZA4B6IkCL1DfvQty3Xk2xlBhYZAGQBpaLo7ZBaZCHoLB4clrZCpZAEZA5EczVJZCSSA751gZBkusM06veAG77ZCpSQnUFtDSCOBZAyi6viAZCf8LRZCZC21E6vVcjIZAp7QGech8"
next_url = 'https://graph.facebook.com/v2.9/nytimes/feed?access_token=%s&fields=id,name' % access_token
while len(posts)<1000:
    res = requests.get(next_url)
    page = res.json()
    data = page['data']
    posts += data
    next_url = page['paging']['next']

f = open('c:\\temp\\keywee.json', 'w')
f.write(json.dumps(posts[0:1000]))
f.close()
