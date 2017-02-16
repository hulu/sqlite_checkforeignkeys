"""The Base behavior of the modified Sqlite engine"""

from django.db.backends.sqlite3.base import DatabaseWrapper as dw

class DatabaseWrapper(dw):
    """Overwrites the behavior of DatabaseWrapper to turn on Foreign Key constraint checking"""
    def get_new_connection(self, conn_params):
        """Turns on `foreign_keys` for every connection"""
        conn = super(DatabaseWrapper, self).get_new_connection(conn_params)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
