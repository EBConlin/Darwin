# 🔬 Darwin System — Pinned Formalisms and Cognitive Architecture

This document integrates formal mathematical models into each core level of the Darwin architecture, including StimLang as a causal scaffold, causal attribution, dual cognitive modes, and dynamic control switching.

---

## 🧠 I. Level-Based Component Formalism

### **Level 1: Observation Layer**
- \( D \sim 	ext{TaskDistribution}(	ext{HEG}, 	ext{StimLang}, 	ext{Noise}) \)

### **Level 2: Attribution**
- \( A(T, D) = 	ext{LearnedAttributionModel.forward}(T, \mathcal{L}(T, D)) \)

### **Level 3: Theory**
- \( \mathcal{L}(T, D) = 	ext{LossFunction}(T, D) \)

### **Level 3.5: Motifs**
- \( f(M_i) = \sum_{T \supseteq M_i} \left[ A(M_i, D) \cdot (1 - \mathcal{L}(T, D)) 
ight] \)

### **Level 4: Program Generators**
- \( T \sim P(T \mid \Theta) \)
- \( \mathcal{E}(P, \Theta, D) = -\mathcal{L}(T, D) + \lambda \cdot 	ext{KL}(P \parallel Q) \)

---

## 🧪 II. StimLang as Causal Protocol

- StimLang: \( S = \{(I_t, O_t)\}_{t=1}^T \)
- Goal: Maximize identifiability of causal influence in theory structure
  \[
  \max_S \, \mathbb{E}_{T \sim P(T \mid \Theta)} \left[ 	ext{Identifiability}(G_T \mid S) 
ight]
  \]

---

## 🔗 III. Attribution as Causal Graph

- Causal Graph: \( G_T = (V, E, w) \)
- Weight inference:
  \[
  w(v_i 	o O) = \mathbb{E}[O \mid do(v_i=1)] - \mathbb{E}[O \mid do(v_i=0)]
  \]
- Reward:
  \[
  R_{	ext{clarity}}(T) = rac{1}{|E|} \sum_{e \in E} rac{|w(e)|}{\sigma(w)}
  \]

---

## 🧬 IV. StimLang Modes

- Clarification Mode: isolate attribution, deconfound theory
- Mutation Mode: identify instability, propose evolution
  \[
  G_T^{	ext{fine}} = 	ext{InferCausalGraph}(T, S_{	ext{clarify}}, D)
  \]
  \[
  M^* = 	ext{SuggestMutationTargets}(T, S_{	ext{mutate}}, D)
  \]

---

## 🧭 V. Dual Cognitive Modes + Control Switching

### Cognitive Modes
| Mode Type | Options |
|-----------|---------|
| Processing | Creative Embedding / Structural Implementation |
| Control | Bayesian Optimization / Evolutionary Reflex |

### Control Policy
Let \( \eta \) = entropy, \( R \) = resources, \( \Delta \mathcal{L} \) = loss change

\[
\pi(	ext{mode}) =
egin{cases}
	ext{Creative + BO}, & \eta > 	au_1 \land R > 
ho \\
	ext{Structural + BO}, & \eta \leq 	au_1 \land R > 
ho \\
	ext{Creative + Evolution}, & \eta > 	au_2 \land R \leq 
ho \\
	ext{Structural + Evolution}, & 	ext{otherwise}
\end{cases}
\]

---

This formalism is now pinned as the core cognitive-evolutionary framework in Darwin.
