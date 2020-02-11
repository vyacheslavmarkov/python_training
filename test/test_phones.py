

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == app.contact.merge_phones_like_on_homepage(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == app.contact.clear(contact_from_edit_page.homephone)
    assert contact_from_view_page.workphone == app.contact.clear(contact_from_edit_page.workphone)
    assert contact_from_view_page.mobilephone == app.contact.clear(contact_from_edit_page.mobilephone)
    assert contact_from_view_page.secondaryphone == app.contact.clear(contact_from_edit_page.secondaryphone)



