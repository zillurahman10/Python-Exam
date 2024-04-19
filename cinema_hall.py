class Star_Cinema: 
    def __init__(self):
        self._hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self._hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self._show_list.append(show)
        self._allocate_seats()
        self._seats[id] = self._allocate_seats()

    def _allocate_seats(self):
        seats = []
        for index in range(self._rows):
            row = ['Free'] * self._cols
            seats.append(row)
        return seats
    
    def book_seats(self, show_id, seat_list):
        if show_id in self._seats:
            for row, col in seat_list:
                if 0 <= row < self._rows and 0 <= col < self._cols:
                    if self._seats[show_id][row][col] == 'Free':
                        self._seats[show_id][row][col] = 'Booked'
                    else:
                        print(f"Seat at row {row}, col {col} is already booked.")
                else:
                    print(f"Invalid seat position: row {row}, col {col}.")
        else:
            print(f"Show with ID {show_id} is not found.")

    def view_show_list(self):
        for show_id, movie_name, time in self._show_list:
            print(f"ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id in self._seats:
            print(f"Available seats:")
            for row in range(self._rows):
                for col in range(self._cols):
                    if self._seats[show_id][row][col] == 'Free':
                        print(f"Row {row}, Col {col}")
        else:
            print(f"Show with ID {show_id} is not found.")

cinema = Star_Cinema()

hall1 = Hall(rows=10, cols=10, hall_no=1)
hall1.entry_show(id=1, movie_name="Your Name", time="18:00")
hall1.entry_show(id=2, movie_name="Suzume no tojimari", time="20:00")

cinema.entry_hall(rows=10, cols=10, hall_no=1)

print("Shows Running:")
cinema._hall_list[0].view_show_list()

print("Available Seats for Show ID 1:")
cinema._hall_list[0].view_available_seats(1)

print("Tickets for Show ID 1:")
cinema._hall_list[0].book_seats(1, [(0, 0), (0, 1), (1, 1)])
