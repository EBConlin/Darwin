import yaml
from theory_tree import TheoryNode, generate_random_theory
from HEG_task_runner import get_task
from evaluation_engine import evaluate_theory
from attribution_learned import compute_attribution
from joint_perturbation import perturbation_attribution
from bo_controller import propose_strategy, update_strategies
from motif_tracker import register_motifs

class DarwinLoop:
    def __init__(self, config_path: str):
        self.load_config(config_path)
        self.generation_count = 0
        self.generation_data = []

    def load_config(self, path):
        with open(path, 'r') as f:
            self.config = yaml.safe_load(f)

    def run(self):
        while self.generation_count < self.config["max_generations"]:
            print(f"\n--- Generation {self.generation_count} ---")
            for agent_id in self.config["agents"]:
                task = get_task(agent_id)
                strategy = propose_strategy(agent_id)
                theory = generate_random_theory(2)
                score = evaluate_theory(theory, task)

                if score < self.config["attribution"]["score_threshold"]:
                    attribution = perturbation_attribution(theory, task)
                else:
                    attribution = compute_attribution(theory, score)

                register_motifs(theory)
                self.generation_data.append((theory, score, strategy))

            if self.generation_count % self.config["bo_update_interval"] == 0:
                update_strategies(self.generation_data)
                self.generation_data.clear()

            self.generation_count += 1