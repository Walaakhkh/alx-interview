#!/usr/bin/python3
"""
Log Parsing Script

This script reads logs from standard input line by line in a specific format.
It computes metrics every 10 lines and upon receiving a keyboard interruption.
"""

import sys
import signal

# Initialize global counters
total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_stats():
    """Prints the accumulated file size and status code counts."""
    print("File size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


def handle_interrupt(sig, frame):
    """Handles keyboard interruption and prints final stats."""
    print_stats()
    sys.exit(0)


# Register the keyboard interrupt handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()

        # Validate and parse line
        if len(parts) >= 7 and parts[-2].isdigit() and parts[-1].isdigit():
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update total file size
                total_file_size += file_size

                # Update status code counts if it's a known code
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            except ValueError:
                # Skip line if there's an error in converting file size or status code
                continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

    # Print final stats if not interrupted after the last set of 10 lines
    if line_count % 10 != 0:
        print_stats()

except KeyboardInterrupt:
    # Handle any unhandled KeyboardInterrupts gracefully
    print_stats()
    raise
