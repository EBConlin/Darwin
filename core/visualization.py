import matplotlib.pyplot as plt

def plot_attribution_scores(scores):
    plt.bar(range(len(scores)), scores)
    plt.title('Attribution Scores')
    plt.show()