CrossPost
=========

A Python/Flask web application that posts to both Facebook and Twitter (via email to IFTTT). Authentication is done via LDAP (so you'll need access to an LDAP server).

Usage
=====

Requirements
------------

* flask
* flask-login
* flask-wtf
* ldap3

Configuration
-------------

You'll need to create a file called `config.py` containing authentication information for your email account (if using two-factor authentication via Gmail, remember to use an application-specific password). It should also include LDAP server information and the LDAP ID of the user who is permitted to use this application (in case you're using a shared LDAP server). A sample configuration file can be found at `sample_config.py`.

Before using, you'll also need to create an IFTTT account and set up email rules to handle posting to Twitter (using hashtag #twitter), Facebook (using hashtag #facebook), and Facebook links (using hashtag #fblink). This is fairly straightforward.

Starting the Server
-------------------

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To make the server world-accessible or for other options, see `run.py -h`.

If you're having trouble configuring your sever, I wrote a <a href="http://blog.spurll.com/2015/02/configuring-flask-uwsgi-and-nginx.html">blog post</a> detailing explaining how to <a href="http://blog.spurll.com/2015/02/configuring-flask-uwsgi-and-nginx.html">get Flask, uWSGI, and Nginx working together</a>.

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

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

Remember: [GitHub is not my CV.](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/)
