from tkinter import *
from PIL import ImageTk, Image

def create_movie_title_section(parent):
    """Create movie title label and entry box"""
    movie_title_label = Label(parent, text="Movie Title:", font=("Aptos", 12, 'bold'))
    movie_title_label.grid(row=0, column=0, sticky=W, padx=(20,0), pady=(20,20))
    title_entry = Entry(parent, width=50)
    title_entry.grid(row=0, column=1, padx=(5,0), pady=(20,20))

def create_favorites_button(parent):
    """Create favorites button"""
    add_favorites_button = Button(parent, text="Add to Favorites", font=("Aptos", 10, 'bold'), bg="black", fg="white")
    add_favorites_button.grid(row=1, column=1, padx=(200, 0))

def create_search_criteria_section(parent):
    """Create movie search criteria label"""
    criteria_label = Label(parent, text="Search by one or more movie criteria:", font=("Aptos", 12, 'bold'))
    criteria_label.grid(row=2, column=0, columnspan=2, sticky=W, padx=(20,0), pady=(20, 20))

def create_genre_section(parent):
    """Create genre label and entry box"""
    genre_label = Label(parent, text="Genre:", font=("Aptos", 12, 'bold'))
    genre_label.grid(row=3, column=0, sticky=W, padx=(20,0))
    genre_entry = Entry(parent, width=50)
    genre_entry.grid(row=3, column=1, padx=(20,20))

def create_release_date_section(parent):
    """Create release date label and entry box"""
    release_date_label = Label(parent, text="Release Date:", font=("Aptos", 12, 'bold'))
    release_date_label.grid(row=5, column=0, sticky=W, padx=(20,0))
    release_date_entry = Entry(parent, width=50)
    release_date_entry.grid(row=5, column=1, padx=(20,20))
    
def create_rating_section(parent):
    """Create rating label and entry box"""
    rating_label = Label(parent, text="Rating:", font=("Aptos", 12, 'bold'))
    rating_label.grid(row=7, column=0, sticky=W, padx=(20,0))
    rating_entry = Entry(parent, width=50)
    rating_entry.grid(row=7, column=1, padx=(20,20))
    
def create_keyword_section(parent):
    """Create keyword label and entry box"""
    actor_label = Label(parent, text="Keyword:", font=("Aptos", 12, 'bold'))
    actor_label.grid(row=9, column=0, sticky=W, padx=(20,0))
    actor_entry = Entry(parent, width=50)
    actor_entry.grid(row=9, column=1, padx=(20,20))
        
def create_language_section(parent):
    """Create language label and entry box"""
    director_label = Label(parent, text="Language:", font=("Aptos", 12, 'bold'))
    director_label.grid(row=11, column=0, sticky=W, padx=(20,0))
    director_entry = Entry(parent, width=50)
    director_entry.grid(row=11, column=1, padx=(20,20))  
    
def open_search_window():
    """Open a new top-level window and populate it with various search-related sections for the movie explorer application."""
    search_window = Toplevel()
    search_window.title("Movie Explorer")
    create_movie_title_section(search_window)
    create_favorites_button(search_window)
    create_search_criteria_section(search_window)
    create_genre_section(search_window)
    create_release_date_section(search_window)
    create_rating_section(search_window)
    create_keyword_section(search_window)
    create_language_section(search_window)

    # Create and grid the "Back", "Search", and "Exit" buttons.
    back_button = Button(search_window, text="Back", font=("Aptos", 12, 'bold'), bg="black", fg="white", command=search_window.destroy)
    back_button.grid(row=13, column=0, pady=(20,20))
    search_button = Button(search_window, text="Search", font=("Aptos", 12, 'bold'), bg="black", fg="white")
    search_button.grid(row=13, column=1, pady=(20,20))
    exit_button = Button(search_window, text="Exit", font=("Aptos", 12, 'bold'), bg="black", fg="white", command=search_window.quit)
    exit_button.grid(row=13, column=2, padx=(20,40), pady=(20,20))

# Initialize the main window
root = Tk()
root.title("Movie Explorer")

# Load and resize images for the age selection buttons using Pillow
under_18_img = Image.open("Not 18 Minor Image.png")
under_18_img = under_18_img.resize((100, 100))  # Resizing to 100x100 pixels
under_18_photo = ImageTk.PhotoImage(under_18_img)

adult_img = Image.open("18 Adult Image.png")
adult_img = adult_img.resize((100, 100))  # Resizing to 100x100 pixels
adult_photo = ImageTk.PhotoImage(adult_img)

# Create the frame to hold the age selection images and buttons
selection_frame = Frame(root)
selection_frame.pack(pady=20)

# Create labels for the age selection images
under_18_label = Label(selection_frame, image=under_18_photo)
under_18_label.pack(side=LEFT, padx=20)

adult_label = Label(selection_frame, image=adult_photo)
adult_label.pack(side=RIGHT, padx=20)

# Create buttons and place them under the images
under_18_button = Button(root, text="Under 18",font=("Aptos", 12, 'bold'),  bg="black", fg="white", command=open_search_window)
under_18_button.pack(side=LEFT, padx=20, pady=10)

adult_button = Button(root, text="Adult 18+", bg="black", font=("Aptos", 12, 'bold'), fg="white", command=open_search_window)
adult_button.pack(side=RIGHT, padx=20, pady=10)

# Start the main loop
root.mainloop()