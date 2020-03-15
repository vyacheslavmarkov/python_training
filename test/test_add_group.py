# -*- coding: utf-8 -*-
from model.group import Group
import allure


@allure.step('Given a group list')
def step_group_list(db):
    return db.get_group_list()


@allure.step('When I add a group to the list')
def step_create_group(app, group):
    app.group.create(group)


@allure.step('Then the new group list is equal to the old list with the added group')
def step_groups_lists_equal(app, db, old_groups, group, check_ui):
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = step_group_list(db)
    step_create_group(app, group)
    step_groups_lists_equal(app, db, old_groups, group, check_ui)


