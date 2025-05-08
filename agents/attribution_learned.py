class LearnedAttributionModel:
    """TreeLSTM attribution model mapping theory and score to component scores."""
    def forward(self, theory_tree, performance_score):
        raise NotImplementedError("Forward pass not implemented.")

    def train(self, dataset):
        raise NotImplementedError("Training routine not implemented.")
