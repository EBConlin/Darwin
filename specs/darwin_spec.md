# Darwin Lab Specification

## Overview
Darwin Lab is an evolutionary reasoning system designed to evolve scientific theories through a process of generation, attribution, optimization, and cultural selection. It simulates a population of agents generating and refining hypotheses, scoring their relevance, and modifying strategies using neural attribution models and Bayesian optimization. All processes can be visualized and logged.

---

## Module Specifications

### main.py
- **Role**: Entry point for Darwin Lab experiments.
- **Functions**:
  - `run_experiment()`: Runs full experiment loop and calls into all subsystems.

### agent.py
- **Role**: Represents an agent that generates and mutates symbolic theories.
- **Functions**:
  - `generate_theory() -> dict`: Returns a nested symbolic theory structure.
  - `mutate_theory(theory) -> dict`: Applies mutation logic.
  - `evaluate_theory(theory, env) -> float`: Returns a score based on environment/task.

### attribution_learned.py
- **Role**: Learnable attribution model, e.g., TreeLSTM, that maps theory structure and performance to per-component contribution scores.
- **Functions**:
  - `forward(theory_tree, performance_score) -> vector`: Returns attribution score vector.
  - `train(dataset)`: Learns to map (theory, score) to attribution vectors.

### bayesian_optimization.py
- **Role**: Suggests new strategies for theory mutation and credit assignment.
- **Functions**:
  - `suggest() -> dict`: Proposes next mutation strategy.
  - `update(score: float)`: Learns from performance outcome.
  - Tracks and evolves mutation/attribution parameters.

### stimlang.py
- **Role**: Converts symbolic theories into linearized command sequences.
- **Functions**:
  - `add_command(str)`: Adds command to buffer.
  - `serialize() -> str`: Converts to serialized stimlang string.

### cultural_evolution.py
- **Role**: Maintains evolutionary history and selects top theories.
- **Functions**:
  - `evolve(theory_list: list) -> list`: Selects best N theories by score.
  - `record(history_entry)`: Logs theory lineage.

### visualization.py
- **Role**: Plots attribution scores and theory evolution.
- **Functions**:
  - `plot_attribution_scores(score_list)`: Bar chart of current attribution.
  - `plot_strategy_change(history)`: Line graph of BO or attribution trends.

### dashboard.py
- **Role**: Displays live feedback from all Darwin modules.
- **Functions**:
  - `update(dict)`: Pushes new state or result to dashboard buffer.
  - `render()`: Optional method to visually render update set.

---

## Data Flow Summary

1. **Agents** generate theories using `generate_theory()`.
2. Theories are scored via `evaluate_theory()`.
3. Theories + scores are fed into `attribution_learned` for structural credit assignment.
4. BO updates its model based on attribution + reward.
5. `cultural_evolution` filters top theories and passes them on.
6. `stimlang` converts theories into executable sequences.
7. `visualization` and `dashboard` update the user in real time.

