def allowed_file(filename):
    from devjobs import ALLOWED_EXTENSIONS
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_token():
    import uuid
    from os import urandom
    return uuid.UUID(bytes=urandom(16))

def generate_salt():
    from os import urandom
    return urandom(16).encode('base_64')
