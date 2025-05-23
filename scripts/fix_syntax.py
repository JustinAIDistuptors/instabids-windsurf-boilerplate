#!/usr/bin/env python3
"""
Syntax fixing script for AI-generated Python code.
Automatically fixes common syntax issues that AI agents might introduce.
"""

import ast
import sys
from pathlib import Path
from typing import List, Tuple

import black


def find_python_files(root_dir: Path) -> List[Path]:
    """Find all Python files in the project."""
    return list(root_dir.glob("**/*.py"))


def check_syntax(file_path: Path) -> Tuple[bool, str]:
    """Check if a Python file has valid syntax."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        ast.parse(content)
        return True, ""
    except SyntaxError as e:
        return False, str(e)


def fix_common_issues(content: str) -> str:
    """Fix common syntax issues in Python code."""
    # Fix common AI-generated syntax issues
    fixes = [
        # Missing colons after function definitions
        (r"def\s+(\w+)\s*\([^)]*\)\s*(?!:)", r"def \1():"),
        # Missing colons after class definitions
        (r"class\s+(\w+)\s*(?:\([^)]*\))?\s*(?!:)", r"class \1:"),
        # Incorrect indentation (this is handled by Black)
    ]
    
    # Apply regex fixes if needed
    # For now, we'll rely on Black to handle most formatting issues
    return content


def format_with_black(file_path: Path) -> bool:
    """Format a Python file with Black."""
    try:
        black.format_file_in_place(
            file_path,
            fast=False,
            mode=black.Mode(line_length=88, target_versions={black.TargetVersion.PY312}),
        )
        return True
    except Exception as e:
        print(f"Error formatting {file_path}: {e}")
        return False


def main():
    """Main function to fix syntax issues in all Python files."""
    root_dir = Path(".").resolve()
    src_dir = root_dir / "src"
    tests_dir = root_dir / "tests"
    
    if not src_dir.exists():
        print("Source directory not found. Are you in the project root?")
        sys.exit(1)
    
    all_files = find_python_files(src_dir) + find_python_files(tests_dir)
    
    issues_found = 0
    files_fixed = 0
    
    print(f"Checking {len(all_files)} Python files...")
    
    for file_path in all_files:
        valid, error = check_syntax(file_path)
        
        if not valid:
            issues_found += 1
            print(f"\nSyntax error in {file_path}:")
            print(f"  {error}")
            
            # Try to fix with Black
            if format_with_black(file_path):
                # Check again
                valid, _ = check_syntax(file_path)
                if valid:
                    files_fixed += 1
                    print(f"  ✅ Fixed!")
                else:
                    print(f"  ❌ Could not fix automatically")
    
    if issues_found == 0:
        print("\n✅ No syntax issues found!")
    else:
        print(f"\n📊 Summary:")
        print(f"  - Issues found: {issues_found}")
        print(f"  - Files fixed: {files_fixed}")
        print(f"  - Files requiring manual fix: {issues_found - files_fixed}")
    
    sys.exit(0 if issues_found == files_fixed else 1)


if __name__ == "__main__":
    main()