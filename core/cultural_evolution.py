class CulturalEvolution:
    def __init__(self):
        self.history = []

    def evolve(self, theories):
        return sorted(theories, key=lambda x: x.get('score', 0), reverse=True)[:5]