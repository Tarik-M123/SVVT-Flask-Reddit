import pytest
from app.models import User, Post


# ---------- PASSWORD TESTS ----------

def test_password_setter(app):
    u = User(password='cat')
    assert u.password_hash is not None


def test_no_password_getter(app):
    u = User(password='cat')
    with pytest.raises(AttributeError):
        u.password


def test_password_verification(app):
    u = User(password='cat')
    assert u.verify_password('cat') is True
    assert u.verify_password('dog') is False


def test_passwords_are_random(app):
    u1 = User(password='cat')
    u2 = User(password='cat')
    assert u1.password_hash != u2.password_hash


# ---------- GRAVATAR TEST ----------

def test_gravatar_hash(app):
    u = User(email='john@example.com')
    assert u.gravatar_hash() == u.gravatar_hash()


# ---------- POST TITLE TEST ----------

def test_remove_space_from_title(app):
    p = Post(title='My Cool Post')
    p.remove_space_from_title()
    assert p.title == 'My-Cool-Post'

def test_change_username(app):
    # Create a user, then change their username.
    u = User(username='old_name')
    u.change_username('new_name')
    # The username should now be updated.
    assert u.username == 'new_name'

def test_username_allows_special_characters(app):
    # The app does NOT validate usernames, so even a username
    # full of special characters is accepted without error.
    # This test PASSING actually demonstrates a WEAKNESS:
    # there is no input validation on usernames.
    u = User(username='!!!@#$%^&*()')
    u.change_username('<script>alert(1)</script>')
    assert u.username == '<script>alert(1)</script>'


def test_change_password(app):
    u = User(password='oldpass')
    u.change_password('newpass')
    assert u.verify_password('newpass') is True
    assert u.verify_password('oldpass') is False


def test_user_repr(app):
    # The __repr__ method should produce a readable string
    # containing the username and email.
    u = User(username='tarik', email='tarik@example.com')
    assert repr(u) == '<User: tarik tarik@example.com>'


def test_post_repr(app):
    # The Post __repr__ should contain the post title.
    p = Post(title='Hello World')
    assert repr(p) == '<Post: Hello World>'
