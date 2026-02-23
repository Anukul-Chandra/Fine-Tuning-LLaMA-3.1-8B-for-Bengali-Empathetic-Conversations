import os

folders = [
    "src/data",
    "src/training",
    "src/evaluation",
    "configs",
    "logs"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

files = [
    "train.py",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

for file in files:
    open(file, 'a').close()

print("Project structure created!")