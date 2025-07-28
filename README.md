# Autogen Sequence Diagram Generator

Automatically generate UML sequence diagrams from class and method relationships using AI-powered analysis. This tool reads semantic JSON representations of your code and converts them into PlantUML diagrams — making architectural understanding faster and easier. It leverages local LLMs through Ollama and renders .puml and .png sequence diagrams using PlantUML.

---

## Features

- Parses semantic .json files representing classes and method calls.
- Uses local LLMs (via Ollama) to semantically analyze relationships.
- Generates valid PlantUML sequence diagrams (.puml).
- Renders output diagrams as images (.png) using plantuml.jar.
- Modular code structure for easy extension or integration.
  
---

## Project Structure

```bash
autogen-sequence-diagram/
├── diagram_generator.py        # Handles core diagram logic
├── input_sequence.json         # Sample input format for sequence flow
├── main.py                     # Entry point for running the generator
├── ollama_interface.py         # Interface to communicate with Ollama LLM
├── parser.py                   # Extracts data from input JSON
├── plantuml_wrapper.py         # Converts .puml files to images using PlantUML
├── plantuml-mit-1.2025.4.jar   # PlantUML JAR (MIT version)
├── system_model.json           # Another example input file
├── output/                     # Generated diagram files (.puml, .png, etc.)
└── __pycache__/                # Python bytecode cache
```

---

## Setup Instructions

1. **Clone the Repository**
``` bash
git clone https://github.com/Lakshita0705/autogen-sequence-diagram.git
cd autogen-sequence-diagram
```
2. **Create Virtual Environment**
``` bash
python -m venv venv
venv\Scripts\activate 
```
3. **Install Dependencies**
Install all required Python packages:
``` bash
pip install openai autogen python-dotenv requests plantuml
```
4. **Install and Run Ollama (for Local LLMs)**
``` bash
ollama pull phi
ollama run phi
```
5. **Run the Script**
``` bash
python main.py
```

---

## License

This project is licensed under the MIT License.
