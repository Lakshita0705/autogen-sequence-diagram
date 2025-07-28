import json

def load_semantic_model(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load {filepath}: {e}")
        return None

def extract_from_classes(classes):
    actors = set()
    interactions = []

    for cls in classes:
        caller = cls.get("name")
        actors.add(caller)
        for method in cls.get("methods", []):
            method_name = method.get("name")
            params = method.get("params", [])
            formatted_action = f"{method_name}({', '.join(params)})" if params else method_name

            for call in method.get("calls", []):
                if '.' in call:
                    callee, called_method = call.split('.', 1)
                else:
                    callee, called_method = call, "unknownMethod"

                actors.add(callee)
                interactions.append({
                    "from": caller,
                    "to": callee,
                    "action": called_method
                })
    return actors, interactions

def extract_from_workflows(workflows):
    actors = set()
    interactions = []

    for workflow in workflows:
        for step in workflow.get("steps", []):
            # Handle chained calls
            steps = [s.strip() for s in step.split("→")]
            for i in range(len(steps) - 1):
                sender = steps[i].split('.')[0]
                action = steps[i + 1].split('.')[-1]
                receiver = steps[i + 1].split('.')[0]
                actors.update([sender, receiver])
                interactions.append({
                    "from": sender,
                    "to": receiver,
                    "action": action
                })

    return actors, interactions

def extract_sequence_data(semantic_model):
    actors = set()
    interactions = []

    if "classes" in semantic_model:
        a, i = extract_from_classes(semantic_model["classes"])
        actors.update(a)
        interactions.extend(i)

    if "businessLogic" in semantic_model and "workflows" in semantic_model["businessLogic"]:
        a, i = extract_from_workflows(semantic_model["businessLogic"]["workflows"])
        actors.update(a)
        interactions.extend(i)

    return {
        "actors": sorted(list(actors)),
        "interactions": interactions
    }

def save_sequence_model(data, out_path="system_model.json"):
    try:
        with open(out_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Flattened sequence model saved to {out_path}")
    except Exception as e:
        print(f"Failed to save model: {e}")

if __name__ == "__main__":
    input_path = "input_sequence.json"
    semantic_model = load_semantic_model(input_path)
    if semantic_model:
        sequence_model = extract_sequence_data(semantic_model)
        save_sequence_model(sequence_model)
