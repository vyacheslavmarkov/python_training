from random import randrange


def test_contact_on_home_page(app):
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_homepage == \
           app.contact.merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_homepage == \
           app.contact.merge_emails_like_on_homepage(contact_from_edit_page)
