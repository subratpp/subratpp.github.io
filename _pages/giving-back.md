---
layout: archive
title: "Giving Back"
permalink: /giving-back/
author_profile: true
redirect_from:
  - /giving
---

{% include base_path %}

Giving Back
======

- **RLFT**  
  A lightweight research-oriented project built on **nanoGPT** (Andrej Karpathy) to study reinforcement learning–based fine-tuning on a controlled toy setting.  
  The model is trained on a **digit arithmetic task**, where:
  - **Addition** is learned via supervised fine-tuning.
  - **Subtraction** is improved using **Group Relative Policy Optimization (GRPO)**.
  
  The project further analyzes **token embedding geometry** before and after GRPO-based fine-tuning to investigate whether **emergent structure or behavior** arises in the latent space, particularly from supervised learning on addition alone.

  Code and experiments: https://github.com/subratpp/rlft
