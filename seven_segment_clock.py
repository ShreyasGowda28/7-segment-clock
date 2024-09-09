import tkinter as tk
import time

class SevenSegmentDisplay(tk.Canvas):
    def __init__(self, master, color="red", **kwargs):
        super().__init__(master, **kwargs)
        self.color = color
        self.segments = self.create_segments()

    def create_segments(self):
        # Segment positions: A, B, C, D, E, F, G (7 segments)
        segments = {
            "A": self.create_polygon(20, 10, 100, 10, 80, 30, 40, 30, fill="black"),
            "B": self.create_polygon(90, 20, 110, 20, 110, 100, 90, 80, fill="black"),
            "C": self.create_polygon(90, 110, 110, 110, 110, 190, 90, 170, fill="black"),
            "D": self.create_polygon(20, 190, 100, 190, 80, 170, 40, 170, fill="black"),
            "E": self.create_polygon(10, 110, 30, 110, 30, 190, 10, 170, fill="black"),
            "F": self.create_polygon(10, 20, 30, 20, 30, 100, 10, 80, fill="black"),
            "G": self.create_polygon(20, 100, 100, 100, 80, 120, 40, 120, fill="black"),
        }
        return segments

    def set_digit(self, digit):
        # Define segment activation for each digit (0-9)
        digit_segments = {
            "0": ["A", "B", "C", "D", "E", "F"],
            "1": ["B", "C"],
            "2": ["A", "B", "G", "E", "D"],
            "3": ["A", "B", "G", "C", "D"],
            "4": ["F", "G", "B", "C"],
            "5": ["A", "F", "G", "C", "D"],
            "6": ["A", "F", "E", "D", "C", "G"],
            "7": ["A", "B", "C"],
            "8": ["A", "B", "C", "D", "E", "F", "G"],
            "9": ["A", "B", "C", "D", "F", "G"],
        }
        # Turn off all segments
        for segment in self.segments.values():
            self.itemconfig(segment, fill="black")
        # Turn on the segments needed for the digit
        for segment in digit_segments.get(digit, []):
            self.itemconfig(self.segments[segment], fill=self.color)

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    hours, minutes, seconds = current_time.split(":")

    # Set digits for hours
    hour_left.set_digit(hours[0])
    hour_right.set_digit(hours[1])
    # Set digits for minutes
    minute_left.set_digit(minutes[0])
    minute_right.set_digit(minutes[1])
    # Set digits for seconds
    second_left.set_digit(seconds[0])
    second_right.set_digit(seconds[1])

    # Toggle colon visibility
    colon_visibility = ":" if int(time.time()) % 2 == 0 else " "
    label_colon1.config(text=colon_visibility)
    label_colon2.config(text=colon_visibility)

    # Display greeting based on the time of day
    hour = int(hours)
    if 5 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    elif 18 <= hour < 22:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"
    label_greeting.config(text=greeting)

    # Display the current date
    current_date = time.strftime("%A, %B %d, %Y")  # Day, Month Date, Year format
    label_date.config(text=current_date)

    # Update every 1 second
    root.after(1000, update_clock)

# Setting up the main window
root = tk.Tk()
root.title("Advanced 7-Segment LED Digital Clock")
root.configure(bg="black")

# Creating the clock digits with custom colors
segment_color = "cyan"
hour_left = SevenSegmentDisplay(root, width=120, height=210, bg="black", highlightthickness=0, color=segment_color)
hour_left.grid(row=0, column=0, padx=10)
hour_right = SevenSegmentDisplay(root, width=120, height=210, bg="black", highlightthickness=0, color=segment_color)
hour_right.grid(row=0, column=1, padx=10)

# Adding colon labels between hours, minutes, and seconds
label_colon1 = tk.Label(root, text=":", font=("Arial", 80), fg=segment_color, bg="black")
label_colon1.grid(row=0, column=2, padx=5)

minute_left = SevenSegmentDisplay(root, width=120, height=210, bg="black", highlightthickness=0, color=segment_color)
minute_left.grid(row=0, column=3, padx=10)
minute_right = SevenSegmentDisplay(root, width=120, height=210, bg="black", highlightthickness=0, color=segment_color)
minute_right.grid(row=0, column=4, padx=10)

label_colon2 = tk.Label(root, text=":", font=("Arial", 80), fg=segment_color, bg="black")
label_colon2.grid(row=0, column=5, padx=5)

second_left = SevenSegmentDisplay(root, width=120, height=210, bg="black", highlightthickness=0, color=segment_color)
second_left.grid(row=0, column=6, padx=10)
second_right = SevenSegmentDisplay(root, width=120, height=210, bg="black", highlightthickness=0, color=segment_color)
second_right.grid(row=0, column=7, padx=10)

# Greeting label
label_greeting = tk.Label(root, font=("Arial", 25, "italic"), bg="black", fg="light green")
label_greeting.grid(row=1, column=0, columnspan=8, pady=10)

# Date label
label_date = tk.Label(root, font=("Arial", 20), bg="black", fg="light blue")
label_date.grid(row=2, column=0, columnspan=8, pady=20)

# Start the clock update
update_clock()

# Running the main loop
root.mainloop()
