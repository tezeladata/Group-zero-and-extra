import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Some function we will need later:
    def points_to_triangle(point1, point2, point3):
        triangle = [list(point1), list(point2), list(point3)]
        return triangle

    def triangle_to_circumcenter(triangle):
        x, y, z = complex(triangle[0][0], triangle[0][1]), complex(triangle[1][0], triangle[1][1]), complex(triangle[2][0], triangle[2][1])
        w = z - x
        w /= y - x
        c = (x - y) * (w - abs(w)**2) / 2j / w.imag - x
        radius = abs(c + x)
        return ((0 - c.real, 0 - c.imag), radius)

    def get_distance(point1, point2):
        distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
        return distance

    def gen_delaunay(points):
        delaunay = [points_to_triangle([-5, -5], [-5, 10], [10, -5])]
        number_of_points = 0
        
        # part1
        while number_of_points < len(points): 
            point_to_add = points[number_of_points]
            delaunay_index = 0

            # part2
            invalid_triangles = [] 
            while delaunay_index < len(delaunay):
                circumcenter, radius = triangle_to_circumcenter(delaunay[delaunay_index])
                new_distance = get_distance(circumcenter, point_to_add)

                if new_distance < radius:
                    invalid_triangles.append(delaunay[delaunay_index])
                delaunay_index += 1

            # part3
            points_in_invalid = [] 
            for i in range(len(invalid_triangles)):
                delaunay.remove(invalid_triangles[i])
                for j in range(len(invalid_triangles[i])):
                    points_in_invalid.append(invalid_triangles[i][j])

            points_in_invalid = [list(x) for x in set(tuple(x) for x in points_in_invalid)]

            # part4
            for i in range(len(points_in_invalid)): 
                for j in range(i + 1, len(points_in_invalid)):
                    # count the number of times both of these are in the bad triangles
                    count_occurrences = 0
                    for k in range(len(invalid_triangles)):
                        count_occurrences += 1 * (points_in_invalid[i] in invalid_triangles[k]) * (points_in_invalid[j] in invalid_triangles[k])
                    
                    if count_occurrences == 1:
                        delaunay.append(points_to_triangle(points_in_invalid[i], points_in_invalid[j], point_to_add))
            
            number_of_points += 1

        return delaunay

    try: 
        n = int(input("Enter natural number: "))
        np.random.seed(5201314)
        xs = np.random.rand(n)
        ys = np.random.rand(n)
        points = list(zip(xs, ys))
        the_delaunay = gen_delaunay(points)
    except ValueError:
        print("Invalid input")
        return float("-inf")

    # Visualize the result
    plt.figure(figsize=(8, 8))
    for triangle in the_delaunay:
        triangle.append(triangle[0])  # To close the triangle
        t = np.array(triangle)
        plt.plot(t[:, 0], t[:, 1], 'b-')

    # Plot the points
    plt.plot(xs, ys, 'ro')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Delaunay Triangulation')
    plt.show()

if __name__ == "__main__":
    main()