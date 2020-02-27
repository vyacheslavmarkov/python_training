from model.group import Group
from random import randrange


def test_delete_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    if len(db.get_contact_list()) == 0:
        app.contact.create_simple_contact()

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
