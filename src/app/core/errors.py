

class FileOperationError(Exception):
    pass

class ShowFilesError(FileOperationError):
    pass

class ShowFilesWithSuffixError(FileOperationError):
    pass

class MoveFilesError(FileOperationError):
    pass



