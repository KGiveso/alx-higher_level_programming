#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for i in range(len(sys.args) - 1):
        total += int(sys.args[i + 1])
    print("{}".format(total))
