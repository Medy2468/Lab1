import math

def calc_distance(point1, point2):
    """
    Calculate and return the distance between two points.
    Each point is represented as a list containing its coordinates (x, y, z).
    """
    # Extract coordinates from the points
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    # Calculate the Euclidean distance between the points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    
    return distance

# Exemple d'utilisation
points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

distances = [calc_distance(p1, p2) for p1, p2 in zip(points1, points2)]
print("Calling function calc_distance with arguments",points1,points2)
print(distances)