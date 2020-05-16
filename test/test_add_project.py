from model.project import Project


def test_add_project(app):
    project = Project(name="test1365", status="release", inherit_global=False, view_status="public",
                      description="test description")
    old_project_list = app.project.get_project_list()
    app.project.create(project)
    new_project_list = app.project.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.name) == sorted(new_project_list, key=Project.name)