🚀 Deli-Heimdall v0.1.5 - The Modular YAML-Driven Pipeline Release
We are excited to introduce a major architectural leap in the core pipeline execution model of Deli-Heimdall. With this release, the library transitions into a highly scalable, plugin-based framework, allowing users to build complex data processing workflows using pure YAML configurations without writing a single line of boilerplate Python code.

🌟 Key Architectural Updates
Safely Decoupled Pipeline Executor (MyPipeline): The core engine has been stripped of hardcoded methods. It now acts as a pure, lightweight YAML orchestrator that translates multi-stage blueprints into dynamic executions.

Declarative Multi-Stage Configurations (stages & actions): Complex pipelines can now be vertically scaled and logically grouped into stages (e.g., Ingestion, Cleaning, Export). This keeps your configuration files readable and organized, no matter how large the project grows.

Dynamic Plugin Discovered via hasattr: Seamlessly integrates standalone loaders and cleaners. Adding new data processing capabilities is now as simple as dropping a new .py file into the corresponding module directory; the pipeline engine automatically adopts it.

Bulletproof Data Cleaning (delete_empty_rows): Introduced a resilient cleaning mechanism that strips whitespace and unmasks pseudo-empty string values like "None", "nan", and "NaN", forcing them into actual pd.NA bounds before elimination.

Production-Grade Logging Integration: Replaced all primitive print statements with a robust, timestamps-enabled logger utility for transparent and traceable runtime audit logs.

📦 How It Works (For Users)
Users can now initiate a full data pipeline with just three lines of code by mapping their logic entirely inside a config.yaml file:

YAML
project_name: "Production Energy Analytics"

stages:

- name: "Data Ingestion"
  actions:
  - load_csv:
    path: "raw_data.csv"
    encoding: "utf-8"

- name: "Data Cleaning"
  actions:
  - delete_empty_rows:
    column: "consumption_kw"

- name: "Data Export"
  actions: - save_csv:
  path: "output/cleaned_data.csv"
  Python
  from dheimdall.core.pipelines import MyPipeline

pipeline = MyPipeline("config.yaml")
pipeline.run()
🛠️ Technical Enhancements & Bug Fixes
Added an early-catch path verification (os.path.exists) during pipeline initialization to prevent cryptic runtime crashes.

Implemented clean Type Hinting (pd.DataFrame, str) across core modules for enhanced IDE autocompletion and enterprise-grade maintainability.
