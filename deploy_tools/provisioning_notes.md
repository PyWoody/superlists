Provisioning a new site
========================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:
	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv
	
## Nginx Virtual Host Config

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
	/home/username
	|_____sites
		  |____SITENAME
				|___ database
				|___ source
				|___ static
				|___ virtualenv