#!/usr/bin/env python3
"""
Tower of Hanoi - Recursive Solution with Enhanced Graphics
===========================================================

A classic demonstration of recursion where disks must be moved from
source tower to destination tower following these rules:
1. Only one disk can be moved at a time
2. A disk can only be placed on top of a larger disk
3. Only the top disk of a tower can be moved

Author: Saksham Khalkho
Date: April 2026
Purpose: LFX Mentorship 2026 - Coding Challenge
"""

import sys
import time
import os


# ANSI Color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def clear_screen():
    """Clear the terminal screen for better visualization."""
    os.system('clear' if os.name != 'nt' else 'cls')


def get_disk_color(disk_size, max_disks):
    """
    Return color code based on disk size.
    Smaller disks get warmer colors, larger disks get cooler colors.
    """
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, 
              Colors.CYAN, Colors.BLUE, Colors.MAGENTA]
    return colors[disk_size % len(colors)]


def draw_disk(disk_size, max_size, color=True):
    """
    Draw a single disk with the given size.
    
    Args:
        disk_size: Size of the disk (1 to n)
        max_size: Maximum disk size in the puzzle
        color: Whether to use colors
    
    Returns:
        String representation of the disk
    """
    # Create the disk with brackets and number
    disk_width = disk_size * 2 + 1
    disk_display = f"[{'='*(disk_size-1)}{disk_size}{'='*(disk_size-1)}]"
    
    # Add color if enabled
    if color:
        disk_color = get_disk_color(disk_size, max_size)
        disk_display = f"{disk_color}{disk_display}{Colors.END}"
    
    # Center the disk
    padding = ' ' * (max_size - disk_size)
    return padding + disk_display + padding


