## Data Structures

**s**

* A string of characters, each one of: ‘(’, ‘)’, ‘{’, ‘}’, ‘\[’, ‘]’.

**stack**

* A list (used as a stack) to keep track of opening brackets encountered.

**pairs**

* A mapping from each closing bracket to its matching opening bracket:

  ```
  pairs = {
    ')' : '(',
    '}' : '{',
    ']' : '['
  }
  ```

## What happens in isValid(s)

```mermaid
flowchart TD
  A["Start: s"] --> B["Initialize empty stack"]
  B --> C{"Iterate each character c in s"}
  C --> D{"Is c a closing bracket?"}
  D -->|Yes| E["Check if stack non-empty and top == pairs[c]"]
  E -->|True| F["Pop stack"]
  E -->|False| G["Return False"]
  D -->|No| H["Push c onto stack"]
  F --> C
  H --> C
  C --> I{"End of string?"}
  I -->|Yes| J{"Is stack empty?"}
  J -->|Yes| K["Return True"]
  J -->|No| L["Return False"]
```

1. **Initialize**

   ```python
   stack = []
   pairs = {')': '(', '}': '{', ']': '['}
   ```

2. **Process each character**

   * Loop over each character (call it **c**) in **s**.
   * If **c** is one of the closing brackets (i.e. it appears as a key in **pairs**):

     1. Verify that **stack** is not empty **and** that its top element equals **pairs\[c]**.
     2. If that check fails, return **False** immediately; otherwise pop the top of **stack**.
   * If **c** is not a closing bracket, treat it as an opening bracket and append it to **stack**.

3. **Final check**

   * After the loop finishes, if **stack** is empty then every opening bracket had a matching closer in the correct order → return **True**.
   * Otherwise there were unmatched openings → return **False**.

## Complexity

* **Time:** O(n), where n is the length of **s**. Each character is looked at exactly once.
* **Space:** O(n) in the worst case, since all characters could be opening brackets and pushed onto **stack**.
