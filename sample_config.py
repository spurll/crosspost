from os import urandom

# Web Server
CSRF_ENABLED = True
SECRET_KEY = urandom(30)
PROPAGATE_EXCEPTIONS = True
REMEMBER_COOKIE_NAME = 'crosspost_token'    # Needs to be unique server-wide.

# LDAP
LDAP_URI = 'ldap://YOUR.LDAP.URI'
LDAP_SEARCH_BASE = 'ou=????,dc=????,dc=????'
LDAP_USER = 'YOUR.LDAP.USER.ID'

# Email
USERNAME = 'YOUR.EMAIL@gmail.com'
PASSWORD = 'YOUR LONG AND/OR APPLICATION-SPECIFIC PASSWORD'
SMTPHOST = 'smtp.gmail.com:587'
