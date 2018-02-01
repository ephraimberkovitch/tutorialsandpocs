https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

# Part 1
## git init
## python3 -m venv env
## source env/bin/activate
## heroku login
## Procfile
### web: gunicorn app:app
## runtime.txt
### python-3.6.4
## heroku create berko-wordcount-pro
## heroku create berko-wordcount-stage
## git remote add pro git@heroku.com:YOUR_APP_NAME.git
## git remote add stage git@heroku.com:YOUR_APP_NAME.git
## git push stage master
## git push pro master
## autoenv
## heroku config:set APP_SETTINGS=config.StagingConfig --remote stage
## heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro
## heroku run python app.py --app berko-wordcount-stage
## heroku run python app.py --app berko-wordcount-pro

# Part 2
