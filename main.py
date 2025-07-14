import json
from diagram_generator import generate_plantuml
from plantuml_wrapper import write_puml_file, render_png
from ollama_interface import query_ollama

#1. Load JSON-like semantic model
try:
    with open("input_sequence.json") as f:
        model = json.load(f)
        method_sequence = [(i["from"], i["to"], i["action"]) for i in model["interactions"]]
except Exception as e:
    print(" Failed to load input_sequence.json:", e)
    exit(1)

#2. AI description via Ollama (optional)
try:
    prompt = f"Explain this system interaction in plain language:\nActors: {model['actors']}\nInteractions: {model['interactions']}"
    description = query_ollama(prompt)
    print(" AI Description:\n", description)
except Exception as e:
    print(" Ollama query failed:", e)

#3. Generate UML from extracted sequence
puml_code = generate_plantuml(method_sequence)

#4. Render to PNG
puml_path = write_puml_file(puml_code)
png_path = render_png(puml_path)

print(f"Sequence diagram saved as: {png_path}")
