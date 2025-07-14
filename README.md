# AutoGen AI - UML Sequence Diagram Generator
This project is a dynamic AI-powered tool that generates UML **Sequence Diagrams** from **language-independent semantic models** (in JSON format). It uses:
-A local LLM (Phi via Ollama) for interpreting and describing system interactions
-PlantUML to convert those interactions into clean UML sequence diagrams
-Automatic PNG image generation of the UML diagram

 ---
 
# Features
AutoGen AI: Powered by Ollama's Phi model (LLM)  
Dynamic: Each diagram is generated based on live semantic input  
Language-Independent: No need for Java, Python, etc. — input is in pure JSON  

---

# Project Structure
autogen_sequence_ai/
├── main.py # Main runner script
├── diagram_generator.py # Builds PlantUML from JSON
├── plantuml_wrapper.py # Converts PlantUML (.puml) to PNG
├── ollama_interface.py # Communicates with Ollama's local Phi model
├── input_sequence.json # Language-independent semantic model input
├── output/ # Contains generated sequence.puml and sequence.png
└──plantuml.jar # PlantUML renderer 

---

# Setup Instructions
1. install requirements
  -Python 3.10+
  -Java
  -Ollama (for LLM)
   pip install requests
2. Start Ollama with Phi model
   ollama run phi
3. Download PlantUML Jar
  Download plantuml.jar from:
  https://plantuml.com/download
  Place it inside the root folder of this project.
4. Run
   python main.py

---

# Output
After running, check the output/ folder:
output/
├── sequence.puml       # PlantUML syntax
└── sequence.png        # UML diagram image
