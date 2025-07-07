![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/Project%20Status-Completed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Search Algorithms](https://img.shields.io/badge/Algorithms-DFS%2FBFS%2FUCS%2FA*-orange)

# 👾 Pacman Search AI — Implementing Search Algorithms

This project implements foundational AI search algorithms like DFS, BFS, UCS, and A* to control the movements of Pacman in various maze environments.

It is based on the classic CS188: Intro to AI (Berkeley) assignment to practice uninformed and informed search strategies.

---

## 📌 Algorithms Implemented

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search

Each algorithm is implemented inside `search.py` and tested via different agent behaviors in `searchAgents.py`.

---

## 📂 Project Structure

```
├── pacman.py               # Main game loop
├── search.py               # Core search algorithms (you implement here)
├── searchAgents.py         # Agents that use your algorithms
├── layouts/                # Different maze environments
├── graphicsDisplay.py      # Visualization for the game
├── autograder.py           # Used for grading / testing
├── util.py                 # Priority queues, stacks, etc.
```

---

## 🕹️ How to Run

```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=depthFirstSearch
```

Other examples:
```bash
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

---

## 📊 Evaluation

Use `autograder.py` to test the correctness and performance of your implementations:

```bash
python autograder.py
```

---

## 🎯 Learning Outcomes

- Understand core AI search strategies
- Implement and test pathfinding in grid environments
- Learn trade-offs between uninformed and informed search

---

## 👤 Author

Abdulrahman Zahir  
[GitHub Profile](https://github.com/abdulrahmanzahir)