def draw_towers(towers, n_disks, move_count=0):
    """
    Visualize the current state of all three towers.
    
    Args:
        towers: Dictionary containing the state of each tower
        n_disks: Total number of disks in the puzzle
        move_count: Current move number
    """
    clear_screen()
    
    # Title
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}🗼  TOWER OF HANOI - Recursive Solution  🗼{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}\n")
    
    # Move counter
    print(f"{Colors.BOLD}Move #{move_count}{Colors.END}  |  ", end="")
    print(f"Total Disks: {n_disks}  |  ", end="")
    print(f"Minimum Moves: {2**n_disks - 1}\n")
    
    # Calculate tower display width
    tower_width = n_disks * 2 + 3
    spacing = "    "
    
    # Draw tower labels at top
    tower_labels = ""
    for name in ['A', 'B', 'C']:
        label = f"{Colors.BOLD}{Colors.YELLOW}Tower {name}{Colors.END}"
        # Center the label
        label_padding = ' ' * ((tower_width - 7) // 2)
        tower_labels += label_padding + label + label_padding + spacing
    print(tower_labels)
    print()
    
    # Print each level from top to bottom
    for level in range(n_disks, 0, -1):
        line = ""
        for tower_name in ['A', 'B', 'C']:
            tower = towers[tower_name]
            
            if len(tower) >= level:
                # Get the disk at this level
                disk_size = tower[level - 1]
                line += draw_disk(disk_size, n_disks, color=True) + spacing
            else:
                # Empty space - show the pole
                pole = f"{Colors.WHITE}│{Colors.END}"
                padding = ' ' * n_disks
                line += padding + pole + padding + spacing
        
        print(line)
    
    # Print base platforms
    base_line = ""
    for _ in range(3):
        base = f"{Colors.BOLD}{'▬' * (n_disks * 2 + 1)}{Colors.END}"
        base_line += base + spacing
    print(base_line)
    
    # Print tower name labels at bottom
    label_line = ""
    for name in ['A', 'B', 'C']:
        label = f"{Colors.BOLD}{Colors.GREEN}{name}{Colors.END}"
        padding = ' ' * n_disks
        label_line += padding + label + padding + spacing
    print(label_line)
    
    print(f"\n{Colors.CYAN}{'─'*70}{Colors.END}\n")


def tower_of_hanoi(n, source, destination, auxiliary, towers, visualize=True, delay=0.8, move_count=[0]):
    """
    RECURSIVE SOLUTION to Tower of Hanoi problem.
    
    This function demonstrates RECURSION - a function calling itself with smaller
    subproblems until reaching the base case.
    
    RECURSION BREAKDOWN:
    --------------------
    Base Case: If n == 1, simply move the disk from source to destination
    
    Recursive Case (n > 1):
        1. Move (n-1) disks from source to auxiliary (using destination as temporary)
           This is a RECURSIVE CALL with a smaller problem
        
        2. Move the largest disk (nth disk) from source to destination
           This is the actual work at this recursion level
        
        3. Move (n-1) disks from auxiliary to destination (using source as temporary)
           This is another RECURSIVE CALL with a smaller problem
    
    Why recursion works here:
    -------------------------
    - Each recursive call solves a simpler version of the same problem
    - The base case (n=1) is trivial - just move one disk
    - Larger problems are broken down into smaller subproblems
    - The call stack keeps track of all pending operations
    
    Args:
        n: Number of disks to move
        source: Name of source tower ('A', 'B', or 'C')
        destination: Name of destination tower
        auxiliary: Name of auxiliary/helper tower
        towers: Dictionary tracking the current state of all towers
        visualize: Boolean to enable/disable visualization
        delay: Delay in seconds between moves for visualization
        move_count: List containing move counter (mutable for tracking)
    
    Returns:
        int: Total number of moves made
    """
    
    # BASE CASE: Only one disk to move
    # This is where recursion stops - no more recursive calls needed
    if n == 1:
        # Perform the actual move
        disk = towers[source].pop()
        towers[destination].append(disk)
        
        move_count[0] += 1
        
        # Display the move
        print(f"{Colors.BOLD}Move disk {Colors.YELLOW}{disk}{Colors.END} ", end="")
        print(f"from tower {Colors.CYAN}{source}{Colors.END} ", end="")
        print(f"to tower {Colors.GREEN}{destination}{Colors.END}")
        
        if visualize:
            draw_towers(towers, max(len(towers['A']) + len(towers['B']) + len(towers['C']), n), move_count[0])
            time.sleep(delay)
        
        return 1  # One move made
    
    # RECURSIVE CASE: More than one disk to move
    else:
        total_moves = 0
        
        # RECURSIVE STEP 1: Move (n-1) disks from source to auxiliary
        # We use destination as the temporary helper tower
        # This is a SMALLER subproblem (n-1 instead of n)
        total_moves += tower_of_hanoi(n - 1, source, auxiliary, destination, 
                                     towers, visualize, delay, move_count)
        
        # STEP 2: Move the largest disk (nth disk) from source to destination
        # This is the work done at THIS level of recursion
        disk = towers[source].pop()
        towers[destination].append(disk)
        
        move_count[0] += 1
        
        # Display the move
        print(f"{Colors.BOLD}Move disk {Colors.YELLOW}{disk}{Colors.END} ", end="")
        print(f"from tower {Colors.CYAN}{source}{Colors.END} ", end="")
        print(f"to tower {Colors.GREEN}{destination}{Colors.END}")
        
        if visualize:
            draw_towers(towers, max(len(towers['A']) + len(towers['B']) + len(towers['C']), n), move_count[0])
            time.sleep(delay)
        
        total_moves += 1  # Count this move
        
        # RECURSIVE STEP 3: Move (n-1) disks from auxiliary to destination
        # We use source as the temporary helper tower
        # Another SMALLER subproblem (n-1 instead of n)
        total_moves += tower_of_hanoi(n - 1, auxiliary, destination, source, 
                                     towers, visualize, delay, move_count)
        
        return total_moves


def main():
    """
    Main function to run the Tower of Hanoi demonstration.
    """
    clear_screen()
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}🗼  TOWER OF HANOI - Recursive Solution  🗼{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}\n")
    
    
    # Get number of disks from user
    try:
        if len(sys.argv) > 1:
            n_disks = int(sys.argv[1])
        else:
            n_disks = int(input(f"{Colors.YELLOW}Enter number of disks (3-6 recommended): {Colors.END}"))
        
        if n_disks < 1:
            print(f"{Colors.RED}Number of disks must be at least 1!{Colors.END}")
            return
        
        if n_disks > 7:
            print(f"{Colors.YELLOW}Warning: More than 7 disks will take a long time!{Colors.END}")
            confirm = input(f"Continue anyway? (y/n): ")
            if confirm.lower() != 'y':
                return
    
    except ValueError:
        print(f"{Colors.RED}Please enter a valid number!{Colors.END}")
        return
    
    # Initialize towers
    # Tower A starts with all disks (largest to smallest)
    # Towers B and C start empty
    towers = {
        'A': list(range(n_disks, 0, -1)),  # [n, n-1, ..., 2, 1]
        'B': [],
        'C': []
    }
    
    print(f"\n{Colors.BOLD}Solving Tower of Hanoi with {n_disks} disk(s){Colors.END}")
    print(f"{Colors.GREEN}Goal: Move all disks from Tower A to Tower C{Colors.END}\n")
    
    draw_towers(towers, n_disks, 0)
    
    input(f"{Colors.YELLOW}Press Enter to start the animation...{Colors.END}")
    
    # Solve the puzzle using RECURSION
    start_time = time.time()
    move_counter = [0]
    total_moves = tower_of_hanoi(n_disks, 'A', 'C', 'B', towers, 
                                 visualize=True, delay=0.6, move_count=move_counter)
    end_time = time.time()
    
    # Final summary
    clear_screen()
    print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}✓ PUZZLE SOLVED! ✓{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}{'='*70}{Colors.END}\n")
    
    draw_towers(towers, n_disks, total_moves)
    
    print(f"{Colors.BOLD}Statistics:{Colors.END}")
    print(f"  • Total moves made: {Colors.GREEN}{total_moves}{Colors.END}")
    print(f"  • Time taken: {Colors.CYAN}{end_time - start_time:.2f} seconds{Colors.END}\n")
    
    # Explain the recursion
    print(f"{Colors.BOLD}{Colors.CYAN}RECURSION EXPLANATION:{Colors.END}")
    print(f"{Colors.CYAN}{'─'*70}{Colors.END}")
    print(f"For {Colors.YELLOW}{n_disks}{Colors.END} disk(s), the recursive algorithm:")
    print(f"  1. {Colors.MAGENTA}Recursively{Colors.END} moved {n_disks-1} disk(s) from A to B (using C)")
    print(f"  2. Moved the {Colors.BOLD}largest disk{Colors.END} from A to C")
    print(f"  3. {Colors.MAGENTA}Recursively{Colors.END} moved {n_disks-1} disk(s) from B to C (using A)")
    print(f"\nThis pattern repeats at each recursion level, creating")
    print(f"a call tree with {Colors.YELLOW}{2**n_disks - 1}{Colors.END} total moves.")
    print(f"{Colors.CYAN}{'='*70}{Colors.END}\n")


if __name__ == "__main__":
    main()
