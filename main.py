import json
from diagram_generator import generate_plantuml
from plantuml_wrapper import write_puml_file, render_png
from ollama_interface import query_ollama

# --- PARSER INTEGRATION ---
from parser import load_semantic_model, extract_sequence_data, save_sequence_model

# Step 0: Convert semantic_model.json -> system_model.json
semantic_path = "input_sequence.json"
semantic_data = load_semantic_model(semantic_path)
if semantic_data:
    system_data = extract_sequence_data(semantic_data)
    save_sequence_model(system_data, "system_model.json")
else:
    print(" Failed to load semantic model.")
    exit(1)

# Step 1: Load parsed model (system_model.json)
try:
    with open("system_model.json") as f:
        model = json.load(f)
        method_sequence = [(i["from"], i["to"], i["action"]) for i in model["interactions"]]
except Exception as e:
    print(" Failed to load system_model.json:", e)
    exit(1)

# Step 2: Generate AI description
try:
    prompt = f"Explain this system interaction in plain language:\nActors: {model['actors']}\nInteractions: {model['interactions']}"
    description = query_ollama(prompt)
    print(" AI Description:\n", description)
except Exception as e:
    print("Ollama query failed:", e)

# Step 3: Generate PlantUML code
puml_code = generate_plantuml(method_sequence)

# Step 4: Write to .puml file
puml_path = write_puml_file(puml_code)

# Step 5: Render diagram as PNG
png_path = render_png(puml_path)

print(f"Sequence diagram saved as: {png_path}")
