# Neuroscience - Reinforcement Learning

This repository contains a Jupyter notebook implementing a reinforcement learning approach for a neuroscience-related task. The project demonstrates how neural networks and reinforcement learning can be applied to specific neuroscience problems to achieve efficient learning outcomes.

## Project Overview

The primary goal of this project is to develop and evaluate a reinforcement learning model capable of interacting with an environment to learn and improve its performance over time. The project focuses on the following concepts:

- **Deep Q-Learning (DQN)**: Implementing a DQN agent to interact with the environment and optimize rewards.
- **Target Q-Network**: Introducing a target Q-network to stabilize training by predicting target Q-values via regression.
- **Exploration vs Exploitation**: Balancing exploration and exploitation during training.
- **Performance Metrics**: Tracking the score and performance of the agent across multiple episodes.
- **Optimization**: Fine-tuning hyperparameters to achieve better learning performance.

## Files

- `Neuroscience_Project_99101705.ipynb`: Main Jupyter notebook containing the reinforcement learning code for the project.

## Key Concepts

- **Q-Learning**: A model-free reinforcement learning algorithm to find the best action to take given the current state.
- **DQN**: Deep Q-Network, a neural network used to approximate the Q-value function.
- **Replay Buffer**: Storing experiences from which the agent samples to improve learning efficiency.
- **Target Network**: A secondary neural network used to predict more stable Q-values for updating the main network.

## Requirements

- Python 3.8 or higher
- TensorFlow or PyTorch (depending on the framework used in the notebook)
- NumPy
- Matplotlib
- Jupyter Notebook
