import os.path


class CurrentWorkingDirectory(object):
    """ Represents the current working directory for the application """

    def __init__(self, path):
        self._path = path

    @property
    def directory_name(self):
        return os.path.dirname(self._path)

    def list_files(self):
        pass

    def _set_current_working_directory(self, path,
                                       create_if_not_existant=False):
        if not os.path.isdir(path):
            raise NoDirectory(path)

        if not os.path.exists(path):
            if create_if_not_existant:
                self._create_directory_at(path)
            else:
                raise DirectoryNotExistant(path)

        absolute_path = path
        if not os.path.isabs(path):
            absolute_path = os.path.abspath(path)

    def _create_directory_at(self, path):
        pass


class NoDirectory(Exception):
    """ Exception that is raised when a filesystem path does not point to a directory """

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.__repr__(self)

    def __repr__(self):
        return "The given path does not point to a directory: {path}".format(
            path=self.path)


class DirectoryNotExistant(Exception):
    """ Exception that is raised when the directory at the given path does not exist """

    def __init__(self, path):
        self.__path = path
        self.__directoryName = os.path.dirname(path)

    def __str__(self):
        return self.__repr__(self)

    def __repr__(self):
        return "The directory \'{directory}\' does not exist at the given path: {path}".format(
            directory=self.__directoryName, path=self.__path)
