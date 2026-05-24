# 👁️ Deli-Heimdall: Data Analysis Library

**Deli-Heimdall** is an open-source Python library designed to manage modern data engineering and data analysis workflows through a dynamic, flexible, and bulletproof pipeline architecture.

Named after the all-seeing Norse god, **Deli-Heimdall** spots structural anomalies, formatting issues, and corrupted rows in your datasets at the very first step, ensuring clean and reliable data processing.

---

## 🚀 Key Features

- **Zero-Keyword Flexible Pipeline:** Manages dynamic workflows directly via YAML/JSON using native function names, without being bound to rigid keywords like `step`.
- **Armored File Loader (Smart CSV/Excel Detection):** Detects spoofed files—such as an Excel file intentionally renamed to `.csv`—by inspecting file signatures (`PK\x03\x04`) under the hood, instantly catching format manipulation.
- **Dirty Data Isolation:** Extracts malformed or corrupted rows during CSV parsing without breaking the main execution loop, dumping them into a dedicated `logs/heimdall_bad_lines.txt` report.
- **Enterprise-Grade Logging:** Features a built-in dual-handler logging mechanism that outputs clean console streams and automatically preserves execution history inside an isolated `logs/` directory.
- **Frontend-Ready Design:** Built on a completely data-driven architecture, making it seamlessly compatible with future Web/Desktop interfaces (React, Vue, Electron, etc.).

---

## 🛠️ Installation & Quick Start

Install the official package directly from PyPI:

```bash
pip install deli-heimdall
Development Mode (Editable Install)
If you are developing locally on the source code, eliminate the need for PYTHONPATH workarounds by running this command in the root directory:

Bash
pip install -e .
Now you can run your scripts directly from any terminal session:

Bash
python main.py

📋 Example Pipeline Configuration (config.yaml)
Deli-Heimdall eliminates complex loops and messy if-elif boilerplates. Simply define your steps sequentially in a YAML configuration file:

YAML
project_name: "Heimdall Energy Data Analysis"

pipeline:
  load:
    path: "data/raw_dataset.csv"
    encoding: "utf-8"

  # Future transformation modules will be chained here dynamically

  save:
    path: "output/cleaned_result.csv"
In your Python code, executing this pipeline is as simple as:

Python
import dheimdall

# Your dynamic pipeline execution logic here
🤝 Contributing
Deli-Heimdall features a highly modular, open architecture. To introduce a new data processing stage, simply add a callable method to your pipeline class—our dynamic execution engine will automatically register and resolve it!

Feel free to open an Issue or submit a Pull Request for any features or improvements you'd like to add.

Licensed under the MIT License.
```
