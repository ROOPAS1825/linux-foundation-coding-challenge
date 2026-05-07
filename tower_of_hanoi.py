# Tower of Hanoi using Recursion
# Linux Foundation Mentorship Coding Challenge

def tower_of_hanoi(n, source, destination, auxiliary):

    # Base case
    if n == 1:
        print(f"Move disk 1 from {source} -> {destination}")
        return

    # Recursive call
    tower_of_hanoi(n - 1, source, auxiliary, destination)

    # Move current disk
    print(f"Move disk {n} from {source} -> {destination}")

    # Recursive call again
    tower_of_hanoi(n - 1, auxiliary, destination, source)


num_disks = 3

print("Tower of Hanoi Solution:\n")

tower_of_hanoi(num_disks, "A", "C", "B")
