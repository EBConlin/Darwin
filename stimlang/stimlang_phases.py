class StimLangPhase:
    def __init__(self, name, state_machine):
        self.name = name
        self.state_machine = state_machine

class StimLangProgram:
    def __init__(self, phases):
        self.phases = phases
