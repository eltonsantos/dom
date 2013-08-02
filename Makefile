clean:
		@find . -name "*.pyc" -delete

deps:
		@pip install -r requirements.txt

settings:
	cp dom/local_settings.sample.py dom/local_settings.py

setup: deps settings
		@python manage.py syncdb
		@python manage.py migrate
		@git remote add heroku git@heroku.com:projetodom.git

run:
		@python manage.py runserver 0.0.0.0:8000

remote_migrate:
		@heroku run python manage.py syncdb --noinput
		@heroku run python manage.py migrate

collectstatic:
		@heroku run python manage.py collectstatic --noinput

heroku:
		@git push heroku master

deploy: heroku remote_migrate collectstatic

flake8:
		@flake8 . --exclude='.*migrations,.*manage.py' --ignore=E124,E128

help:
		grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
