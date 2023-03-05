# Lab assignments for Introduction to Data-Centric AI

This repository contains the lab assignments for the [Introduction to
Data-Centric AI](https://dcai.csail.mit.edu/) class.

Contributions are most welcome! If you have ideas for improving the labs,
please open an issue or submit a pull request.

For more hands-on experience with techniques taught in this class, participate in the
[Data-centric AI Competition 2023](https://machinehack.com/tournaments/data_centric_ai_competition_2023).

## [Lab 1: Data-Centric AI vs. Model-Centric AI][lab-1]

The [first lab assignment][lab-1] walks you through an ML task of building a
text classifier, and illustrates the power (and often simplicity) of
data-centric approaches.

[lab-1]: data_centric_model_centric/Lab%20-%20Data-Centric%20AI%20vs%20Model-Centric%20AI.ipynb

## [Lab 2: Label Errors][lab-2]

[This lab][lab-2] guides you through writing your own implementation of
automatic label error identification using Confident Learning, the technique
taught in [today’s lecture][lec-2].

[lab-2]: label_errors/Lab%20-%20Label%20Errors.ipynb
[lec-2]: https://dcai.csail.mit.edu/lectures/label-errors/

## [Lab 3: Dataset Creation and Curation][lab-3]

[This lab assignment][lab-3] is to analyze an already collected dataset labeled
by multiple annotators.

[lab-3]: dataset_curation/Lab%20-%20Dataset%20Curation.ipynb

## [Lab 4: Data-centric Evaluation of ML Models][lab-4]

[This lab assignment][lab-4] is to try improving the performance of a given
model solely by improving its training data via some of the various strategies
covered here.

[lab-4]: data_centric_evaluation/Lab%20-%20Data-Centric%20Evaluation.ipynb

## [Lab 5: Class Imbalance, Outliers, and Distribution Shift][lab-5]

[The lab assignment][lab-5] for this lecture is to implement and compare
different methods for identifying outliers. For this lab, we've focused on
anomaly detection. You are given a clean training dataset consisting of many
pictures of dogs, and an evaluation dataset that contains outliers (non-dogs).
Your task is to implement and compare various methods for detecting these
outliers. You may implement some of the ideas presented in [today's
lecture][lec-5], or you can look up other outlier detection algorithms in the
linked references or online.

[lab-5]: outliers/Lab%20-%20Outliers.ipynb
[lec-5]: https://dcai.csail.mit.edu/lectures/imbalance-outliers-shift/

## [Lab 6: Growing or Compressing Datasets][lab-6]

[This lab][lab-6] guides you through an implementation of active learning.

[lab-6]: growing_datasets/Lab%20-%20Growing%20Datasets.ipynb

## [Lab 7: Interpretability in Data-Centric ML][lab-7]

[This lab][lab-7] guides you through finding issues in a dataset’s features by
applying interpretability techniques.

[lab-7]: interpretable_features/Lab%20-%20Interpretable%20Features.ipynb

## [Lab 8: Encoding Human Priors: Data Augmentation and Prompt Engineering][lab-8]

[This lab] guides you through prompt engineering, crafting inputs for large
language models (LLMs). With these large pre-trained models, even small amounts
of data can make them very useful. This lab is also [available on
Colab][lab-8-colab].

[lab-8]: prompt_engineering/Lab_Prompt_Engineering.ipynb
[lab-8-colab]: https://colab.research.google.com/drive/1cipH-u6Jz0EH-6Cd9MPYgY4K0sJZwRJq

## [Lab 9: Data Privacy and Security][lab-9]

The [lab assignment][lab-9] for this lecture is to implement a membership
inference attack. You are given a trained machine learning model, available as
a black-box prediction function. Your task is to devise a method to determine
whether or not a given data point was in the training set of this model. You
may implement some of the ideas presented in [today’s lecture][lec-9], or you
can look up other membership inference attack algorithms.


[lab-9]: membership_inference/Lab%20-%20Membership%20Inference.ipynb
[lec-9]: https://dcai.csail.mit.edu/lectures/data-privacy-security/

## License

Copyright (c) by the instructors of Introduction to Data-Centric AI (dcai.csail.mit.edu).

dcai-lab is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

dcai-lab is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See [GNU Affero General Public LICENSE](https://github.com/dcai-course/dcai-lab/blob/master/LICENSE.txt) for details.

