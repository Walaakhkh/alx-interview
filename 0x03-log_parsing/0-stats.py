#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the total file size and counts for each status code in ascending order."""
    print("File size:", total_size)
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def handle_exit(signal, frame):
    """Handles keyboard interrupt to print stats before exiting."""
    print_stats()
    sys.exit(0)

# Set up signal handler for graceful exit on keyboard interrupt (CTRL+C)
signal.signal(signal.SIGINT, handle_exit)

try:
    for line in sys.stdin:
        line_count += 1

        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total file size and status code count
            total_size += file_size
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
        except (IndexError, ValueError):
            # Skip lines that don't match the expected format
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interrupt gracefully
    print_stats()
    raise
