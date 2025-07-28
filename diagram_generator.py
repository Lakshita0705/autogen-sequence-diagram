def generate_plantuml(sequence):
    lines = ["@startuml"]
    participants = set()

    for sender, receiver, _ in sequence:
        participants.add(sender)
        participants.add(receiver)

    for p in participants:
        lines.append(f"participant {p}")

    for sender, receiver, message in sequence:
        lines.append(f"{sender} -> {receiver} : {message}")

    lines.append("@enduml")
    return "\n".join(lines)
