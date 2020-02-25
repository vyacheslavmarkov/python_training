from model.contact import Contact
import random


def test_delete_first_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tester", middlename="Something", lastname="Trump",
                                   photo="picture.jpg", nickname="super nickname", title="QA engineer",
                                   company="Google", address="Kremlin", homephone="1111111",
                                   mobilephone="2222222", workphone="3333333", fax="4444444",
                                   email="test@test.com", email2="test2@test.com", email3="test3@test.com",
                                   homepage="google.com", bday="29", bmonth="April", byear="1991", aday="22",
                                   amonth="August", ayear="2015", address_2="Moscow", secondaryphone="5555555",
                                   notes="Cool guy"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        # tune db contact data to be appropriate for the homepage representation
        old_contacts = app.contact.make_contacts_like_on_homepage(old_contacts)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
