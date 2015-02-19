Crosspost
=========

A Python/Flask web applicationt that posts to both Facebook and Twitter (via email to IFTTT). Authentication is done via LDAP (so you'll need access to an LDAP server).

Usage
=====

Requirements
------------

* flask (0.10)
* flask-login
* python-ldap

Configuration
-------------

You'll need to create a file called `config.py` containing authentication information for your email account (if using two-factor authentication via Gmail, remember to use an application-specific password). It should also include LDAP server information and the LDAP ID of the user who is permitted to use this application (in case you're using a shared LDAP server). It should look something like this:

```python
from os import urandom

USERNAME = 'you@gmail.com'
PASSWORD = 'your very long and presumably sensible password'
SMTPHOST = 'smtp.gmail.com:587'

LDAP_USER = 'your.user.id'
LDAP_URI = 'ldap://your.ldap.server'
LDAP_SEARCH_BASE = 'ou=something,dc=something,dc=ca'    # Consult LDAP admin.

CSRF_ENABLED = True
SECRET_KEY = urandom(30)
PROPAGATE_EXCEPTIONS = True
```

Before using, you'll also need to create an IFTTT account and set up email rules to handle posting to Twitter (using hashtag #twitter), Facebook (using hashtag #facebook), and Facebook links (using hashtag #fblink). This is fairly straightforward.

Starting the Server
-------------------

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To make the server world-accessible or for other options, see `run.py -h`.

Bugs and Feature Requests
=========================

Feature Requests
----------------

None

Known Bugs
----------

None

License Information
===================

Written by Gem Newman. [GitHub](https://github.com/spurll/) | [Blog](http://www.startleddisbelief.com) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).
