#
# install website and environment
#
ENV_PATH=/var/www/env/django

default:
	@echo "make install\tinstall sw and set default config"
	@echo "make update\tUpdate from Github"
	@echo "make apache\tInstall in apache"
	@echo "make help\tDisplay alternative options"

.PHONY: apache
apache:
	@echo Installing apache files
	@ln -s $(CURDIR)/apache/traindb.conf /etc/apache2/sites-available/traindb.conf
	@a2ensite traindb.conf
	@systemctl reload apache2

python3:
	@echo install Python binaries
	apt install python3-venv

environment:
	@echo "Make Python environment"
	@echo Env $(ENV_PATH)
	@mkdir -p $(ENV_PATH)
	@python3 -m venv $(ENV_PATH)

requirements:
	. $(ENV_PATH)/bin/activate ; pip install -r requirements.txt

db:
	@echo "Prepare DB"
	@chown www-data:danbots db.sqlite3

django:
	. $(ENV_PATH)/bin/activate; python manage.py collectstatic;	python manage.py migrate

permissions:
	chown www-data:danbots . db.sqlite3 static
	
install:	apache
	@echo "Install TrainingDB website"

test:
	@echo Testing

