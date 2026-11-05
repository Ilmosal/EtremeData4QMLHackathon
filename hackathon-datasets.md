# Datasets for the extreme QML hackathon

These are twelve open datasets for the hackathon. Only the first five are
quantum focused. Datasets 1 to 4 hold quantum data, and dataset 5 holds
classical data computed from quantum mechanics. Datasets 6 to 12 are classical
datasets. Each has a property that makes it hard to learn from, such as
extreme class imbalance, graph structure, few samples or strong symmetries.

## 1. Google Quantum AI surface code experiments (real hardware)

Google published the raw data from its Willow error correction experiment on
Zenodo. The data comes from surface code and repetition code memory runs on a
105-qubit chip, at code distances 3, 5 and 7. Each sample is a set of
stabilizer measurements taken over many rounds. A detection event marks a
change in one measure qubit's result between two rounds. The task is to
predict the logical error from those detection events. Logical errors happen
in about 0.14% of cycles at distance 7, so the positive class is tiny.
AlphaQubit trained on this kind of data. Older sets from the 2022 Sycamore
surface code work and the 2024 dynamic surface code work are on Zenodo too.

**Fit:** rare events, extreme class imbalance, time series, graph structure
(the decoding graph).

**Links:**
- [Zenodo 13273331: Willow surface code data](https://zenodo.org/records/13273331)
- [Zenodo 6804040: 2022 Sycamore surface code data](https://zenodo.org/records/6804040)
- [Zenodo 14238907: dynamic surface codes data](https://zenodo.org/records/14238907)
- [arXiv 2408.13687: QEC below the surface code threshold](https://arxiv.org/abs/2408.13687)

## 2. QDataSet (simulated qubit control and noise)

QDataSet has 52 datasets from simulations of one- and two-qubit systems. Some
systems evolve under noise and some do not. Each sample holds control pulse
sequences, the time evolution they cause, and the measurement results. Tasks
include quantum control, tomography, and learning the noise. The full set is
about 14 TB compressed, so teams should pick one or two subsets. The
repository includes the simulation code and example notebooks.

**Fit:** time series, high dimensions.

**Links:**
- [QDataSet on GitHub](https://github.com/eperrier/QDataSet)
- [QDataSet paper, Scientific Data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9508231/)

## 3. PennyLane spin systems (`qspin`)

PennyLane hosts ground-state data for spin models: transverse-field Ising, XXZ
Heisenberg, Fermi-Hubbard and Bose-Hubbard. Each model comes on 1D chains and
2D rectangular lattices, with open or periodic boundaries. Each entry holds
the Hamiltonian, the ground state, the ground energy, phase labels and order
parameters. Entries also hold classical shadow measurements, so teams can
learn from measurements instead of full state vectors. One possible task is to
classify quantum phases across a phase transition. `qml.data.load("qspin", ...)`
downloads the data in one line. Run
`qml.data.list_attributes(data_name="qspin")` to see the full attribute list.

**Fit:** strong symmetries (translation, spin flip, U(1)), graph structure
(the lattice).

**Links:**
- [PennyLane Datasets](https://pennylane.ai/datasets)
- [Introducing PennyLane Datasets](https://pennylane.ai/blog/2023/08/introducing-pennylane-datasets/)

## 4. MNISQ (classical images as quantum circuits)

MNISQ turns MNIST, Fashion-MNIST and Kuzushiji-MNIST into quantum circuits.
Each image's pixels are mapped into the amplitudes of a quantum state. The set has
4.95 million circuits in 9 subsets, at about 90% fidelity to the target
states. Each circuit comes in two forms: one you run on a simulator, and a
QASM text form for classical sequence models. The authors report 97% accuracy
with quantum kernels. This set shows how much the choice of encoding changes
the result.

**Fit:** high dimensions. You can also make it imbalanced on purpose by
removing most samples of one class, etc.

**Links:**
- [MNISQ paper, arXiv 2306.16627](https://arxiv.org/abs/2306.16627)
- [MNISQ on PennyLane](https://pennylane.ai/datasets/mnisq)

## 5. QM9 (classical data from quantum chemistry)

QM9 holds about 134,000 small organic molecules made of C, H, O, N and F. DFT
calculations give each molecule's geometry and 12 quantum properties, such as
the HOMO-LUMO gap and the dipole moment. Each molecule is a graph: atoms are
nodes and bonds are edges. Most machine learning libraries (PyTorch Geometric,
DeepChem) load it in one call. QM9 suits teams that want to compare a quantum
graph model with a classical graph neural network on a well-known benchmark.

**Fit:** graph structure, symmetries (rotation and permutation invariance).

**Links:**
- QM9 ships with PyTorch Geometric and DeepChem.

## 6. Credit Card Fraud Detection (ULB)

This set holds 284,807 card transactions made by European cardholders over
two days in September 2013. Only 492 of them are fraud, a positive rate of
about 0.17%. For privacy, 28 of the 30 features are PCA components (V1 to
V28). The other two are the time and the transaction amount. The task is to
flag the fraud cases. Plain accuracy is useless here: a model that never
predicts fraud scores 99.8%. Use precision-recall curves or AUPRC instead.

**Fit:** extreme class imbalance, rare events.

**Links:**
- [Kaggle: Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## 7. Cora and CiteSeer (citation networks)

Cora and CiteSeer are small citation graphs. Each node is a paper and each
edge is a citation. Each node has a binary bag-of-words vector, and the task
is to predict the paper's topic. Cora has 2,708 papers in 7 classes, with
1,433 word features. CiteSeer has 3,312 papers in 6 classes, with 3,703 word
features. The standard split trains on only 20 labeled nodes per class, so
the task is semi-supervised. Both load in one call from PyTorch Geometric
(`Planetoid`) or DGL.

**Fit:** graph structure, small N, few labels, high dimensions (sparse word
features).

**Links:**
- [LINQS datasets](https://linqs.org/datasets/)
- [PyTorch Geometric Planetoid](https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Planetoid.html)

## 8. MoleculeNet subsets (BBBP, Tox21)

MoleculeNet is a benchmark collection for molecular machine learning. Each
molecule comes as a SMILES string, which converts to a graph: atoms are nodes
and bonds are edges. BBBP has about 2,000 molecules with a binary label for
whether the molecule crosses the blood-brain barrier. Tox21 has about 7,800
molecules with 12 binary toxicity labels. Most Tox21 labels are negative and
some are missing. Both sets are small enough to subsample for a quantum
prototype. DeepChem loads them with `dc.molnet.load_bbbp()` and
`dc.molnet.load_tox21()`.

**Fit:** graph structure, small N, class imbalance (Tox21), symmetries
(permutation invariance).

**Links:**
- [MoleculeNet](https://moleculenet.org/datasets-1)
- [MoleculeNet paper, arXiv 1703.00564](https://arxiv.org/abs/1703.00564)

## 9. Gene expression and single-cell RNA-seq

Gene expression data measures how active each gene is in a sample. Bulk data
has one profile per tissue sample. Single-cell RNA-seq has one profile per
cell. Both have tens of thousands of genes as features. Bulk studies often
have only tens to hundreds of samples, and only a few genes carry the signal.
Single-cell data has more samples but is very sparse, since most counts are
zero. Typical tasks are classifying disease or cell type. Scanpy loads small
example sets in one call, for example `sc.datasets.pbmc3k()` (2,700 blood
cells).

**Fit:** high dimensions, low N, sparse signal.

**Links:**
- [NCBI Gene Expression Omnibus (GEO)](https://www.ncbi.nlm.nih.gov/geo/)
- [CZ CELLxGENE](https://cellxgene.cziscience.com/)
- [Scanpy datasets](https://scanpy.readthedocs.io/en/stable/api/datasets.html)

## 10. Materials Project (crystal structures)

The Materials Project holds computed data for over 150,000 inorganic
materials. Each entry has a crystal structure (a periodic lattice of atoms)
and DFT properties such as the band gap, the formation energy and the elastic
constants. A crystal's properties do not change under rotation, translation,
reordering of atoms, or the operations of its space group. A model should
respect these symmetries. The API needs a free key. Matbench offers ready
subsets with fixed splits, some with only a few hundred samples.

**Fit:** strong symmetries (space groups, rotation, translation,
permutation), graph structure (the crystal graph).

**Links:**
- [Materials Project](https://next-gen.materialsproject.org/)
- [Matbench](https://matbench.materialsproject.org/)

## 11. KDD Cup 99 (network intrusion detection)

KDD Cup 99 holds records of network connections from a simulated military
network. Each record has 41 features, such as duration, protocol and bytes
sent. Each record is labeled normal or as one of 22 attack types, grouped into
four categories: DoS, probe, R2L and U2R. DoS attacks dominate the data, but
U2R and R2L attacks are very rare. U2R has only 52 records in the 10% training
subset. The set has many duplicate records. NSL-KDD is a cleaned version.
`sklearn.datasets.fetch_kddcup99()` downloads it in one call.

**Fit:** rare events, anomalies, extreme class imbalance (rare attack types).

**Links:**
- [UCI: KDD Cup 1999 Data](https://archive.ics.uci.edu/dataset/130/kdd+cup+1999+data)
- [NSL-KDD](https://www.unb.ca/cic/datasets/nsl.html)

## 12. IBM Transactions for Anti-Money Laundering (AML)

IBM built this set with a simulator of a virtual world in which people,
companies and banks trade with each other and some agents launder money. The
data is synthetic, so every laundering transaction has a true label, which
real bank data never has. Each record is one transfer, with a timestamp, the
sending and receiving bank and account, the amount, the currency and the
payment format. The accounts form a large directed graph, and the task is to
label each edge (transaction) as laundering or not. Laundering follows known
patterns such as fan-in, fan-out, cycles and scatter-gather, and the patterns
files list them. The set comes in six versions: Small, Medium and Large, each
with a higher (HI) or lower (LI) share of illicit transactions. HI-Small
holds about 5 million transactions, of which about 0.1% are laundering. The
Large sets hold more than 175 million, so teams should start with a Small set
or a subgraph.

**Fit:** graph structure (the transaction graph), extreme class imbalance,
rare events, time series.

**Links:**
- [Kaggle: IBM Transactions for Anti Money Laundering](https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml)
- [Paper, arXiv 2306.16424: Realistic Synthetic Financial Transactions for AML Models](https://arxiv.org/abs/2306.16424)
- [IBM Multi-GNN baseline code](https://github.com/IBM/Multi-GNN)
