---
title: 'Interpretable Reinforcement Learning'
date: 2023-05-01
permalink: /posts/2023/05/blog-post-irl/
tags:
  - Reinforcement Learning
  - Interpretability
  - Explainability
  - Explainable AI
---

Contents are reused from <cite>Interpretable Machine Learning by Christoph Molnar</cite>. Please visit the [original source](https://christophm.github.io/interpretable-ml-book/) for more details.


1.What is Interpretability?
------
Interpretability refers to how much a human can understand a model's behavior [2]. An interpretable model can be represented as a simple mathematical equation or a decision tree (DT), which shows how the model makes its predictions. If a model can be represented as a polynomial equation or a DT, it is considered interpretable.

However, some researchers only consider a model to be interpretable if it can be easily understood by humans. For example, a small decision tree with 10 nodes is interpretable because a person can follow the steps and see how the model makes its predictions. On the other hand, a large DT with 1000 nodes is not considered interpretable because it becomes too complex for humans to understand.

In this blog, we will focus on the broader definition of interpretability, which is that a model can be considered interpretable if it can be represented as a decision tree or a concise equation, even if it is lengthy.


2.Interpretability vs Explainability
------
Interpretable models are actually "white-box models" because they provide a clear understanding of how the model works. However, explainability is different from interpretability in that it refers to the ability to explain how the model behaves after it has been trained.

For example, let's say we train a neural network to classify images. The model's behavior is not immediately apparent just by looking at the network architecture. To explain how the model works, we can examine the weights of the neurons in the network. By doing this, we can see which features of the image are most important for the model's predictions.

This type of explanation is known as "post-hoc explainability," which means that we can explain how the model behaves after it has already been trained. This approach can be useful in situations where we want to understand the model's behavior or improve its performance, but it doesn't provide the same level of understanding as an interpretable model.

The following techniques are commonly used for post-training explainability, but will not be discussed in this blog:

1. Feature Visualization: This technique enables us to visualize the features learned by a neural network, and can include methods such as Saliency Maps, Feature Importance, Partial Dependence Plots (PDPs), Individual Conditional Expectation (ICE) plots, Local Interpretable Model-Agnostic Explanations (LIME), Gradient Analysis, and more.

2. Model Distillation: This technique involves training a smaller model to mimic the behavior of a larger, more complex model. Examples of this technique include Knowledge Distillation, Model Compression, and Model Pruning. The goal is to create a smaller model that is _interpretable_, meaning it can be represented as a decision tree or concise equation.

3. Training Sample Importance: This technique allows us to identify the most important training samples that led to a particular decision.


3.Interpretable Models
------

Follwoing are the two main approaches for creating interpretable models:

1. Decision Trees: The nodes of the decision tree determine which path should be taken to reach a particular leaf node. Examples of decision trees include Binary Decision Trees, Decision Rules (Non-binary DT), and RuleFit (DT leaf node representation).

2. Function Decomposition: This technique involves representing a complex function as a sum of simpler functions. Examples of this include Linear Regression, Additive Models, Generalized Additive Models (GAMs), and Generalized Linear Models (GLMs), which are all considered interpretable.



4.Interpretable Reinforcement Learning
-----

coming soon!
{: .notice}

References
------
[1] Christoph Molnar. Interpretable Machine Learning. A Guide for Making Black Box Models Explainable. 2019. https://christophm.github.io/interpretable-ml-book/.

[2] Miller, Tim. “Explanation in artificial intelligence: Insights from the social sciences.” arXiv Preprint arXiv:1706.07269. (2017).
