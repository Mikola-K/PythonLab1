class Ship:

    number_of_transportation = 0

    def __init__ (self, name = "", number_of_containers = 0, water_capacity = 0, cruising_speed = 0, number_of_crew  = 0, board_hight = 0, swimming_range = 0):
        self.name = name
        self.number_of_containers = number_of_containers
        self.water_capacity = water_capacity
        self.cruising_speed = cruising_speed
        self.number_of_crew = number_of_crew
        self.board_hight = board_hight
        self.swimming_range = swimming_range
        Ship.number_of_transportation += 1 
    
    def __del__ (self):
        pass 
    
    def __str__ (self):
        return f"Name: {self.name}\n " \
               f"Number of containers: {self.number_of_containers}\n " \
               f"Water capacity: {self.water_capacity}\n " \
               f"Cruising speed: {self.cruising_speed}\n " \
               f"Number of crew: {self.number_of_crew}\n " \
               f"Board hight: {self.board_hight}\n " \
               f"Swiming range: {self.swimming_range}\n" 

    @staticmethod
    def print_amount_of_transportation():
        print(f"Number of transportation: {Ship.number_of_transportation}")

def main():

    First_ship = Ship("Titanik", 5, 48, 23, 2208, 6, 2000)
    Second_ship = Ship("Kroha", 3, 23, 40, 14, 3, 3000)
    Third_ship = Ship ("Symphony_of_the_Seas", 0, 230, 59, 5400, 10, 4000)

    print(First_ship)
    print(Second_ship)
    print(Third_ship)

    Ship.print_amount_of_transportation()

if __name__ == "__main__":
    main()