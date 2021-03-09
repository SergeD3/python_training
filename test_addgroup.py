# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.login(user_name="admin", password="secret")
        app.create_group(Group(name="new group2", header="qwerty", footer="qwerty"))
        app.logout()


def test_add_empty_group(app):
        app.login(user_name="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()