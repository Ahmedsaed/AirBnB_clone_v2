import ast
import sys
import os

def has_docstring(node):
    """Returns True if node has a docstring, False otherwise."""
    return isinstance(node, ast.FunctionDef) or \
           isinstance(node, ast.AsyncFunctionDef) or \
           isinstance(node, ast.ClassDef) or \
           isinstance(node, ast.Module) and bool(ast.get_docstring(node))

def check_docstrings(filename):
    """Checks if all modules, classes, and functions have docstrings."""
    with open(filename, 'r') as file:
        content = file.read()

    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"Error parsing {filename}: {e}")
        return False

    missing_docstrings = []

    for node in ast.walk(tree):
        if has_docstring(node):
            if not ast.get_docstring(node):
                missing_docstrings.append(node.name if hasattr(node, "name") else node.__class__.__name__)

    if missing_docstrings:
        print(f"Missing docstrings in {filename}:")
        for item in missing_docstrings:
            print(f"  - {item}")
        return False

    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_docstrings.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        sys.exit(1)

    if check_docstrings(filename):
        print(f"All modules, classes, and functions in {filename} have docstrings.")
    else:
        sys.exit(1)
