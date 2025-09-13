import sys
import subprocess

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode == "ui":
        subprocess.run(["pytest", "tests/test_ui.py"])
    elif mode == "api":
        subprocess.run(["pytest", "tests/test_api.py"])
    else:
        subprocess.run(["pytest", "tests/"])
