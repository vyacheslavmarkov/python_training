from random import randrange


def test_contact_on_home_page(app):
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.homephone == app.contact.clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == app.contact.clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == app.contact.clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.secondaryphone == app.contact.clear(contact_from_edit_page.secondaryphone)
    assert contact_from_home_page.email == contact_from_edit_page.email
    assert contact_from_home_page.email_2 == contact_from_edit_page.email_2
    assert contact_from_home_page.email_3 == contact_from_edit_page.email_3
