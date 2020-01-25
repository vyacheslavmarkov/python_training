from model.group import Group


# test from the previous home task
def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="Edited name", header="Edited header text", footer="Edited footer text"))

