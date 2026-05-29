# Dijkstra Algorithm using Python

This project implements Dijkstra’s Algorithm to find the shortest distance between cities in a graph.

## Files

* `dijkstra.py` → Main Python program
* `cities.txt` → Input file containing city connections and distances

## Input Format

Each line in `cities.txt` should be:

```text
City1 City2 Distance
```

Example:

```text
Delhi Mumbai 1400
Mumbai Chennai 1200
```

## How to Run

```bash
python dijkstra.py
```

Enter the starting city when prompted.

## Features

* Reads graph from file
* Uses Dijkstra’s shortest path algorithm
* Displays shortest distance from source city to all cities

## Requirements

* Python 3.x
