#!/usr/bin/env python3

import os
import re
import ast

def analyze_python_code(code):
    """Analyze Python code to extract information about data structures, variables, and approach"""
    try:
        tree = ast.parse(code)
        analysis = {
            'variables': [],
            'data_structures': [],
            'functions': [],
            'complexity_hints': [],
            'imports': []
        }
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                analysis['functions'].append(node.name)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    analysis['imports'].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                analysis['imports'].append(f"{node.module}.{node.names[0].name}" if node.names else node.module)
        
        # Look for common patterns in the code
        code_lower = code.lower()
        if 'dp' in code_lower or 'dynamic' in code_lower:
            analysis['complexity_hints'].append('dynamic_programming')
        if 'left' in code_lower and 'right' in code_lower:
            analysis['complexity_hints'].append('two_pointers')
        if 'stack' in code_lower or '.append(' in code and '.pop(' in code:
            analysis['complexity_hints'].append('stack')
        if 'queue' in code_lower or 'deque' in code_lower:
            analysis['complexity_hints'].append('queue')
        if 'set(' in code or 'dict(' in code or '{' in code:
            analysis['complexity_hints'].append('hash_table')
        if 'sort' in code_lower:
            analysis['complexity_hints'].append('sorting')
        if 'head' in code_lower and 'next' in code_lower:
            analysis['complexity_hints'].append('linked_list')
        if 'root' in code_lower and ('left' in code_lower or 'right' in code_lower):
            analysis['complexity_hints'].append('binary_tree')
        if 'visited' in code_lower or 'dfs' in code_lower or 'bfs' in code_lower:
            analysis['complexity_hints'].append('graph_traversal')
        
        return analysis
    except:
        return {'variables': [], 'data_structures': [], 'functions': [], 'complexity_hints': [], 'imports': []}

def get_problem_description(problem_name):
    """Get a description based on the problem name"""
    descriptions = {
        'reverse_bits': 'Reverse the bits of a 32-bit unsigned integer',
        'number_of_1_bits': 'Count the number of 1 bits in an unsigned integer',
        'house_robber': 'Find maximum money that can be robbed without robbing adjacent houses',
        'coin_change': 'Find minimum number of coins needed to make up a given amount',
        'non_overlapping_intervals': 'Find minimum number of intervals to remove to make rest non-overlapping',
        'group_anagrams': 'Group strings that are anagrams of each other',
        'maximum_subarray': 'Find the contiguous subarray with the largest sum',
        'spiral_matrix': 'Return all elements of matrix in spiral order',
        'jump_game': 'Determine if you can reach the last index',
        'merge_intervals': 'Merge all overlapping intervals',
        'subtree_of_another_tree': 'Check if one tree is subtree of another',
        'insert_interval': 'Insert interval into sorted non-overlapping intervals',
        'unique_paths': 'Count unique paths from top-left to bottom-right in grid',
        'minimize_malware_spread': 'Find node to remove to minimize malware spread'
    }
    
    # Clean up the problem name
    clean_name = problem_name.replace('_', ' ').lower()
    for key, desc in descriptions.items():
        if key.replace('_', ' ') in clean_name:
            return desc
    
    return f"Solve the {problem_name.replace('_', ' ')} problem"

def generate_data_structures_section(code, analysis):
    """Generate the data structures section based on code analysis"""
    section = []
    
    # Common variable patterns
    if 'result' in code:
        section.append('* **`result`** - Stores the final answer/output of the algorithm')
    if 'dp' in code:
        section.append('* **`dp`** - Dynamic programming array to store subproblem solutions')
    if 'left' in code and 'right' in code:
        section.append('* **`left, right`** - Two pointers for sliding window or binary search')
    if 'visited' in code:
        section.append('* **`visited`** - Set or array to track visited nodes/elements')
    if 'stack' in code:
        section.append('* **`stack`** - Stack data structure for LIFO operations')
    if 'queue' in code:
        section.append('* **`queue`** - Queue data structure for BFS or FIFO operations')
    if 'head' in code:
        section.append('* **`head`** - Pointer to the head of a linked list')
    if 'root' in code:
        section.append('* **`root`** - Root node of a binary tree')
    
    # If no specific patterns found, add generic description
    if not section:
        section.append('* **Key variables and data structures used in the solution**')
    
    return '\n'.join(section)

def generate_approach_section(problem_name, analysis, code):
    """Generate the overall approach section"""
    approach_templates = {
        'dynamic_programming': 'This problem uses **Dynamic Programming** to build up solutions from smaller subproblems.',
        'two_pointers': 'This solution uses the **Two Pointers** technique to efficiently traverse the data.',
        'stack': 'This solution uses a **Stack** to maintain elements in LIFO order.',
        'queue': 'This solution uses a **Queue** for BFS traversal or FIFO processing.',
        'hash_table': 'This solution uses **Hash Tables** for O(1) lookup and storage.',
        'sorting': 'This solution involves **Sorting** the input for efficient processing.',
        'linked_list': 'This solution manipulates **Linked List** nodes and pointers.',
        'binary_tree': 'This solution traverses or manipulates a **Binary Tree**.',
        'graph_traversal': 'This solution uses **Graph Traversal** (DFS/BFS) techniques.'
    }
    
    # Determine main technique
    main_technique = 'an efficient algorithm'
    if analysis['complexity_hints']:
        hint = analysis['complexity_hints'][0]
        if hint in approach_templates:
            main_technique = approach_templates[hint].split('**')[1].lower()
    
    problem_desc = get_problem_description(problem_name)
    
    approach = f"""The problem asks us to {problem_desc.lower()}.

"""
    
    # Add the technique description
    if analysis['complexity_hints']:
        hint = analysis['complexity_hints'][0]
        if hint in approach_templates:
            approach += approach_templates[hint] + "\n\n"
    else:
        approach += "This solution uses an efficient approach to solve the problem.\n\n"
    
    approach += "The algorithm works by:"
    
    return approach

