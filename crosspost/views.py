from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
import re

from crosspost import app, lm
from crosspost.forms import LoginForm, InputForm
from crosspost.authenticate import authenticate, load_user_info
from crosspost.mailbox import Mailbox


RECIPIENTS = ['trigger@applet.ifttt.com']

# From http://www.regexguru.com/2008/11/detecting-urls-in-a-block-of-text/
LINK_PATTERN = (r'\b(?:(?:https?|ftp|file)://|www\.|ftp\.)(?:\([-A-Z0-9+&@#/%='
                r'~_|$?!:,.]*\)|[-A-Z0-9+&@#/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#/%'
                r'=~_|$?!:,.]*\)|[A-Z0-9+&@#/%=~_|$])')


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for("post"))


@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = InputForm()

    if form.is_submitted():
        print('Form submitted. Validating...')

        if form.validate_on_submit():
            print('Form validated. Posting...')
            post(form.text.data, fb=form.fb.data, twitter=form.twitter.data)
            return redirect(url_for('index'))

        else:
            flash_errors(form)

    return render_template('crosspost.html', title='CrossPost', user=g.user,
                           form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user == app.config['LDAP_USER']:
        return redirect(url_for('index'))

    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', title='Log In', form=form)

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        print('Logging in...')
        user = authenticate(username, password)

        if not user:
            print('Login failed.')
            flash('Login failed.')
            return render_template('login.html', title='Log In', form=form)
        elif user.id != app.config['LDAP_USER']:
            print('This user does not have appropriate permissions.')
            flash('This user does not have appropriate permissions.')
            return render_template('login.html', title='Log In', form=form)

        login_user(user, remember=form.remember.data)
        return redirect(request.args.get('next') or url_for('index'))

    return render_template('login.html', title="Log In", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@lm.user_loader
def load_user(id):
    return load_user_info(id)


@app.before_request
def before_request():
    g.user = current_user


def post(text, fb=False, twitter=False):
    if not (fb or twitter):
        flash('Neither Facebook nor Twitter specified.')
        print('Neither Facebook nor Twitter specified.')
        return

    mailbox = Mailbox(app.config['USERNAME'], app.config['PASSWORD'],
                      app.config['SMTPHOST'])

    if twitter:
        mailbox.send(RECIPIENTS, text, '#twitter')

    if fb:
        match = re.findall(LINK_PATTERN, text, flags=re.IGNORECASE)

        if match:
            # If there's a link at the end of the text, remove it.
            link = match[-1]
            if text.endswith(link):
                text = text[:-len(link)]
            mailbox.send(RECIPIENTS, text, '#fblink '+link)

        else:
            mailbox.send(RECIPIENTS, text, '#facebook')


def flash_errors(form):
    for field, messages in form.errors.items():
        label = getattr(getattr(getattr(form, field), 'label'), 'text', '')
        label = label.replace(':', '')
        error = ', '.join(messages)

        message = f'Error in {label}: {error}' if label else 'Error: {error}'

        flash(message)
        print(message)
