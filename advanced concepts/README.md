# Python Memory Management & Advanced Concepts

This repository uses real-world examples to explain how Python manages memory, data, and objects.

## 1. Stack vs Private Heap

Understanding where variables live is the first step in mastering memory management.

### The Stack (Static Memory)
- **What it is:** A special region of your computer's memory that stores temporary variables created by each function (including the main function).
- **Behavior:** It's a LIFO (Last In, First Out) data structure. When a function calls another, a new "frame" is pushed onto the stack. When the function returns, that frame is popped, and all its local variables are instantly forgotten.
- **What goes here:** 
  - Function references (call stack).
  - References (pointers) to objects.
  - *Note:* In languages like C/C++, primitives (int, float) live here. In Python, **everything** is an object, so the Stack mainly holds *references* to objects that live on the Heap.

### The Private Heap (Dynamic Memory)
- **What it is:** A large pool of memory used for dynamic allocation.
- **Behavior:** Objects are allocated here and stay until they are no longer needed (deleted or garbage collected).
- **What goes here:** 
  - **All Python objects** (integers, strings, lists, your custom objects, etc.).
  - If you say `x = 10`, the integer object `10` is created on the Heap, and the variable `x` on the Stack points to it.

---

## 2. Python's Memory Manager

Python automates memory management so you don't have to manually `malloc` and `free` like in C.

1.  **Reference Counting (The First Line of Defense):**
    - Every object keeps a count of how many references point to it.
    - When the count drops to 0, the memory is *immediately* freed.
    
2.  **Garbage Collector (The Second Line of Defense):**
    - Handles **Reference Cycles** (e.g., Object A points to B, and B points to A). Even if you delete external references, they still point to each other, so ref count is not 0.
    - Python's GC runs periodically to detect and clean up these isolated cycles.

---

## How to Run the Examples

1. **Reference Counting:** `python 01_ref_counting.py`
2. **Garbage Collection:** `python 02_garbage_collection.py`
3. **Shallow vs Deep Copy:** `python 03_shallow_vs_deep_copy.py`
4. **__slots__ Optimization:** `python 04_slots_optimization.py`
