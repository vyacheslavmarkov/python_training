# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    # concatenate emails and phones for the future comparison with db data
    contact.all_emails_from_homepage = contact.email + contact.email_2 + contact.email_3
    contact.all_phones_from_homepage = contact.homephone + contact.mobilephone + contact.workphone + contact.secondaryphone
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        # tune db contact data to be appropriate for the homepage representation
        old_contacts = app.contact.make_contacts_like_on_homepage(old_contacts)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
