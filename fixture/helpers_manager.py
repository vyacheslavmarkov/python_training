from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class HelpersManager:

    def __init__(self, app):
        app.session = SessionHelper(app)
        app.group = GroupHelper(app)
        app.contact = ContactHelper(app)
