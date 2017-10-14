class Logger:
    def __init__(self, quiet=False):
        self.quiet = quiet

    def log(self, message):
        if not self.quiet:
            print(message)
