
def calculate_average(marks):
    """Return the average of the given marks."""
    return sum(marks) / len(marks)


marks = [65, 80, 45, 90, 70]

average = calculate_average(marks)

print(f"Marks: {marks}")
print(f"Class average: {average}")
print(f"Average again: {calculate_average(marks)}")
