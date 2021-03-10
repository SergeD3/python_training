# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import AddContact2
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.group.fill_contact_form(AddContact2(
        middle_name="middle name 1",
        first_name="name 1",
        last_name="last name 1",
        user_nick="nick 1",
        user_title="title 1",
        user_company="wrum",
        user_adress="lazer 5, Moscow",
        user_home="784763587643",
        user_mob="746358746357",
        user_email="weuyrt@iwer.ri",
        user_bday="17",
        user_bmonth="October",
        user_byear="1980",
        user_group="new group2",
        user_addr2="lazer 5, Russian Federation",
        user_phone2="rgegregreg",
        user_note="notes from user"))
    app.session.logout()

