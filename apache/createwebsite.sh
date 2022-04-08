#!/bin/bash
#
# shell script to init site - run as root
#
# 1. make website folder
# 2. clone project

# create virtual env

# enshure server environment

mkdir -p /var/www/traindb/site

sudo apt install libapache2-mod-wsgi-py3
sudo apt-get install python3-venv

sudo chown peter:www-data .
chmod ug+w .

mkdir site
sudo mkdir /var/log/apache2/danbots


echo remove old env
rm -rf env

echo install new env
python3 -m venv env
. env/bin/activate
pip install --upgrade pip

echo install requiremetns
pip install -r requirements_prod.txt

echo prepare sqlite db
touch db.sqlite3
chmod ug+w db.sqlite3
sudo chown www-data:peter db.sqlite3

echo init database
python manage.py makemigrations
python manage.py migrate

echo load demo data
python manage.py loaddata demo

echo collect static files
python manage.py collectstatic

mkdir data
sudo chown www-data data

sudo systemctl restart apache2
