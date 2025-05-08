class BOController:
    """Bayesian Optimizer that suggests mutation strategies."""
    def suggest(self):
        raise NotImplementedError("Suggest method not implemented.")

    def update(self, score):
        raise NotImplementedError("Update method not implemented.")
