import smtplib

from pytest import fixture


@fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP(host="smtp.gmail.com", port=587, timeout=5)
