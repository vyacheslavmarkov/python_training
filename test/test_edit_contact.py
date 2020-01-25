from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tester", middlename="Something", lastname="Trump",
                               photo="picture.jpg", nickname="super nickname", title="QA engineer",
                               company="Google", address="Kremlin", home_phone="1111111",
                               mobile_phone="2222222", work_phone="3333333", fax="4444444",
                               email="test@test.com", email_2="test2@test.com", email_3="test3@test.com",
                               homepage="google.com", bday="29", bmonth="April", byear="1991", aday="22",
                               amonth="August", ayear="2015", address_2="Moscow", phone_2="5555555",
                               notes="Cool guy"))
    app.contact.edit_first_contact(Contact(firstname="New", middlename="Something new", lastname="Obama",
                                           photo="picture2.jpg", nickname="new nickname", title="SDET",
                                           company="Yandex", address="Washington", home_phone="2222222",
                                           mobile_phone="3333333", work_phone="4444444", fax="5555555",
                                           email="new@test.com", email_2="new2@test.com", email_3="new3@test.com",
                                           homepage="yandex.ru", bday="15", bmonth="May", byear="1982", aday="13",
                                           amonth="September", ayear="1999", address_2="Samara", phone_2="7777777",
                                           notes="New note"))

