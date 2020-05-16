from model.project import Project
import random


def test_del_project(app):
    check_projects_count(app, Project(name="best project", status="stable", inherit_global=True, view_status="public",
                                      description="the best project for deletion"))
    old_projects_list = app.project.get_project_list()
    project = random.choice(old_projects_list)
    app.project.del_project(project)
    old_projects_list.remove(project)
    new_projects_list = app.project.get_project_list()
    assert sorted(old_projects_list, key=Project.name) == sorted(new_projects_list, key=Project.name)


def check_projects_count(app, project):
    if len(app.project.get_project_list()) == 0:
        app.project.create(project)
