from model.project import Project
from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    soap = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

    project_cache = None

    def can_login(self, username, password):
        client = self.soap
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = self.soap
        try:
            project_list = client.service.mc_projects_get_user_accessible(username, password)
            self.project_cache = []
            for project in project_list:
                name = project.name
                status = project.status.name
                enabled = project.enabled
                view_status = project.view_state.name
                description = project.description
                self.project_cache.append(Project(name=name, status=status, enabled=enabled, view_status=view_status,
                                                  description=description))
            return list(self.project_cache)
        except WebFault:
            return []