# Day 4 – File I/O, CSV, JSON Handling

✅ Focus:
- Read/write files
- Parse and write CSV and JSON
- Apply to real-world test data formats

📁 Java vs 🐍 Python – Day 4: File I/O, CSV, JSON (Markdown Table)

| Concept                  | Java (Typical)                                           | Python (Simplified)                             | Notes                                          |
|--------------------------|-----------------------------------------------------------|--------------------------------------------------|------------------------------------------------|
| Read text file           | `BufferedReader reader = new BufferedReader(...)`       | `with open("file.txt", "r") as f:`              | `with` ensures auto-close                     |
| Read line-by-line        | `reader.readLine()` loop                                | `for line in f:`                                | Python is iterable by default                 |
| Write to file            | `FileWriter writer = new FileWriter("file.txt")`        | `with open("file.txt", "w") as f:`              | Auto-closes + indentation cleaner             |
| CSV parser               | `OpenCSV` or `Apache Commons CSV`                       | `import csv`                                    | Built-in CSV module in Python                 |
| Read CSV rows            | `CSVReader reader = new CSVReader(new FileReader(...))` | `csv.DictReader(f)`                             | `DictReader` returns rows as dictionaries     |
| Write CSV rows           | `CSVWriter.writeNext(...)`                              | `csv.DictWriter(f).writerow({...})`             | Requires header definition in both            |
| JSON support             | `Gson`, `Jackson`, or `org.json`                        | `import json`                                   | Native JSON support in Python                 |
| Parse JSON string        | `new JSONObject(jsonStr)`                               | `json.loads(json_str)`                          | Python returns dict                           |
| Read JSON file           | `mapper.readValue(file, Map.class)`                     | `json.load(f)`                                  | File must be opened before use                |
| Write JSON file          | `mapper.writeValue(file, object)`                       | `json.dump(data, f, indent=2)`                  | `indent` pretty-prints the output             |
| Handle missing file      | `try { ... } catch (IOException e)`                     | `try: ... except FileNotFoundError:`            | Cleaner error names                           |
| Handle parse error       | `catch (JsonParseException e)`                          | `except json.JSONDecodeError:`                  | Python has granular exceptions                |

