class Project:
    def __init__(self, name=None, status=None, enabled=True, inherit_global=True, view_status=None, description=None):
        self.name = name
        self.status = status
        self.enabled = enabled
        self.inherit_global = inherit_global
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return "%s" % self.name

    def __eq__(self, other):
        return self.name == other.name and self.status == other.status and self.enabled == other.enabled and \
               self.view_status == other.view_status and self.description == other.description

    def name(self):
        return self.name