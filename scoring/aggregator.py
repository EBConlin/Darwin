class ScoringAggregator:
    def compute_scores(self, agent_output):
        return {
            'utility': ..., 'novelty': ..., 'interpretability': ..., 'uncertainty': ...
        }
