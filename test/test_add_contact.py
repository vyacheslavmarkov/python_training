# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_user(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Tester", middlename="Something", lastname="Trump",
                      photo="picture.jpg", nickname="super nickname", title="QA engineer",
                      company="Google", address="Kremlin", home_phone="1111111",
                      mobile_phone="2222222", work_phone="3333333", fax="4444444",
                      email="test@test.com", email_2="test2@test.com", email_3="test3@test.com",
                      homepage="google.com", bday="29", bmonth="April", byear="1991", aday="22",
                      amonth="August", ayear="2015", address_2="Moscow", phone_2="5555555",
                      notes="Cool guy")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
