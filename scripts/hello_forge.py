"""
The Builder Forge - Environment Verification Script
Run this to confirm your Python environment is set up correctly.
"""

import sys
import platform
import importlib


def check_environment():
    print("=" * 50)
    print("THE BUILDER FORGE - Environment Check")
    print("=" * 50)
    print()
    print(f"Python Version:  {sys.version}")
    print(f"Python Location: {sys.executable}")
    print(f"Platform:        {platform.platform()}")
    print()

    packages = [
        "fastapi",
        "uvicorn",
        "requests",
        "httpx",
        "pandas",
        "dotenv",
        "pytest",
    ]

    print("Package Check:")
    all_good = True
    for package in packages:
        try:
            mod = importlib.import_module(package)
            version = getattr(mod, "__version__", "installed")
            print(f"  OK {package} ({version})")
        except ImportError:
            print(f"  MISSING {package}")
            all_good = False

    print()
    if all_good:
        print("All checks passed. The Builder Forge is online.")
    else:
        print("Some packages missing. Run: pip install -r requirements.txt")
    print("=" * 50)


if __name__ == "__main__":
    check_environment()
