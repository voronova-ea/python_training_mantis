from model.project import Project


def test_add_project(app):
    project = Project(name="test12", status="release", inherit_global=False, view_status="public",
                      description="test description")
    check_same_name(app, project)
    old_projects_list = app.project.get_project_list()
    app.project.create(project)
    old_projects_list.append(project)
    new_projects_list = app.project.get_project_list()
    assert sorted(old_projects_list, key=Project.name) == sorted(new_projects_list, key=Project.name)


def check_same_name(app, project):
    projects_list = app.project.get_project_list()
    for proj in projects_list:
        if project.name == proj.name:
            app.project.del_project(proj)
            break