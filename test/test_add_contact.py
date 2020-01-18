# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Tester", middlename="Something", lastname="Trump",
                               photo="picture.jpg", nickname="super nickname", title="QA engineer",
                               company="Google", address="Kremlin", home_phone="1111111",
                               mobile_phone="2222222", work_phone="3333333", fax="4444444",
                               email="test@test.com", email_2="test2@test.com", email_3="test3@test.com",
                               homepage="google.com", bday="29", bmonth="April", byear="1991", aday="22",
                               amonth="August", ayear="2015", address_2="Moscow", phone_2="5555555",
                               notes="Cool guy"))
    app.session.logout()

