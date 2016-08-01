Effective Python
================

Source code for `Effective Python: 59 Specific Ways to Write Better Python`.

Pythonic Thinking
-----------------

### 1. Know Which Version of Python You're Using

  * There are two major versions of Python still in active use: Python 2 and Python 3.
  * There are multiple popular runtimes for Python: CPython, Jython, IronPython, PyPy, etc.
  * Be sure that the command-line for running Python on your system is the version you expect it ot be.
  * Prefer Python 3 for your next project because that is th primary focus of the Python community.

### 2. Follow the PEP 8 Style Guide

  * Always follow the PEP 8 style guide when writing Python code.
  * Sharing a common style with the larger Python community facilitates collaboration with others
  * Using a consistent style makes it easier to modify your own code later.

### 3. Know the Differences Between `bytes`, `str`, and `unicode`

  * In Python 3, `bytes` contains sequences of 8-bit values, `str` contains sequences of Unicode characters. `bytes` and `str` instances can't be used together with operators (like `>` or `+`)
  * In Python 2, `str` contains sequences of 8-bit values, `unicode` contains sequences of Unicode characters. `str` and `unicode` *can* be used together with operators if the `str` only contains 7-bit ASCII characters.
  * Use helper functions to ensure that the inputs you operate on are the type of character sequence you expect (8-bit values, UTF-8 encode character, Unicode characters, etc.).
  * If you want to read or write binary data to/from a file, always open the file using a binary mode (like `'rb'` or `'wb'`).

### 4. Write Helper Functions Instead of Complex Expressions

  * Python's syntax makes it all too easy to write single-line expressions that are overly complicated and difficult to read.
  * Move complex expressions into helper functions, especially if you need to use the same logic repeatedly.
  * The `if/else` expression provide a more readable alternative to using Boolean operators like `or` and `and` in expressions.

### 5. Know How to Slice Sequences

  * Avoid being verbose: Don't supply `0` for the `start` index or the length of the sequence for the `end` index.
  * Slicing is forgiving of `start` or `end` indexes that are out of bounds, making it easy to express slices on the front or back boundaries of a sequence (like `a[:20]` or `a[-20]`).
  * Assigning to a `list` slice will replace that range in the original sequence with what's referenced even if their lengths are different.

### 6. Avoid Using `start`, `end`, and `stride` in a Single Slice

  * Specifying `start`, `end`, and `stride` in a slice can be extremely confusing.
  * Prefer using positive `stride` values in slices without `start` or `end` indexes. Avoid negative `stride` values if possible.
  * Avoid using `start`, `end`, and `stride` together in a single slice. If you need all three parameters, consider doing two assignments (one to slice, another to stride) or using `islice` from the `itertools` built-in module.

### 7. Use List Comprehensions Instead of `map` and `filter`

  * List comprehensions are clearer than the `map` and `filter` built-in functions because they don't require extra `lambda` expressions.
  * List comprehensions allow you to easily skip items from the input list, a behavior `map` doesn't support without help from `filter`.
  * Dictionaries and sets also support comprehension expressions.

### 8. Avoid More Than Two Expressions in List Comprehensions

  * List comprehensions support multiple levels of loops and multiple conditions per loop level.
  * List comprehensions with more than two expressions are very difficult to read and should be avoided.

### 9. Consider Generator Expressions for Large Comprehensions

  * List comprehensions can cause problems for large inputs by using too much memory.
  * Generator expressions avoid memory issues by producing outputs one at a time as an iterator.
  * Generator expressions can be composed by passing the iterator from one generator expression into the `for` subexpression of another.
  * Generator expressions execute very quickly when chained together.

### 10. Prefer `enumerate` Over `range`

  * `enumerate` provides concise syntax for looping over an iterator and getting the index of each item from the iterator as you go.
  * Prefer `enumerate` instead of looping over a `range` and indexing into a sequence.
  * You can supply a second parameter to `enumerate` to specify the number from which to begin counting (zero is the default).

### 11. Use `zip` to Process Iterators in Parallel

  * The `zip` built-in function can be used to iterate over multiple iterators in parallel.
  * In Python 3, `zip` is a lazy generator that produces tuples. In Python 2, `zip` returns the full result as a list of tuples.
  * `zip` truncates its output silently if you supply it with iterators of different lengths.
  * The `zip_longest` function from the `itertools` built-in module lets you iterate over multiple iterators in parallel regardless of their lengths (see Item 46: "Use Built-in Algorithms and Data Structures").

### 12. Avoid `else` Blocks After `for` and `while` Loops

  * Python has special syntax that allows `else` blocks to immediately follow `for` and `while` loop interior blocks.
  * The `else` block after a loop only runs if the loop body did bot encounter a `break` statement.
  * Avoid using `else` block after loops because their behavior isn't intuitive and can be confusing.

### 13. Take Advantage of Each Block in `try/except/else/finally`

  * The `try/finally` compound statement lets you run cleanup code regardless of whether exceptions were raised in the `try` block.
  * The `else` block helps you minimize the amount of code in `try` blocks and visually distinguish the success case from the `try/except` blocks.
  * An `else` block an be used to perform additional actions after a successful `try` block but before common cleanup in a `finally` block.
