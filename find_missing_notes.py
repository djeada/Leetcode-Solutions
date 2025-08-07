#!/usr/bin/env python3

import os
import re

def get_base_names(directory, extension):
    """Get base names of files with given extension from directory"""
    files = []
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(file[:-len(extension)])
    return set(files)

def extract_problem_info(filename):
    """Extract problem number and name from filename"""
    # Pattern: number_problem_name
    match = re.match(r'^(\d+)_(.+)$', filename)
    if match:
        problem_num = match.group(1)
        problem_name = match.group(2).replace('_', ' ').title()
        return problem_num, problem_name
    return None, filename

def read_source_file(filepath):
    """Read and analyze the source file to understand the solution structure"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""

def generate_notes_template(filename, source_content):
    """Generate a notes template based on the source code"""
    problem_num, problem_name = extract_problem_info(filename)
    
    template = f"""## Data Structures

* **`TODO: Identify key data structures used`**
  Description of the main data structures and variables used in the solution.

## Overall Approach

TODO: Describe the algorithm and approach used to solve this problem.

The solution uses [TODO: mention technique/algorithm] to achieve [TODO: goal].

1. **Step 1**
   
   ```python
   # TODO: Add code snippet showing key steps
   ```

2. **Step 2**
   
   ```python
   # TODO: Add more code snippets as needed
   ```

## Complexity Analysis

* **Time Complexity**: TODO: Analyze time complexity
* **Space Complexity**: TODO: Analyze space complexity

## Key Insights

* TODO: Add key insights about the problem and solution
* TODO: Mention any edge cases or important considerations

## Source Code Analysis

```python
{source_content.strip()}
```

## Related Problems

* TODO: List related LeetCode problems
* TODO: Mention similar techniques or patterns
"""
    
    return template

def main():
    src_dir = 'src'
    notes_dir = 'notes'
    
    # Get base names (without extensions)
    src_files = get_base_names(src_dir, '.py')
    notes_files = get_base_names(notes_dir, '.md')
    
    # Find missing notes
    missing_notes = src_files - notes_files
    
    print("Missing notes files:")
    for missing in sorted(missing_notes):
        print(f"  {missing}.md")
    
    print(f"\nTotal missing: {len(missing_notes)}")
    print(f"Total src files: {len(src_files)}")
    print(f"Total notes files: {len(notes_files)}")
    
    # Save missing files list
    with open('missing_notes.txt', 'w') as f:
        for missing in sorted(missing_notes):
            f.write(f"{missing}\n")
    
    # Only ask to create files if there are missing ones
    if len(missing_notes) == 0:
        print("\nAll notes files are already present! No files need to be created.")
        return sorted(missing_notes)
    
    # Ask user if they want to create the missing notes files
    create_files = input(f"\nDo you want to create the {len(missing_notes)} missing notes files? (y/N): ").lower().strip()
    
    if create_files == 'y':
        created_count = 0
        for missing in sorted(missing_notes):
            src_filepath = os.path.join(src_dir, f"{missing}.py")
            notes_filepath = os.path.join(notes_dir, f"{missing}.md")
            
            # Read source code
            source_content = read_source_file(src_filepath)
            
            # Generate notes template
            template = generate_notes_template(missing, source_content)
            
            # Create notes file
            try:
                with open(notes_filepath, 'w') as f:
                    f.write(template)
                print(f"Created: {notes_filepath}")
                created_count += 1
            except Exception as e:
                print(f"Error creating {notes_filepath}: {e}")
        
        print(f"\nSuccessfully created {created_count} notes files!")
    else:
        print("Notes files creation cancelled.")
    
    return sorted(missing_notes)

if __name__ == "__main__":
    main()
