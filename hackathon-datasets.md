# Datasets for the extreme QML hackathon

These are five open datasets for the hackathon. Four hold quantum data. The
fifth holds classical data computed from quantum mechanics.

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
