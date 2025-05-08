
# 🌱 Darwin System — Pinned Formalisms and Cognitive Architecture

This document formalizes the Darwin learning architecture using a layered HBM (Hierarchical Bayesian Model) framework. It integrates causal attribution, StimLang-based experimentation, motif reuse, and adaptive cognitive control.

---

## 🧠 I. Level-Based Component Formalism

### 🧩 Level 1: Observation Layer

**Symbol:** 𝐷  
**Meaning:** Task data from HEG paths, StimLang protocols, or synthetic environments.  
**Sampling:**  
𝐷 ∼ TaskDistribution(HEG, StimLang, Noise)

---

### 🧠 Level 2: Attribution

**Symbol:** 𝐴(𝑇, 𝐷)  
**Meaning:** Attribution map assigning credit or blame to components of theory 𝑇 based on outcome from task 𝐷.  
**Computation:**  
𝐴(𝑇,𝐷) = LearnedAttributionModel.forward(𝑇, 𝐿(𝑇,𝐷))

---

### 🧠 Level 3: Theory

**Symbol:** 𝑇  
**Meaning:** Structured symbolic hypothesis (tree of rules/motifs).  
**Loss Function:**  
𝐿(𝑇,𝐷) = LossFunction(𝑇,𝐷)

---

### 🧠 Level 3.5: Motifs

**Symbol:** 𝑀ᵢ ⊆ 𝑇  
**Meaning:** Reusable substructures within theories.  
**Fitness:**  
𝑓(𝑀ᵢ) = ∑ₜ⊇𝑀ᵢ [𝐴(𝑀ᵢ,𝐷) ⋅ (1 − 𝐿(𝑇,𝐷))]

---

### 🧠 Level 4: Probabilistic Program Generators

**Symbols:**  
𝑃(𝑇 ∣ Θ): Generator of symbolic theories  
Θ: Meta-prior (e.g., grammar rule weights)  
**Sampling:**  
𝑇 ∼ 𝑃(𝑇 ∣ Θ)  
**Scoring:**  
𝐸(𝑃,Θ,𝐷) = −𝐿(𝑇,𝐷) + λ ⋅ KL(𝑃 ∥ 𝑄)  
**Bifurcation Trigger:**  
If 𝐿(𝑇,𝐷) > δ or Entropy(𝑃) → 0, then fork Θ

---

## 🧪 II. StimLang as Causal Protocol

**Structure:**  
𝑆 = {(𝐼ₜ, 𝑂ₜ)} for t = 1..T  
𝐼ₜ: Intervention at time t  
𝑂ₜ: Output observed  

**Objective:**  
maxₛ Eₜ∼𝑃(𝑇 ∣ Θ)[Identifiability(𝐺ₜ ∣ 𝑆)]

---

## 🔗 III. Attribution as Causal Graph

**Graph Definition:**  
𝐺ₜ = (𝑉, 𝐸, 𝑤)  
V: Theory components  
E: Directed causal edges  
w(e): Estimated influence  

**Edge Weight Estimation:**  
w(vᵢ→O) ≈ E[O ∣ do(vᵢ=1)] − E[O ∣ do(vᵢ=0)]  

**Clarity Reward:**  
𝑅_clarity(𝑇) = (1/|𝐸|) ⋅ ∑ₑ∈𝐸 |𝑤(e)| / σ(𝑤)

---

## 🧬 IV. StimLang Modes

- **🔍 Clarification Mode:**  
  𝐺ₜ_fine = InferCausalGraph(𝑇, 𝑆_clarify, 𝐷)

- **🧪 Mutation Mode:**  
  𝑀* = SuggestMutationTargets(𝑇, 𝑆_mutate, 𝐷)

---

## 🧭 V. Dual Cognitive Modes + Control Switching

**Modes:**

| Mode Type | Options |
|-----------|---------|
| Processing | Creative Embedding / Structural Implementation |
| Control    | Bayesian Optimization / Evolutionary Reflex     |

**Control Policy:**  
Let:  
η = entropy  
R = agent resources  
Δ𝐿 = change in loss

Then:  
π(mode) =  
• Creative + BO if η > τ₁ ∧ R > ρ  
• Structural + BO if η ≤ τ₁ ∧ R > ρ  
• Creative + Evolution if η > τ₂ ∧ R ≤ ρ  
• Structural + Evolution otherwise

---

This defines the formal cognitive-evolutionary framework of Darwin: a layered, self-refining system that evolves not only solutions, but the generators of solutions, using causal reasoning and structured experimentation.
