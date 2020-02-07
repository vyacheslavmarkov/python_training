from model.contact import Contact
from random import randrange


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tester", middlename="Something", lastname="Trump",
                                   photo="picture.jpg", nickname="super nickname", title="QA engineer",
                                   company="Google", address="Kremlin", homephone="1111111",
                                   mobilephone="2222222", workphone="3333333", fax="4444444",
                                   email="test@test.com", email2="test2@test.com", email3="test3@test.com",
                                   homepage="google.com", bday="29", bmonth="April", byear="1991", aday="22",
                                   amonth="August", ayear="2015", address_2="Moscow", secondaryphone="5555555",
                                   notes="Cool guy"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New", middlename="Something new", lastname="Obama",
                      photo="picture2.jpg", nickname="new nickname", title="SDET",
                      company="Yandex", address="Washington", homephone="2222222",
                      mobilephone="3333333", workphone="4444444", fax="5555555",
                      email="new@test.com", email2="new2@test.com", email3="new3@test.com",
                      homepage="yandex.ru", bday="15", bmonth="May", byear="1982", aday="13",
                      amonth="September", ayear="1999", address_2="Samara", secondaryphone="7777777",
                      notes="New note")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

