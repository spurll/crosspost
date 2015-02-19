from ldap3 import Server, Connection

from crosspost import app


def authenticate(username, password):
    user = None

    # Initial connection to the LDAP server.
    server = Server(app.config['LDAP_URI'])
    connection = Connection(server)

    try:
        if not connection.bind(): return None

        # Verify that the user exists.
        result = connection.search(search_base=app.config['LDAP_SEARCH_BASE'],
                                   search_filter='(uid={})'.format(username),
                                   attributes=['mail', 'cn'])

        if not result: return None

        # The user exists!
        name = connection.response[0]['attributes']['cn'][0]
        email = connection.response[0]['attributes']['mail'][0]

        # Now attempt to re-bind and authenticate with the password.
        distinguished_name = connection.response[0]['dn']
        connection = Connection(server, user=distinguished_name,
                                password=password.encode('iso8859-1'))

        if not connection.bind(): return None

        # We're authenticated! Create the actual user object.
        user = User(username, name, email)

    finally:
        connection.unbind()
        return user


def load_user_info(username):
    user = None

    # Initial connection to the LDAP server.
    server = Server(app.config['LDAP_URI'])
    connection = Connection(server)

    try:
        if not connection.bind(): return None

        # Verify that the user exists.
        result = connection.search(search_base=app.config['LDAP_SEARCH_BASE'],
                                   search_filter='(uid={})'.format(username),
                                   attributes=['mail', 'cn'])

        if not result: return None

        # The user exists!
        name = connection.response[0]['attributes']['cn'][0]
        email = connection.response[0]['attributes']['mail'][0]
        user = User(username, name, email)

    finally:
        connection.unbind()
        return user


class User:
    def __init__(self, id, name=None, email=None):
        self.id = id
        self.name = name
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_admin(self):
        return self.id == app.config["LDAP_USER"]

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {}>'.format(self.id)