def generate_complexity_analysis(analysis, code):
    """Generate complexity analysis based on code patterns"""
    time_complexity = "O(n)"  # default
    space_complexity = "O(1)"  # default
    
    # Analyze for complexity patterns
    if 'dp' in code and any(char in code for char in ['[i]', '[j]']):
        if code.count('[i]') > 1 and code.count('[j]') > 1:
            time_complexity = "O(n²)"
            space_complexity = "O(n²)"
        else:
            time_complexity = "O(n)"
            space_complexity = "O(n)"
    elif 'sort' in code.lower():
        time_complexity = "O(n log n)"
    elif any(hint in analysis['complexity_hints'] for hint in ['stack', 'queue']):
        time_complexity = "O(n)"
        space_complexity = "O(n)"
    elif 'binary_tree' in analysis['complexity_hints']:
        time_complexity = "O(n)"
        space_complexity = "O(h) where h is the height of the tree"
    
    return f"""* **Time Complexity**: {time_complexity}
* **Space Complexity**: {space_complexity}"""

def extract_key_code_snippets(code):
    """Extract key code snippets for documentation"""
    lines = code.strip().split('\n')
    snippets = []
    
    # Find important loops or logic
    for i, line in enumerate(lines):
        if 'for' in line or 'while' in line:
            # Get the loop and a few lines after
            snippet = '\n'.join(lines[i:min(i+4, len(lines))])
            snippets.append(snippet.strip())
        elif 'if' in line and '==' in line or '>' in line or '<' in line:
            # Get important conditionals
            snippet = '\n'.join(lines[i:min(i+3, len(lines))])
            snippets.append(snippet.strip())
    
    return snippets[:2]  # Return first 2 snippets

def generate_enhanced_notes(filename, source_content):
    """Generate comprehensive notes with actual analysis"""
    problem_num, problem_name = extract_problem_info(filename)
    analysis = analyze_python_code(source_content)
    
    # Generate sections
    data_structures = generate_data_structures_section(source_content, analysis)
    approach = generate_approach_section(problem_name, analysis, source_content)
    complexity = generate_complexity_analysis(analysis, source_content)
    code_snippets = extract_key_code_snippets(source_content)
    
    # Build step-by-step explanation
    steps = []
    if code_snippets:
        for i, snippet in enumerate(code_snippets, 1):
            steps.append(f"""
{i}. **Step {i}**
   
   ```python
   {snippet}
   ```""")
    
    steps_section = ''.join(steps) if steps else """
1. **Initialize variables and data structures**
   
2. **Process the input using the chosen algorithm**
   
3. **Return the result**"""
    
    # Generate key insights based on analysis
    insights = []
    if 'dynamic_programming' in analysis['complexity_hints']:
        insights.append("* The problem exhibits optimal substructure - optimal solution contains optimal solutions to subproblems")
        insights.append("* Memoization avoids redundant calculations")
    if 'two_pointers' in analysis['complexity_hints']:
        insights.append("* Two pointers technique reduces time complexity from O(n²) to O(n)")
    if 'hash_table' in analysis['complexity_hints']:
        insights.append("* Hash table provides O(1) average lookup time")
    
    if not insights:
        insights.append("* Consider edge cases and boundary conditions")
        insights.append("* The algorithm handles the problem constraints efficiently")
    
    insights_section = '\n'.join(insights)
    
    template = f"""## Data Structures

{data_structures}

## Overall Approach

{approach}
{steps_section}

## Complexity Analysis

{complexity}

## Key Insights

{insights_section}

## Source Code Analysis

```python
{source_content.strip()}
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
"""
    
    return template

def extract_problem_info(filename):
    """Extract problem number and name from filename"""
    match = re.match(r'^(\d+)_(.+)$', filename)
    if match:
        problem_num = match.group(1)
        problem_name = match.group(2)
        return problem_num, problem_name
    return None, filename

def main():
    notes_dir = 'notes'
    src_dir = 'src'
    
    # Find all notes files that contain TODO
    todo_files = []
    for filename in os.listdir(notes_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(notes_dir, filename)
            with open(filepath, 'r') as f:
                content = f.read()
                if 'TODO:' in content:
                    todo_files.append(filename[:-3])  # Remove .md extension
    
    print(f"Found {len(todo_files)} notes files with TODOs to fill out:")
    for filename in sorted(todo_files):
        print(f"  {filename}.md")
    
    if not todo_files:
        print("No notes files with TODOs found!")
        return
    
    # Ask user if they want to fill out the templates
    fill_templates = input(f"\nDo you want to fill out the {len(todo_files)} template files? (y/N): ").lower().strip()
    
    if fill_templates == 'y':
        filled_count = 0
        for filename in sorted(todo_files):
            src_filepath = os.path.join(src_dir, f"{filename}.py")
            notes_filepath = os.path.join(notes_dir, f"{filename}.md")
            
            # Read source code
            try:
                with open(src_filepath, 'r') as f:
                    source_content = f.read()
            except Exception as e:
                print(f"Error reading {src_filepath}: {e}")
                continue
            
            # Generate enhanced notes
            enhanced_notes = generate_enhanced_notes(filename, source_content)
            
            # Update notes file
            try:
                with open(notes_filepath, 'w') as f:
                    f.write(enhanced_notes)
                print(f"Filled out: {notes_filepath}")
                filled_count += 1
            except Exception as e:
                print(f"Error updating {notes_filepath}: {e}")
        
        print(f"\nSuccessfully filled out {filled_count} notes files!")
    else:
        print("Template filling cancelled.")

if __name__ == "__main__":
    main()
