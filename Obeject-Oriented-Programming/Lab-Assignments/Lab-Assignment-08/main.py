#Lab Activity No 7
#Programmed by: Mark Justine L. Apitan
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: June 22, 2024
import tkinter as tk
from tkinter import messagebox, ttk
from classes import Movie, Room, Record
from database_manager import MovieHouseDatabaseManager

import tkinter as tk
from tkinter import messagebox

class RecordWindow(tk.Toplevel):
    
    def __init__(self, parent, room, database_manager, record):
        super().__init__(parent)
        self.room = room
        self.database_manager = database_manager
        self.record = record
        self.title(f"Room {room[0]}")

        self.listbox_frame = tk.Frame(self)
        self.listbox_frame.pack(fill=tk.BOTH, expand=True)

        self.movies_list = tk.Listbox(self.listbox_frame, selectmode=tk.MULTIPLE)
        self.movies_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.movies_to_view_list = tk.Listbox(self.listbox_frame, selectmode=tk.MULTIPLE)
        self.movies_to_view_list.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Frame for buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill=tk.X)

        self.add_movie_button = tk.Button(self.button_frame, text="Add Movie", command=self.add_movie)
        self.add_movie_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        self.remove_movie_button = tk.Button(self.button_frame, text="Remove Movie", command=self.remove_movie)
        self.remove_movie_button.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5, pady=5)

        # Label for total cost
        self.total_cost_label = tk.Label(self, text="Total Cost: $0.00")
        self.total_cost_label.pack(fill=tk.X, padx=5, pady=5)

        # Frame for check-in/out buttons
        self.check_frame = tk.Frame(self)
        self.check_frame.pack(fill=tk.X)

        self.check_in_button = tk.Button(self.check_frame, text="Check In", command=self.check_in)
        self.check_in_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        self.check_out_button = tk.Button(self.check_frame, text="Check Out", command=self.check_out)
        self.check_out_button.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5, pady=5)

        self.populate_movies_list()

    def populate_movies_list(self):
        #self.movies_list.delete(0, tk.END)
        movies = self.database_manager.retrieve_movies([])
        for movie in movies:
            self.movies_list.insert(tk.END, f"{movie[0]} - {movie[1]} - {movie[2]} - ₱{movie[4]}")

            
    def add_movie(self):
        selected_indices = self.movies_list.curselection()
        # For each selected index, get the movie and insert it into movies_to_view_list
        for index in selected_indices:
            movie = self.movies_list.get(index)
            self.movies_to_view_list.insert(tk.END, movie)

    def remove_movie(self):
        selected_indices = self.movies_to_view_list.curselection()
        for index in selected_indices[::-1]:  # Reverse to handle multiple deletions correctly
            self.movies_to_view_list.delete(index)
        self.update_total_cost()


    def check_in(self):
        print("Checked in")
        self.update_buttons()
        total_cost = 0  # Initialize total_cost before the loop
        for i in range(self.movies_to_view_list.size()):
            movie = self.movies_to_view_list.get(i)
        # Assuming the price is always at the end after '₱'
            price_str = movie.split('₱')[-1]
            try:
                price = float(price_str)
                total_cost += price  # Add price to total_cost within the try block
            except ValueError:
                # Handle the case where the price is not a valid float
                print(f"Error: Invalid price '{price_str}' for movie '{movie}'")
     #Update the total cost label outside the loop
        self.total_cost_label.config(text=f"Total Cost: ₱{total_cost}")
    def check_out(self):
        print("Checked out")
        self.update_buttons()


    def update_buttons(self):
        has_records = bool(self.movies_to_view_list.size())
        self.check_in_button.config(state=tk.NORMAL if not has_records else tk.DISABLED)
        self.check_out_button.config(state=tk.NORMAL if has_records else tk.DISABLED)

