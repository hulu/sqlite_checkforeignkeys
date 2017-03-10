# sqlite_checkforeignkeys
A sqlite engine that checks foreign keys

## Database Engine

This references the django sqlite engine and overrides one of its methods. When a new connection is created it [turns on the foreign key checking as per the sqlite documentation](http://www.sqlite.org/foreignkeys.html)

This package supports setup.py, to use it, install the package, then change your database engine to: `sqlite_checkforeignkeys_engine`

There is also a weirdness in pytest where it doesn't know that this is actually sqlite, so if you want to run an in-memory DB for tests, you'll need to specify the in-memory DB manually. Which means that for a test config, your `DATABASES` assignment will probably look like this:

    DATABASES = {
        'default': {
            'ENGINE': 'sqlite_checkforeignkeys_engine',
            'TEST': {'NAME': ':memory:'},
        }
    }

## Repository

The repository contains three folders.

* `sqlite_checkforeignkeys_engine` - This is the new database engine for django that supports foreign key checking. This is the only piece that gets installed using setup.py
* `sqlite_checkforeignkeys` - This is the core django app for the project. It hosts the standard django webserver code. The settings file has been modified to use the previously-mentioned database engine
* `sample_app` - This is the app that hosts the models needed for the sample django project, and it also has a test that tests this specific behavior using those models. The tests are pytest style tests. The tests can be run with the `py.test` command. Changing engines to the standard sqlite engine causes the test to fail.
