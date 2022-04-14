# wpa-django

This is a Django (python) container hosting the FREE web framework from WPA. 


## Install procedure

Just clone this repo in the directory of your choice (e.g. /opt):

```bash
cd /opt
git clone https://github.com/bgeneto/wpa-django.git
cd wpa-django
docker compose up -d 
# docker-compose up -d 
```

## Configure

Add a `.env` file inside the `config` folder containing, for example, the following:

```
FREE_PRODUCTION=on
FREE_SECRET=!r2341+@cs%euw2l6l)+2ots47t++dr48!+)!i^0dtg4y28u123
FREE_ALLOWED_HOSTS=192.168.98.190,your.long.url.com

FREE_FENIX_OAUTH=off
SOCIAL_AUTH_FENIX_AUTH_KEY=
SOCIAL_AUTH_FENIX_AUTH_SECRET=

FREE_GOOGLE_OAUTH=off
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=
```

Or simply rename the provided `.env.init` file.
Add an initial database file by renaming the `db.sqlite3.init` file to `db.sqlite3`. 
