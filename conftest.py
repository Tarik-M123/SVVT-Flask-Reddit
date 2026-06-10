import pytest
from app import create_app, db


@pytest.fixture
def app():
    # Build an app using the 'testing' configuration.
    # TestingConfig uses an in-memory SQLite database,
    # so we never touch your real dev.db file.
    app = create_app('testing')

    # 'app_context' makes the app the "current" app so that
    # the database and models know which app they belong to.
    with app.app_context():
        db.create_all()      # build all the tables fresh
        yield app            # hand the ready app to the test
        db.session.remove()  # clean up the session afterwards
        db.drop_all()        # delete all tables so next test starts clean


@pytest.fixture
def client(app):
    # A "test client" lets us send fake browser requests
    # to the app without running a real server.
    return app.test_client()