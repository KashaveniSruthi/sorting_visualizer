#  Sorting Visualizer (Python + Tkinter)

A simple desktop application built with **Python** and **Tkinter** that visually demonstrates how different sorting algorithms work. Instead of just displaying the final sorted output, the application animates every swap, making it easier to understand how each algorithm arranges the data step by step.

This project is a great way to learn sorting algorithms through visualization and also serves as a beginner-friendly GUI project using Python.

---

## Features

* Visual representation of sorting algorithms using animated bars
* Random data generation with a **Shuffle** button
* Step-by-step animation of each sorting process
* Simple and easy-to-use graphical interface
* Highlights the smallest and largest values using different colors
* Built entirely with Python's built-in Tkinter library

---

## Sorting Algorithms Included

### Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them whenever they are in the wrong order. The process continues until the list becomes sorted.

**Time Complexity**

* Best Case: **O(n)**
* Average Case: **O(n²)**
* Worst Case: **O(n²)**

---

### Selection Sort

Selection Sort finds the smallest element from the unsorted portion of the list and places it at its correct position during each iteration.

**Time Complexity**

* Best Case: **O(n²)**
* Average Case: **O(n²)**
* Worst Case: **O(n²)**

---

### Insertion Sort

Insertion Sort builds the sorted portion one element at a time by inserting each element into its correct position.

**Time Complexity**

* Best Case: **O(n)**
* Average Case: **O(n²)**
* Worst Case: **O(n²)**

---

## Technologies Used

* Python 3
* Tkinter (GUI)
* Random Module

---

## Project Structure

```text
Sorting-Visualizer/
│
├── sorting_visualizer.py
├── README.md
└── screenshots/
    ├── home.png
    ├── bubble_sort.png
    ├── selection_sort.png
    └── insertion_sort.png
```

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/KashaveniSruthi/sorting-visualizer.git
```

### 2. Navigate to the project folder

```bash
cd sorting-visualizer
```

### 3. Run the application

```bash
python sorting_visualizer.py
```

> Make sure Python 3 is installed on your system. No external libraries are required.

---

## How to Use

1. Run the program.
2. Click **Shuffle** to generate a new set of random bars.
3. Choose one of the available sorting algorithms:

   * Bubble Sort
   * Selection Sort
   * Insertion Sort
4. Watch the animation as the bars are sorted step by step.

---

## Screenshots


### Home Screen


![Sorting Visualizer](https://github.com/KashaveniSruthi/sorting_visualizer/blob/main/sorting_visualizer.png)


### Bubble Sort

![Bubble sort](https://github.com/KashaveniSruthi/sorting_visualizer/blob/main/bubble_sort.png)

### Selection Sort


![Selection sort](https://github.com/KashaveniSruthi/sorting_visualizer/blob/main/selection_sort.png)

### Insertion Sort


![Insertion_sort](https://github.com/KashaveniSruthi/sorting_visualizer/blob/main/insertion_sort.png)

---

## What I Learned

While building this project, I learned how to:

* Create desktop GUI applications using Tkinter
* Implement Bubble Sort, Selection Sort, and Insertion Sort
* Animate sorting operations using generators
* Work with Tkinter Canvas to draw and move graphical objects
* Use Python's event loop (`after()`) to create smooth animations
* Organize code into reusable functions for better readability

---

## Future Improvements

Some features that can be added in future versions include:

* Merge Sort visualization
* Quick Sort visualization
* Heap Sort visualization
* Adjustable animation speed
* Pause and Resume functionality
* Sorting statistics (comparisons and swaps)
* User-controlled array size
* Dark mode interface
* Color highlighting for comparisons and sorted elements

---
