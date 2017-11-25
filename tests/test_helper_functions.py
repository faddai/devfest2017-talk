from flask import url_for
from ideatank import hash_password


def test_hash_password():
    assert '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824' == hash_password(
        'hello')
