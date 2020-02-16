from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    return str(random.randrange(1, 28))


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return months[random.randrange(len(months))]


def random_year():
    return str(random.randrange(1900, 2000))


def random_picture():
    pictures = ["picture.jpg", "picture2.jpg"]
    return pictures[random.randrange(len(pictures))]


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastaname", 10), photo=random_picture(), nickname=random_string("nickname", 5),
            title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 15), homephone=random_string("homephone", 7),
            mobilephone=random_string("mobilephone", 7), workphone=random_string("workphone", 7),
            fax=random_string("fax", 7), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email2", 30), homepage=random_string("homepage", 10), bday=random_day(),
            bmonth=random_month(), byear=random_year(), aday=random_day(), amonth=random_month(),
            ayear=random_year(), address_2=random_string("address2", 10),
            secondaryphone=random_string("secondaryphone", 7), notes=random_string("notes", 20))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
