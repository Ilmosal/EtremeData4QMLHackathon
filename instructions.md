# Challenge: Data-Centric Quantum Machine Learning

## Goal
Most QML work starts from a model and applies it to a convenient dataset. In this challenge, you start from the data. Pick a dataset with a challenging property, then argue which quantum approach could exploit that property and why.

## Tasks
1. **Choose a dataset with a challenging property.** Use one of the starter datasets below or bring your own, including data from your own research.
2. **Describe the challenge.** State what makes this data hard or interesting to learn from, for example graph structure, extreme class imbalance, very few samples, high dimensionality with sparse signal, or strong symmetries.
3. **Argue for a quantum model or technique.** Explain how it addresses the challenge. You can use an existing model or design your own. The argument matters more than the novelty of the model.
4. **Build a small prototype.** Implement it with classical simulation of quantum circuits to show feasibility. A full benchmark is not required. Purely theoretical work is also accepted.
5. **Connect to the real world.** Explain where data with this property occurs and why it matters.

## Guidelines
- Avoid applying a generic variational circuit to a generic dataset without engaging with the data's properties.
- You do not need to beat classical baselines. Focus on mechanistic arguments such as sample complexity, generalization bounds, kernel alignment, expressivity, qubit or memory efficiency, and symmetry-based inductive bias.

## Starter Datasets

| Property | Dataset | Link |
|---|---|---|
| Extreme class imbalance | Credit Card Fraud Detection (ULB, ~0.17% positive rate) | [link](TODO) |
| Graph-structured, small N | Cora / Citeseer citation networks | [link](TODO) |
| Graph-structured, small N | MoleculeNet subsets (BBBP, Tox21) | [link](TODO) |
| High-dimensional, low N | Gene expression / single-cell RNA-seq | [link](TODO) |
| Strong symmetry / invariance | Materials Project subsets (crystal structures) | [link](TODO) |
| Rare events / anomalies | KDD Cup 99 network intrusion detection | [link](TODO) |

## Deliverables
- Slides and a 5 minute presentation, with short Q&A.

## Judging Criteria
1. **Theoretical grounding:** Specific, mechanistic arguments score higher than general claims such as "quantum is exponentially faster."
2. **Novelty and creativity**
3. **Quality of presentation**
