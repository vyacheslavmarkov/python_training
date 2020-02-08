from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, photo=None, nickname=None, title=None,
                 company=None, address=None, homephone=None, mobilephone=None, workphone=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, address_2=None, secondaryphone=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email_2 = email2
        self.email_3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address_2 = address_2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:" % (self.id, self.firstname, self.lastname, self.address,
                                                      self.homephone, self.mobilephone, self.workphone, self.email,
                                                      self.email_2, self.email_3, self.secondaryphone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname and self.address == other.address \
               and self.homephone == other.homephone and self.mobilephone == other.mobilephone \
               and self.workphone == other.workphone and self.secondaryphone == other.secondaryphone \
               and self.email == other.email and self.email_2 == other.email_2 and self.email_3 == other.email_3

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
