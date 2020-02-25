from model.contact import Contact


def test_contacts_on_home_page(app, db):
    contacts_from_homepage = app.contact.get_contacts_list()
    contacts_from_db = db.get_contact_list()
    contacts_from_db = app.contact.make_contacts_like_on_homepage(contacts_from_db)
    assert sorted(contacts_from_homepage, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)

