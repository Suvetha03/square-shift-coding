class AeroplaneSeating:

    def __init__(self, seating_grid, passenger_id_list):
        self.seating_grid = seating_grid
        self.passenger_id_list = passenger_id_list
        self.aeroplane_seating = []

    # creating the seats
    def createSeating(self, seating_arrangement):
        print(seating_arrangement)
        for dim in seating_arrangement:
            seat_grid = []
            for i in range(dim[1]):
                seat_grid.append(['xx'] * dim[0])
            self.aeroplane_seating.append(seat_grid)

    # filling the Aisle seats
    def fillAisleSeats(self, passenger_id):
        i = j = 0
        k = -1
        index = 0
        for _ in passenger_id:
            try:
                self.aeroplane_seating[i][j][k] = passenger_id[index]
                index = index + 1
            except:
                pass
            if k == -1:
                i = i + 1
                k = 0
            else:
                k = -1
                if i == len(self.aeroplane_seating) - 1:
                    i = 0
                    j = j + 1

        return index

# Filling the window seats
    def fillWindowSeats(self, passenger_id):
        i = 0
        j = 0
        k = 0
        index = 0
        for _ in passenger_id:
            try:
                self.aeroplane_seating[i][j][k] = passenger_id[index]
                index = index + 1
            except:
                pass
            if i == 0:
                i = k = -1
            elif i == -1:
                i = k = 0
                j = j + 1

        return index

# Filling the middle seats
    def fillMiddleSeats(self, passenger_id):
        i = j = 0
        k = 1
        index = 0
        for _ in passenger_id:
            try:
                self.aeroplane_seating[i][j][k] = passenger_id[index]
                k = k + 1
                index = index + 1
            except:
                pass
            if k == len(self.aeroplane_seating[i][j]) - 1:
                k = 1
                i = i + 1

            if i == len(self.aeroplane_seating[i][j]) - 1:
                i = 0
                j = j + 1

        return index

    def displaySeating(self):
        for block in self.aeroplane_seating:
            for rows in block:
                print(rows)
            print("\n")
