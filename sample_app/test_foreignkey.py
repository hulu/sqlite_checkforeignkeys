import pytest
# from django.db.utils import IntegrityError
# from django.db.backends import sqlite3

from sample_app.models import Referencer


@pytest.mark.django_db
def test_break_foreign_key():
    """Tries to violate the foreign key"""
    # Referenced.objects.create()
    # with pytest.raises(IntegrityError):
    Referencer.objects.create(fk_id=-1)
