class File:
    def __init__(self, name, path, size, date, stream=None, title=None, description=None, thumbnail=None):
        self.name = name
        self.path = path
        self.size = size
        self.date = date
        self.stream = stream
        self.title = title
        self.description = description
        self.thumbnail = thumbnail

    def __repr__(self):
        return f"File(name={self.name}, path={self.path}, size={self.size}, date={self.date}, stream={self.stream})"


