import os
import ast
import subprocess
import sys

SRC_DIR = os.path.join(os.path.dirname(__file__), '..', 'src')

def find_python_files(directory):
    py_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    return py_files

def extract_imports_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
        except SyntaxError:
            print(f"Skipping {file_path} due to syntax error.")
            return []

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

def find_local_modules(src_dir):
    """Return a set of top-level module names that exist locally in SRC_DIR."""
    local_modules = set()
    for root, dirs, files in os.walk(src_dir):
        # Consider top-level modules only (direct children of SRC_DIR)
        rel_path = os.path.relpath(root, src_dir)
        if rel_path == '.':
            for d in dirs:
                # If directory has __init__.py, treat as package
                if os.path.isfile(os.path.join(root, d, '__init__.py')):
                    local_modules.add(d)
            for f in files:
                if f.endswith('.py'):
                    local_modules.add(os.path.splitext(f)[0])
    return local_modules

def install_package(pkg):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])
    except subprocess.CalledProcessError:
        print(f"Failed to install {pkg}")

def main():
    print(f"Scanning Python files in: {SRC_DIR}")
    
    py_files = find_python_files(SRC_DIR)
    print(f"Found {len(py_files)} Python files.")

    all_imports = set()
    for py_file in py_files:
        imports = extract_imports_from_file(py_file)
        all_imports.update(imports)

    local_modules = find_local_modules(SRC_DIR)
    print(f"Detected local modules: {local_modules}")

    to_install = []
    for module in all_imports:
        # Skip if module is local (part of SRC_DIR)
        if module in local_modules:
            continue
        
        try:
            __import__(module)
        except ImportError:
            to_install.append(module)

    print(f"Installing {len(to_install)} packages: {to_install}")
    for pkg in to_install:
        install_package(pkg)

if __name__ == "__main__":
    main()
