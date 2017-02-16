# sqlite_checkforeignkeys
A sqlite engine that checks foreign keys

This references the django sqlite engine and overrides one of its methods. When a new connection is created it [turns on the foreign key checking as per the sqlite documentation](http://www.sqlite.org/foreignkeys.html)

There is a test that tests this specific behavior, built using pytest. Changing engines to the base sqlite engine causes the test to fail

To use this in your own project, add the engine app folder into your project, and change your database engine to the new engine.
