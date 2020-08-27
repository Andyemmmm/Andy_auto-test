#!/usr/bin/python3
# _*_ coding:utf8 _*_
# @Author   : Andy
# @time     : 2019/12/16 21:07
# @File     : demo.py
# @Software : aiwen_ui

import pytest


# test1.py
@pytest.mark.skip
def test_001():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.skip
def test_002():
    assert 1 + 1 == 1


@pytest.mark.skip
def test_003():
    assert 1 + 1 == 2


@pytest.mark.parametrize('user, passwd',
                         [('jack', 'abcdefgh'),
                          ('tom', 'a123456a')])
def test_passwd_md5(user, passwd):
    db = {
        'jack': 'e8dc4081b13434b45189a720b77b6818',
        'tom': '1702a132e769a623c1adb78353fc9503'
    }

    import hashlib
    assert hashlib.md5(passwd.encode()).hexdigest() == db[user]


@pytest.fixture()
def postcode():
    return '010'


def test_postcode(postcode):
    assert postcode == '010'
