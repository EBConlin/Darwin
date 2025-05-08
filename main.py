# Entry point for Darwin Lab experiments

from agents.agent import DarwinAgent

def run_experiment():
    agent = DarwinAgent()
    agent.run()

if __name__ == '__main__':
    run_experiment()
