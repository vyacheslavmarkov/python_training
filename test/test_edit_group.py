from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Edited name", header="Edited header text", footer="Edited footer text"))

