from selenium.webdriver.support.ui import Select
from model.project import Project
import random
import re


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_link_text("Manage Projects"))) > 0 or \
                (len(wd.find_elements_by_link_text("Manage Users"))) > 0:
            wd.find_element_by_link_text("Manage").click()

    def open_projects_page(self):
        wd = self.app.wd
        self.open_manage_page()
        if not len(wd.find_elements_by_xpath("(//input[@value='Add Project'])")) > 0:
            wd.find_element_by_link_text("Manage Projects").click()

    def open_project_create_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_create_page.php") and
                len(wd.find_elements_by_xpath("(//input[@value='Add Project'])")) > 0):
            self.open_projects_page()
            wd.find_element_by_xpath("(//input[@value='Create New Project'])").click()

    def set_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def set_selected_value(self, field_name, text):
        wd = self.app.wd
        if text is not None and text != '':
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def set_checkbox_value(self, field_name, value):
        wd = self.app.wd
        if not value:
            wd.find_element_by_name(field_name).click()

    def create(self, project):
        wd = self.app.wd
        # open create page
        self.open_project_create_page()
        # fill fields
        self.set_field_value("name", project.name)
        self.set_selected_value("status", project.status)
        self.set_checkbox_value("inherit_global", project.inherit_global)
        self.set_selected_value("view_state", project.view_status)
        self.set_field_value("description", project.description)
        # submit adding
        wd.find_element_by_xpath("(//input[@value='Add Project'])").click()
        # return to project page
        wd.find_element_by_link_text("Proceed").click()

    project_cache = None

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        self.project_cache = []
        rows = wd.find_elements_by_xpath("//table[@class='width100']//tr[@class='row-1' or @class='row-2']")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            status = cells[1].text
            enabled = True if cells[2].text == 'X' else False
            view_status = cells[3].text
            description = cells[4].text
            self.project_cache.append(Project(name=name, status=status, enabled=enabled, view_status=view_status,
                                              description=description))
        return list(self.project_cache)