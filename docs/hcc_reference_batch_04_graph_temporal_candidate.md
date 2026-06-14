# HCC Reference Batch 04: Graph-Temporal Learning, Transformers, GNNs, and Sequence Baselines

## Status

Candidate reference batch for TRUST-Swarm High-Confidence Computing submission.

Do not insert directly into the final manuscript until each item is checked for:
- exact author names
- official venue
- year
- DOI or stable publisher URL
- relevance to the exact sentence being cited

## A. Transformer and Attention Models

[R51] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention Is All You Need,” in Advances in Neural Information Processing Systems, vol. 30, 2017.

[R52] D. Bahdanau, K. Cho, and Y. Bengio, “Neural Machine Translation by Jointly Learning to Align and Translate,” in International Conference on Learning Representations, 2015.

## B. Graph Neural Networks

[R53] T. N. Kipf and M. Welling, “Semi-Supervised Classification with Graph Convolutional Networks,” in International Conference on Learning Representations, 2017.

[R54] P. Veličković, G. Cucurull, A. Casanova, A. Romero, P. Liò, and Y. Bengio, “Graph Attention Networks,” in International Conference on Learning Representations, 2018.

[R55] W. L. Hamilton, R. Ying, and J. Leskovec, “Inductive Representation Learning on Large Graphs,” in Advances in Neural Information Processing Systems, 2017.

## C. Temporal Graph and Spatio-Temporal Learning

[R56] E. Rossi, B. Chamberlain, F. Frasca, D. Eynard, F. Monti, and M. Bronstein, “Temporal Graph Networks for Deep Learning on Dynamic Graphs,” arXiv:2006.10637, 2020.

[R57] L. Zhao, Y. Song, C. Zhang, Y. Liu, P. Wang, T. Lin, M. Deng, and H. Li, “T-GCN: A Temporal Graph Convolutional Network for Traffic Prediction,” arXiv:1811.05320, 2018.

[R58] A. Longa, V. Lachi, G. Santin, M. Bianchini, B. Lepri, P. Liò, F. Scarselli, and A. Passerini, “Graph Neural Networks for Temporal Graphs: State of the Art, Open Challenges, and Opportunities,” arXiv:2302.01018, 2023.

[R59] Candidate needed: peer-reviewed spatio-temporal GNN survey or journal paper. Use for graph-temporal modeling discussion if stronger than arXiv.

## D. Sequence Baselines

[R60] S. Hochreiter and J. Schmidhuber, “Long Short-Term Memory,” Neural Computation, vol. 9, no. 8, pp. 1735–1780, 1997.

[R61] K. Cho, B. van Merriënboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, and Y. Bengio, “Learning Phrase Representations Using RNN Encoder-Decoder for Statistical Machine Translation,” in Proceedings of EMNLP, 2014.

[R62] J. Chung, C. Gulcehre, K. Cho, and Y. Bengio, “Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling,” arXiv:1412.3555, 2014.

[R63] S. Bai, J. Z. Kolter, and V. Koltun, “An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling,” arXiv:1803.01271, 2018.

## E. Where to Use These References

- R51–R52: Transformer encoder and attention mechanism background.
- R53–R55: graph neural network and graph attention motivation.
- R56–R59: graph-temporal / dynamic graph learning.
- R60–R63: LSTM, GRU, and CNN/TCN sequence baseline justification.

## Manuscript Integration Notes

Use this batch to support:

1. the GraphTemporalTransformer model design,
2. comparison against LSTM, GRU, and CNN1D baselines,
3. the need to model both UAV-node relations and temporal mission evolution,
4. the architecture ablation where removing UAV-node attention and temporal transformer components reduces macro F1.

Final manuscript should explain that TRUST-Swarm uses graph-temporal reasoning for high-confidence mission-state recognition, while assurance modules add calibration, OOD testing, explainability, and recovery support.
