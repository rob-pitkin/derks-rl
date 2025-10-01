# Derk's RL

A learning project exploring different reinforcement learning algorithms for [Derk's Gym](https://gym.derkgame.com/), a MOBA RL environment.

## About

This repository implements and compares various RL algorithms to determine which performs best in Derk's Gym. Agents are implemented locally and then trained via a colab notebook for GPU access.

## Setup

This project uses Python 3.13+ and uv for dependency management.

```bash
# Install dependencies
uv sync

# Run the environment
uv run python src/main.py
```

## Current Status

Currently implements a basic random agent that samples actions from the action space.

## Environment

The project uses the `gym-derk` environment, which provides a multi-agent battle arena where teams of 3 compete against each other.
