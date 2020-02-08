# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    return str(random.randrange(1, 28))


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return months[random.randrange(len(months))]


def random_year():
    return str(random.randrange(1900, 2000))


def random_picture():
    pictures = ["picture.jpg", "picture2.jpg"]
    return pictures[random.randrange(len(pictures))]


test_data = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastaname", 10), photo=random_picture(), nickname=random_string("nickname", 5),
            title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 15), homephone=random_string("homephone", 7),
            mobilephone=random_string("mobilephone", 7), workphone=random_string("workphone", 7),
            fax=random_string("fax", 7), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email2", 30), homepage=random_string("homepage", 10), bday=random_day(),
            bmonth=random_month(), byear=random_year(), aday=random_day(), amonth=random_month(),
            ayear=random_year(), address_2=random_string("address2", 10),
            secondaryphone=random_string("secondaryphone", 7), notes=random_string("notes", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    # tune added contact data to be appropriate for the homepage representation
    contact.firstname = app.contact.truncate_whitespaces(contact.firstname)
    contact.lastname = app.contact.truncate_whitespaces(contact.lastname)
    contact.address = app.contact.truncate_whitespaces(contact.address)
    contact.homephone = app.contact.clear(contact.homephone)
    contact.workphone = app.contact.clear(contact.workphone)
    contact.mobilephone = app.contact.clear(contact.mobilephone)
    contact.secondaryphone = app.contact.clear(contact.secondaryphone)
    contact.email = app.contact.truncate_whitespaces(contact.email)
    contact.email_2 = app.contact.truncate_whitespaces(contact.email_2)
    contact.email_3 = app.contact.truncate_whitespaces(contact.email_3)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)