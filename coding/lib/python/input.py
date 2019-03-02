"""Implement reading from stdin."""

if __name__ == "__main__":
    size = int(input().strip())
    array = input().strip().split()
    array = [int(array[i]) for i in range(size)]
    print(array)
