# BLONGO

## Deploying to render.com

pip install django dj-database-url psycopg2-binary whitenoise gunicorn
pip freeze > requirements.txt

### ENV VARS
DATABASE_URL
SECRET_KEY
ALLOWED_HOSTS
DEBUG
PYTHON_VERSION

Build Command ./build.sh
Start Command gunicorn reiko.wsgi:application

## Git COMMANDS
git branch -M main
git remote add origin https://github.com/subham2023/blongo.git
git push -u origin main


## Deploying to gitpod.io
WORKSPACE https://subham2023-reiko-nzo2q2rk9ai.ws-us96.gitpod.io/
SITE https://8000-subham2023-reiko-nzo2q2rk9ai.ws-us96.gitpod.io/
