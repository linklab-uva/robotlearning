---
layout: page
title: Syllabus
permalink: /syllabus/
---

## Course Syllabus

The course is organized around four questions: **How should a robot represent uncertain state? How should it make sequential decisions? How can it learn behavior from data and experience? How do these ideas appear in modern robot-learning systems?**

The first three modules develop the mathematical foundations in depth. The final module deliberately connects those foundations to contemporary robot learning rather than treating recent methods as a separate vocabulary.

PDF copy of the syllabus [PDF](/docs/syllabus.pdf){:target="_blank"}

### Module 1: Estimation and Reasoning Under Uncertainty (~11 lectures)
- Background on probability
- Topics: Markov chains, Hidden Markov Models, Kalman Filter, Extended and Unscented Kalman Filter, particle filters, occupancy grids, rigid transformations
- **Core question:** What should the robot believe about the state of the world, and how should that belief change as new observations arrive?

### Module 2: Sequential Decision-Making, Control, and Planning (~6 lectures)
- Background on linear control and dynamic programming
- Topics: Markov Decision Processes, Bellman equation, Value and Policy Iteration, Linear Quadratic Regulator, Linear Quadratic Gaussian control, Iterative LQR, sampling-based motion planning
- **Core question:** Given a model of the world, how should a robot choose actions over time?

### Module 3: Learning to Act (~7 lectures)
- Background on optimization and deep learning
- Topics: Imitation Learning, Policy Gradient methods, Q-Learning, Inverse RL, Model-Based RL, Offline RL, Deep RL
- **Core question:** When the model or the desired behavior is not known explicitly, how can a robot learn a useful policy from demonstrations, interaction, or previously collected data?

### Module 4: From Robot Learning to Modern Embodied AI (~1-2 lectures)
- Topics: generalization and Sim2Real, meta-learning/adaptation, generative robot policies, robot foundation models, vision-language-action models, and world models
- **Core question:** Which parts of the classical robot-learning stack are being replaced, which are being learned, and which remain fundamentally the same?
- This module is intended as a conceptual bridge. The emphasis is on understanding how the foundations from Modules 1–3 reappear in current systems, not on surveying every recent model.

## Tentative schedule

| Lecture      | Topic | Notes    |
| :---        |    :-------   |         :------ |
| 1     | Introduction      | HW 0 out (not graded)  |
| 2  |  Background on probability |  HW 1 out |
| 3   |  Markov Chains |   |
| 4   | Hidden Markov Models I   |   |
| 5   | Hidden Markov Models II  |   |
| 6   | Kalman Filter  | HW 1 due  |
| 7   | Extended Kalman Filter  |     |
| 8   | Unscented Kalman Filter  | HW 2 out  |
| 9   | Particle Filter  |   |
| 10   | Rigid Transforms, Quaternions  |   |
| 11   | Occupancy Grids  |  Summary on Lec 4-10 |
| 12   | Dynamic Programming, Bellman Equation  |  HW 2 Due |
| 13   | Value Iteration  |   |
| 14   | Policy iteration  |  HW 3 out |
| 15   | Background on Linear Control, LQR  |   |
| 16   | LQG, Iterated LQR  |   |
| 17   | Midterm  |   |
| 18   | Sampling Based Motion Planning  | HW 3 Due  |
| 19   | Optimization, Imitation Learning  |   |
| 20   | Policy Gradient  |   |
| 21   | Tabular Q-Learning  |   |
| 22   | Continuous Q-Learning  | HW 4 out  |
| 23   | Inverse RL, Model-based RL  |   |
| 24   | Offline RL  |   |
| 25   |  Deep RL | HW 4 due   |
| 26   |  Closing topics |  |
