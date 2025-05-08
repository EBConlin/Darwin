
# 🌱 Darwin Lab (Refactored)

**Meta-evolutionary scientific cognition system** — evolving agents, symbolic theories, motifs, and experimental protocols.

---

## 🔧 Core Formalism

### Agent Loop
1. **Generate Theory**: Symbolic structure with motifs.
2. **Evaluate Theory**: Against tasks or simulated environments.
3. **Attribution**: Score subcomponents via TreeLSTM.
4. **Mutation**: Modify structure based on attribution.
5. **Bayesian Optimization**: Update strategy weights.
6. **Cultural Evolution**: Retain, recombine, compress.

---

### Key Abstractions
| Concept         | Role                                                                 |
|----------------|----------------------------------------------------------------------|
| `Agent`         | Evolves symbolic theories, scored by utility + novelty              |
| `Motif`         | Reusable building block for theories (symbolic, cognitive, neural)  |
| `StimLang`      | Linearized protocol used for experiment/task delivery               |
| `HEG`           | Hierarchical Embedded Graph for reasoning, curriculum, compression  |
| `MetaAgent`     | Synergetic controller — tracks entropy, triggers bifurcations       |
| `TreeLSTM`      | Learns attribution over tree-structured theories                    |

---

## 📂 Modules

- `agents/`         → Theory generators, interpreters, and learning models
- `evolution/`      → Core loop, synergetics meta-layer
- `motifs/`         → Memory, abstraction, perturbation scoring
- `biobridge/`      → Kaya interface (astrocyte and neuron feedback)
- `tasks/`          → Task definitions and curriculum engine
- `dashboard/`      → Live strategy & attribution visualization
- `metrics/`        → Theory complexity, compression scoring

---

## 🔮 Vision
Darwin is a recursive theory engine.
It learns how to mutate, how to attribute, and how to structure symbolic knowledge via evolution, optimization, and biological feedback.

