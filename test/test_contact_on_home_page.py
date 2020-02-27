from model.contact import Contact


def test_contacts_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)

    assert len(contacts_from_home_page) == len(contacts_from_db)
    for index, contact in enumerate(contacts_from_home_page):
        assert contact.firstname == app.contact.truncate_whitespaces(contacts_from_db[index].firstname)
        assert contact.lastname == app.contact.truncate_whitespaces(contacts_from_db[index].lastname)
        assert contact.address == app.contact.truncate_whitespaces(contacts_from_db[index].address)
        assert contact.all_phones_from_homepage == app.contact.merge_phones_like_on_homepage(contacts_from_db[index])
        assert contact.all_emails_from_homepage == app.contact.merge_emails_like_on_homepage(contacts_from_db[index])
