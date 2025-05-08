class StimLang:
    def __init__(self):
        self.commands = []

    def add_command(self, cmd):
        self.commands.append(cmd)

    def serialize(self):
        return ' '.join(self.commands)