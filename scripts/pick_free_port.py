#!/usr/bin/env python3
"""
Port allocator utility to prevent port conflicts.
Essential for Windows development where port conflicts are common.
"""

import socket
import random
import sys
import argparse


def find_free_port(start: int = 8100, end: int = 9000, attempts: int = 20) -> int:
    """Find an available TCP port in the specified range."""
    for _ in range(attempts):
        port = random.randint(start, end)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                s.close()
                return port
            except socket.error:
                continue
    
    raise RuntimeError(f"No free port found in range {start}-{end} after {attempts} attempts")


def check_port(port: int) -> bool:
    """Check if a specific port is available."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("", port))
            s.close()
            return True
        except socket.error:
            return False


def main():
    """Main function for CLI usage."""
    parser = argparse.ArgumentParser(description="Find an available TCP port")
    parser.add_argument(
        "--check", type=int, help="Check if a specific port is available"
    )
    parser.add_argument(
        "--start", type=int, default=8100, help="Start of port range (default: 8100)"
    )
    parser.add_argument(
        "--end", type=int, default=9000, help="End of port range (default: 9000)"
    )
    
    args = parser.parse_args()
    
    if args.check:
        if check_port(args.check):
            print(f"Port {args.check} is available")
            sys.exit(0)
        else:
            print(f"Port {args.check} is in use")
            sys.exit(1)
    else:
        try:
            port = find_free_port(args.start, args.end)
            print(port)
            sys.exit(0)
        except RuntimeError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()