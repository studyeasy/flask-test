from flask import Flask
import semantic_version


app = Flask(__name__)

semantic_version.Version('1.0.2')

@app.route("/")
def hello_world():
    """
    Initialize Security for application.

    :param kwargs: parameters that will be passed through to Flask-Security
    :type kwargs: dict
    :returns: None

    >>> def ext_security(self):
    >>>    super(MyApp, self).ext_security(confirm_register_form=CaptchaRegisterForm)
    """
    return "<p>Hello, World updated!</p>"