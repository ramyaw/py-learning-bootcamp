# Day 3 – Functions, Return Values & Error Handling

✅ Focus:
- Define and call functions
- Use return and arguments
- Handle exceptions with try / except

☕ Java vs 🐍 Python – Day 3: Functions & Exceptions

| Concept                 | Java                                         | Python                               | Notes                                |
|-------------------------|----------------------------------------------|--------------------------------------|--------------------------------------|
| Define function/method  | `public int sum(int a, int b)`              | `def sum(a, b):`                     | Python is dynamically typed          |
| Return value            | `return a + b;`                             | `return a + b`                       | No type declaration needed           |
| Call function           | `sum(3, 4);`                                | `sum(3, 4)`                          | Same syntax                          |
| Default args            | Method overloading                          | `def greet(name="Ramya"):`          | Python supports default params       |
| Multi return values     | Return array or object                      | `return a, b`                        | Python returns tuples                |
| Static method           | `static int sum(...)`                       | `@staticmethod` or plain function    | Module-level functions by default    |
| Try-catch exception     | `try { ... } catch (Exception e) {}`        | `try: ... except Exception:`        | Cleaner syntax                       |
| Catch specific error    | `catch (IOException e)`                     | `except IOError:`                   | Python has rich built-in errors      |
| Finally block           | `finally { ... }`                           | `finally:`                          | Same purpose, shorter syntax         |
| Throw exception         | `throw new Exception("msg")`               | `raise Exception("msg")`           | Very similar                         |
| Parse integer           | `Integer.parseInt("3")`                     | `int("3")`                          | Python is simpler                    |
| Handle parse failure    | `catch (NumberFormatException e)`           | `except ValueError:`                | Python error names are intuitive     |
| Print output            | `System.out.println("Hello")`              | `print("Hello")`                    | Simpler in Python                    |
| Logging                 | `Logger.info("msg")`                        | `import logging; logging.info(...)` | Python has built-in `logging` module |


