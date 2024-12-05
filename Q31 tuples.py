# Define some coordinates using tuples
point_1 = (2, 3)
point_2 = (5, 7)
point_3 = (0, -4)

# Print the coordinates
print(f"Point 1: {point_1}")
print(f"Point 2: {point_2}")
print(f"Point 3: {point_3}")

# Access individual elements
x1, y1 = point_1
print(f"Point 1 - x: {x1}, y: {y1}")

# Calculate the distance between two points
import math

def calculate_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

distance = calculate_distance(point_1, point_2)
print(f"Distance between Point 1 and Point 2: {distance:.2f}")

# Create a list of points
points = [point_1, point_2, point_3]

# Find the point with the largest x-coordinate
largest_x_point = max(points, key=lambda p: p[0])
print(f"Point with the largest x-coordinate: {largest_x_point}")

# Find the point closest to the origin (0, 0)
origin = (0, 0)
closest_to_origin = min(points, key=lambda p: calculate_distance(p, origin))
print(f"Point closest to the origin: {closest_to_origin}")

# Example of immutability
try:
    point_1[0] = 10  # Attempt to modify the tuple
except TypeError as e:
    print(f"Error: {e}")
