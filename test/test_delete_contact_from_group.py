from model.group import Group
from model.contact import Contact
from random import randrange


def test_delete_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Tester", middlename="Something", lastname="Trump",
                                   photo="picture.jpg", nickname="super nickname", title="QA engineer",
                                   company="Google", address="Kremlin", homephone="1111111",
                                   mobilephone="2222222", workphone="3333333", fax="4444444",
                                   email="test@test.com", email2="test2@test.com", email3="test3@test.com",
                                   homepage="google.com", bday="29", bmonth="April", byear="1991", aday="22",
                                   amonth="August", ayear="2015", address_2="Moscow", secondaryphone="5555555",
                                   notes="Cool guy"))
    # find any group with the contact inside
    group_ids = app.group.get_available_groups()
    group_id = None
    for group in group_ids:
        if len(db.get_contacts_in_group(group)) > 0:
            group_id = group
            break

    # if we didn't find any groups with contacts, let's add any contact to any group
    if group_id is None:
        groups = app.group.get_available_groups()
        group_id = groups[randrange(len(groups))]
        contacts = app.contact.get_contacts_list()
        contact_index = randrange(len(contacts))
        app.contact.add_contact_to_group(contact_index, group_id)

    # open contacts page for selected group
    contacts = app.contact.get_contacts_for_the_group(group_id)
    # choose any contact to remove from the group
    contact_index = randrange(len(contacts))
    contact = contacts[contact_index]
    app.contact.remove_contact_from_group(contact_index)

    contacts_not_in_group = db.get_contacts_not_in_group(group_id)
    contacts_not_in_group = app.contact.make_contacts_like_on_homepage(contacts_not_in_group)
    assert contacts_not_in_group.count(contact) > 0
