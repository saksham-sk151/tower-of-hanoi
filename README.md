# Tower of Hanoi - Recursive Solution

**A Python implementation demonstrating recursion through the classic Tower of Hanoi puzzle**

Created for: **LFX Mentorship 2026 - Broadening the RISC-V High Precision Code Base and Reach**

## 🎯 Overview

This program solves the Tower of Hanoi puzzle using a **recursive algorithm**, demonstrating:
- **Recursion** - Function calling itself with smaller subproblems
- **Base case and recursive case** handling
- **Algorithm visualization** with ASCII graphics
- **Clear code documentation** and comments

## 🎮 Demo




## 🚀 Usage

### Run with default (interactive mode):
```bash
python3 tower_of_hanoi.py
```

### Run with specific number of disks:
```bash
python3 tower_of_hanoi.py 4
```

### Recommended:
- **3-4 disks**: Good for learning and visualization
- **5-6 disks**: Shows complexity well
- **7+ disks**: Gets slow due to visualization delays

## 📚 How It Works

### The Recursion Pattern

For `n` disks, the algorithm:

1. **Recursively** move `(n-1)` disks from source to auxiliary tower
2. Move the largest disk from source to destination
3. **Recursively** move `(n-1)` disks from auxiliary to destination

### Base Case
When `n = 1`, simply move the single disk directly.

### Why Recursion?
- Each step solves a **smaller version** of the same problem
- The problem **naturally decomposes** into subproblems
- Total moves: `2^n - 1` (proven mathematically)

## 🔍 Code Highlights

### Recursion Implementation
```python
def tower_of_hanoi(n, source, destination, auxiliary, towers):
    # BASE CASE: Only one disk to move
    if n == 1:
        # Move disk directly
        disk = towers[source].pop()
        towers[destination].append(disk)
        return 1
    
    # RECURSIVE CASE: Break problem into smaller parts
    else:
        # Step 1: Recursively move (n-1) disks to auxiliary
        tower_of_hanoi(n - 1, source, auxiliary, destination, towers)
        
        # Step 2: Move largest disk to destination
        disk = towers[source].pop()
        towers[destination].append(disk)
        
        # Step 3: Recursively move (n-1) disks to destination
        tower_of_hanoi(n - 1, auxiliary, destination, source, towers)
```

### Key Recursion Concepts Demonstrated

1. **Base Case**: `if n == 1` - Stops the recursion
2. **Recursive Case**: `n > 1` - Calls itself with smaller `n`
3. **Problem Decomposition**: Breaking `n` disks into `(n-1)` + 1 + `(n-1)`
4. **Call Stack**: Each recursive call waits for its sub-calls to complete

## 📊 Complexity Analysis

| Disks | Moves Required | Time Complexity |
|-------|----------------|-----------------|
| 3     | 7              | O(2³ - 1)       |
| 4     | 15             | O(2⁴ - 1)       |
| 5     | 31             | O(2⁵ - 1)       |
| n     | 2ⁿ - 1         | O(2ⁿ)           |

**Space Complexity**: O(n) - due to recursion call stack depth

## 🎓 Learning Points

### Recursion vs Iteration

This problem is **naturally recursive** because:
- Each step requires solving the same problem with fewer disks
- The solution has a clear recursive structure
- Base case (n=1) is trivial

**Iteration would require**:
- Explicit stack management
- More complex state tracking
- Less intuitive code

### Why This Demonstrates Recursion Well

✅ Clear base case and recursive case  
✅ Natural problem decomposition  
✅ Each recursive call solves a smaller problem  
✅ Demonstrates call stack depth  
✅ Shows exponential growth of recursive calls  

## 📁 Files

- `tower_of_hanoi.py` - Main program with fully commented recursion
- `README.md` - This file

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 📧 Author

**Saksham Khalkho**  
**Date**: April 2026  
**Purpose**: LFX Mentorship 2026 Coding Challenge

---

*This implementation emphasizes clear recursion demonstration with extensive comments explaining each recursive step.*
