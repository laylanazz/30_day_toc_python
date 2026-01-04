import sys


def main():

    stats = {"count": 10, "average": 4.5, "valid": True}

    print(f"Stats: {stats}")
    print(f"Count: {stats["count"]}")
    print(f"Average: {stats["average"]}")
    print(f"Valid: {stats["valid"]}")

    stats["count"] += 5
    stats["valid"] = False
    print(f"Updated stats: {stats}")

    return 0


if __name__ == '__main__':
    sys.exit(main())