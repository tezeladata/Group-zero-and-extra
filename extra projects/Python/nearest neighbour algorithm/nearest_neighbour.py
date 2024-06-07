import math
import numpy as np
import matplotlib.collections as mc
import matplotlib.pylab as pl
import random

def main():
    print("Hello, this algorithm finds smallest distance to visit all cities")
    print("First of all, we have to generate cities")

    random_seed = random.randint(0, 10000)
    np.random.seed(random_seed)
    N=int(input("How many cities do you want to have? "))
    x = np.random.rand(N)
    y = np.random.rand(N)

    points = zip(x, y)
    cities = list(points)
    
    # This function generates lines between cities
    def genlines(cities,itinerary):
        lines = []
        for j in range(0,len(itinerary) - 1):
            lines.append([cities[itinerary[j]],cities[itinerary[j + 1]]])

        return lines
    
    # This is main function to find nearest city:
    def findnearest(cities,idx,nnitinerary):
        point = cities[idx]
        mindistance = float('inf')
        minidx = - 1
        for j in range(0,len(cities)):
            distance = math.sqrt((point[0] - cities[j][0])**2 + (point[1] - cities[j][1])**2)
            
            if distance < mindistance and distance > 0 and j not in nnitinerary:
                mindistance = distance
                minidx = j
        
        return minidx 
    
    # This algorithm finds nearest neighbours for all cities
    def donn(cities,N):
        nnitinerary = [0]
        for j in range(0,N - 1):
            next = findnearest(cities,nnitinerary[len(nnitinerary) - 1],nnitinerary)
            nnitinerary.append(next)
        
        return nnitinerary
    
    # After we have this findnearest() function, we’re ready to implement the nearest neighbor algorithm. We will also see distance
    def howfar(lines):
        distance = 0
        for j in range(len(lines)):
            distance += math.sqrt((lines[j][1][0] - lines[j][0][0])**2 + (lines[j][1][1] - lines[j][0][1])**2)
        return distance
    
    def visualize(cities, itin, plottitle, thename):
        lc = mc.LineCollection(genlines(cities, itin), linewidths=2)
        fig, ax = pl.subplots()
        ax.add_collection(lc)
        ax.autoscale()
        ax.margins(0.1)
        pl.scatter(x, y)
        pl.title(plottitle)
        pl.xlabel('X Coordinate')
        pl.ylabel('Y Coordinate')
        pl.show()  # Display the plot in a window

    
    print("After the work of our algorithm, we can finally see the minimal distance to visit all of the cities")
    print(howfar(genlines(cities,donn(cities,N))))

    decision = input("Do you also want to see visual representation of lines? (Y/N) - ").lower() == "y"
    if decision:
        visualize(cities,donn(cities,N),'TSP - Nearest Neighbor','figure3')

    print("Thanks for attention!")


main()