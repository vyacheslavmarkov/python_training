from model.group import Group
from model.contact import Contact
from random import randrange


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    if len(db.get_contact_list()) == 0:
        app.contact.create_simple_contact()

    # try to find any contact & group that are not paired together
    contacts = db.get_contact_list()
    groups = db.get_group_list()

    contact_to_add = None
    group_to_add = None

    for group in groups:
        if contact_to_add is None:
            for contact in contacts:
                contacts_in_group = db.get_contacts_in_group(group.id)
                # if this group doesn't contain this contact, let's use them for the test
                if contacts_in_group.count(contact) == 0:
                    contact_to_add = contact
                    group_to_add = group
                    break
        else:
            break

    # if there is no contact & group that are not paired, let's create new contact and add it to any group
    if contact_to_add is None:
        app.contact.create_simple_contact()
        # get the newest contact (with biggest id)
        contacts = db.get_contact_list()
        contact_to_add = sorted(contacts, key=Contact.id_or_max)[len(contacts) - 1]
        group_to_add = groups[randrange(len(groups))]

    # add contact to the group
    contact_to_add_index = app.contact.get_contact_index_by_id(contact_to_add.id)
    app.contact.add_contact_to_group(contact_to_add_index, group_to_add.id)

    # check that contact is really in the group
    contacts_in_group = db.get_contacts_in_group(group_to_add.id)
    assert contacts_in_group.count(contact_to_add) > 0
