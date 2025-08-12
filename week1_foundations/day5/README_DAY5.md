# Day 4 – File I/O, CSV, JSON Handling

✅ Goals
- Organize code using modules (.py files)
- Use import and from ... import
- Build a reusable test_utils library
- Practice building + importing helpers

📦 Java vs 🐍 Python – Day 5: Modularization & Imports

| Concept                  | Java                                             | Python                                       | Notes                                                  |
|--------------------------|--------------------------------------------------|----------------------------------------------|--------------------------------------------------------|
| Define reusable method   | `public static int sum(...)`                    | `def sum(...):`                              | Python doesn’t need `public`, `static`, or return types |
| Create utility file      | `Utils.java`                                    | `test_utils.py`                              | Each `.py` file is a module                            |
| Package structure        | `com.project.utils.Utils`                       | `folder/test_utils.py`                       | Python uses folders + files, no explicit `package`     |
| Import method            | `import com.project.utils.Utils;`               | `from test_utils import sum`                 | Python imports by filename                            |
| Import all functions     | `import static Utils.*;`                        | `import test_utils`                          | Access functions via `test_utils.fn()`                 |
| Function alias           | Not common                                      | `import test_utils as utils`                | Aliases simplify long module names                    |
| Main method entry point  | `public static void main(String[] args)`        | `if __name__ == "__main__":`                | Python’s entry-point idiom                            |
| Command line arguments   | `String[] args`                                 | `import sys; sys.argv`                      | Python reads args from `sys.argv` list                |
| Run module from CLI      | `java App` with args                            | `python app.py arg1 arg2`                   | Python is script-first                                |
| File as import & script  | No (needs `main`)                               | Yes – script + import logic in one file     | Python files can be both importable & executable      |
