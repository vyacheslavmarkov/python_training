from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New", middlename="Something new", lastname="Obama",
                                           photo="picture2.jpg", nickname="new nickname", title="SDET",
                                           company="Yandex", address="Washington", home_phone="2222222",
                                           mobile_phone="3333333", work_phone="4444444", fax="5555555",
                                           email="new@test.com", email_2="new2@test.com", email_3="new3@test.com",
                                           homepage="yandex.ru", bday="15", bmonth="May", byear="1982", aday="13",
                                           amonth="September", ayear="1999", address_2="Samara", phone_2="7777777",
                                           notes="New note"))
    app.session.logout()
