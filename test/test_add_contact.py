# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    # tune added contact data to be appropriate for the homepage representation
    contact.firstname = app.contact.truncate_whitespaces(contact.firstname)
    contact.lastname = app.contact.truncate_whitespaces(contact.lastname)
    contact.address = app.contact.truncate_whitespaces(contact.address)
    contact.all_phones_from_homepage = app.contact.merge_phones_like_on_homepage(contact)
    contact.all_emails_from_homepage = app.contact.merge_emails_like_on_homepage(contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)