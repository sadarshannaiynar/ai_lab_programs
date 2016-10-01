class City:
    def __init__(self, label):
        self.label = label
        self.neighbours = list()
        self.neighbours_distance = list()

    def add_neighbour(self, city, distance):
        self.neighbours.append((city, distance))
        if (self, distance) not in city.neighbours:
            city.add_neighbour(self, distance)
        self.neighbours.sort(key=lambda pair: pair[1])

visited = list()

def find_next_nearest_neighbour(city):
    global visited
    for i in city.neighbours:
        if i[0] not in visited:
            visited.append(i[0])
            find_next_nearest_neighbour(i[0])
            break
    return

city_A = City('A')
city_B = City('B')
city_C = City('C')
city_D = City('D')
city_E = City('E')

city_A.add_neighbour(city_B, 5000)
city_A.add_neighbour(city_C, 2000)
city_A.add_neighbour(city_D, 3000)
city_A.add_neighbour(city_E, 4000)

city_B.add_neighbour(city_C, 2000)
city_B.add_neighbour(city_D, 1000)
city_B.add_neighbour(city_E, 3000)

city_C.add_neighbour(city_D, 6000)
city_C.add_neighbour(city_E, 2000)

city_D.add_neighbour(city_E, 1000)

visited.append(city_A)
find_next_nearest_neighbour(city_A)
print('->'.join([i.label for i in visited]))
