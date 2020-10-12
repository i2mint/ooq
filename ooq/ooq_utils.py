class ModuleNotFoundIgnore:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ModuleNotFoundError:
            pass
        return True

module_not_found_ignore = ModuleNotFoundIgnore()
