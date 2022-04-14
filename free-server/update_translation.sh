#!/bin/bash
python3 ./manage.py compilemessages
python3 ./manage.py makemessages -d djangojs -a
python3 ./manage.py makemessages -a
#git commit -am "translation update"
