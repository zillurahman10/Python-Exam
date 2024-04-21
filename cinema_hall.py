class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

    def __create_seats(self):
        seats = [['Free' for index in range(self.__cols)] for index in range(self.__rows)]
        return seats

    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)
        self.__show_list.append(show_info)

        self.__seats[show_id] = self.__create_seats()

    def book_seats(self, show_id, seats_to_book):
        if show_id in self.__seats:
            for seat in seats_to_book:
                row, col = seat
                if 1 <= row <= self.__rows and 1 <= col <= self.__cols:
                    if self.__seats[show_id][row - 1][col - 1] == 'Free':
                        self.__seats[show_id][row - 1][col - 1] = 'Booked'
                        print(f"Your seat {row}{chr(64 + col)} has been successfully.booked")
                    else:
                        print(f"Seat {row}{chr(64 + col)} is already booked.")
                else:
                    print(f"Invalid seat {row}{chr(64 + col)} for show ID {show_id}.")
        else:
            print(f"Show with ID {show_id} does not exist.")

    def __view_show_list(self):
        print("The shows which are running now:")
        for show_info in self.__show_list:
            print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def __view_available_seats(self, show_id):
        if show_id in self.__seats:
            print(f"Available seats for show ID {show_id}:")
            for row in range(self.__rows):
                for col in range(self.__cols):
                    if self.__seats[show_id][row][col] == 'Free':
                        print(f"Row {row + 1}, Seat {chr(65 + col)}")
        else:
            print(f"Show with ID {show_id} does not exist.")

class CounterReplica:
    def __init__(self, hall):
        self.__hall = hall

    def view_all_shows(self):
        self.__hall._Hall__view_show_list()

    def view_available_seats(self, show_id):
        self.__hall._Hall__view_available_seats(show_id)

    def book_tickets(self, show_id, seats_to_book):
        self.__hall.book_seats(show_id, seats_to_book)


hall1 = Hall(10, 10, 1)

hall1.entry_show("S1", "Your Name", "6:00 PM")
hall1.entry_show("S2", "Garden of words", "9:00 PM")

counter = CounterReplica(hall1)

print("All shows running:")
counter.view_all_shows()

print("Viewing available seats:")
counter.view_available_seats("S1")

print("Booking tickets:")
counter.book_tickets("S1", [(1, 1), (2, 2), (3, 3)])