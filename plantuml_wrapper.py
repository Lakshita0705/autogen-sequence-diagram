import subprocess
import os

def write_puml_file(puml_code, path="output/sequence.puml"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(puml_code)
    return path

def render_png(puml_path, jar_path="plantuml-mit-1.2025.4.jar"):
    subprocess.run(["java", "-jar", jar_path, puml_path], check=True)
    png_path = puml_path.replace(".puml", ".png")
    if os.path.exists(png_path):
        print(f" PNG generated at: {png_path}")
    return png_path
