class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Миша всё фигня! Давай сначала!'

    def __str__(self):
        return str(self.message)
