class Folder:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __repr__(self):
        return f"Folder(name={self.name}, path={self.path})"