class MovieHouseWindow(tk.Tk):
    def __init__(self, database_file_name):
        super().__init__()
        self._database_manager = MovieHouseDatabaseManager(database_file_name)

        self.title("Movie House")

        # Movie Registration Section
        tk.Label(self, text="Register").grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        tk.Label(self, text="Title").grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
        self.movie_title_entry = tk.Entry(self)
        self.movie_title_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Cost").grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
        self.cost_entry = tk.Entry(self)
        self.cost_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Genre").grid(row=3, column=0, sticky=tk.E, padx=10, pady=5)
        self.genre_entry = tk.Entry(self)
        self.genre_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self, text="Add Movie", command=self.add_movie)
        self.add_button.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)

        # Movies List Section
        tk.Label(self, text="Movies").grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.movies_list = tk.Listbox(self, width=50)
        self.movies_list.grid(row=6, column=0, columnspan=2, rowspan=6, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

        self.remove_button = tk.Button(self, text="Remove Movie", command=self.remove_movie)
        self.remove_button.grid(row=12, column=0, columnspan=2, padx=10, pady=5)

        # Genre Filter Section
        tk.Label(self, text="Filter by Genre").grid(row=5, column=2, columnspan=2, padx=10, pady=5)

        self.adventure_checkbutton = tk.Checkbutton(self, text="Adventure")
        self.adventure_checkbutton.grid(row=6, column=2, sticky=tk.W, padx=10, pady=5)

        self.comedy_checkbutton = tk.Checkbutton(self, text="Comedy")
        self.comedy_checkbutton.grid(row=7, column=2, sticky=tk.W, padx=10, pady=5)

        self.fantasy_checkbutton = tk.Checkbutton(self, text="Fantasy")
        self.fantasy_checkbutton.grid(row=8, column=2, sticky=tk.W, padx=10, pady=5)

        self.romance_checkbutton = tk.Checkbutton(self, text="Romance")
        self.romance_checkbutton.grid(row=9, column=2, sticky=tk.W, padx=10, pady=5)

        self.tragedy_checkbutton = tk.Checkbutton(self, text="Tragedy")
        self.tragedy_checkbutton.grid(row=10, column=2, sticky=tk.W, padx=10, pady=5)

        # Room Buttons Section
        tk.Label(self, text="Rooms").grid(row=0, column=5, padx=20, pady=5)

        self.room1_button = tk.Button(self, text="Room 1", command=lambda: self.open_record_window(1), width=15, height=2)
        self.room1_button.grid(row=1, column=5, padx=20, pady=5)

        self.room2_button = tk.Button(self, text="Room 2", command=lambda: self.open_record_window(2), width=15, height=2)
        self.room2_button.grid(row=2, column=5, padx=20, pady=5)

        self.room3_button = tk.Button(self, text="Room 3", command=lambda: self.open_record_window(3), width=15, height=2)
        self.room3_button.grid(row=3, column=5, padx=20, pady=5)

        self.room4_button = tk.Button(self, text="Room 4", command=lambda: self.open_record_window(4), width=15, height=2)
        self.room4_button.grid(row=4, column=5, padx=20, pady=5)

        self.populate_movies_list()

    def populate_movies_list(self):
        # Clear the movies_list
        self.movies_list.delete(0, tk.END)
        
        # Retrieve movies from the database
        movies = self._database_manager.retrieve_movies([])
        
        # Insert each movie into the movies_list
        for movie in movies:
            self.movies_list.insert(tk.END, f"{movie[0]} - {movie[1]} - {movie[2]} - ₱{movie[4]}")

    def add_movie(self):
        # Get the movie details from the input fields
        title = self.movie_title_entry.get()
        cost = float(self.cost_entry.get())
        genre = self.genre_entry.get()
        
        # Check if all fields are filled
        if title and cost and genre:
            # Register the movie in the database
            success = self._database_manager.register_movie(title, genre, cost)
            
            if success:
                # If registration is successful, update the movies_list and show a success message
                self.populate_movies_list()
                messagebox.showinfo("Success", "Movie added successfully!")
            else:
                # If registration fails, show an error message
                messagebox.showerror("Error", "Failed to add movie.")
        else:
            # If any field is empty, show an error message
            messagebox.showerror("Error", "Please fill all fields.")

    def remove_movie(self):
        # Get the index of the selected movie in the movies_list
        selected_movie_index = self.movies_list.curselection()
        
        if selected_movie_index:
            # Get the selected movie details
            selected_movie = self.movies_list.get(selected_movie_index[0])
            movie_id = int(selected_movie.split(' - ')[0])
            
            # Remove the movie from the database
            self._database_manager.remove_movie(movie_id)
            
            # Update the movies_list
            self.populate_movies_list()

    def open_record_window(self, room_id):
        # Retrieve the room details from the database
        room = next((r for r in self._database_manager.retrieve_rooms() if r[0] == room_id), None)
        
        if room:
            # Retrieve the record for the room from the database
            record = self._database_manager.retrieve_record(room_id)
            
            # Open the RecordWindow with the room, database_manager, and record
            RecordWindow(self, room, self._database_manager, record)

if __name__ == '__main__':
    # Create an instance of MovieHouseWindow and start the main event loop
    app = MovieHouseWindow('moviehouse.db')
    app.mainloop()
