# 7-Segment LED Digital Clock

## Overview

This repository contains a Python application that simulates a 7-segment LED digital clock using the `tkinter` library. The clock displays the current time in hours, minutes, and seconds using a 7-segment display representation, along with a greeting message and the current date.

## Features

- **7-Segment Display**: Represents hours, minutes, and seconds using a 7-segment LED display.
- **Greeting Message**: Displays a dynamic greeting based on the time of day (Good Morning, Good Afternoon, Good Evening, Good Night).
- **Date Display**: Shows the current date in a readable format.
- **Colon Toggle**: The colons between hours, minutes, and seconds toggle on and off every second.

## Requirements

- Python 3.x
- `tkinter` (standard library in Python 3)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShreyasGowda28/7-segment-clock.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd 7-segment-clock
   ```

3. **Ensure Python 3 and `tkinter` are Installed**:
   `tkinter` is included with Python 3.x installations. Ensure you have Python 3.x installed.

4. **Run the Application**:
   Execute the script with:
   ```bash
   python seven_segment_clock.py
   ```

## Code Structure

- **`SevenSegmentDisplay` Class**: 
  - Inherits from `tk.Canvas` to draw 7-segment displays.
  - `create_segments()`: Creates the graphical representation of the 7 segments.
  - `set_digit(digit)`: Sets the display to show a specific digit (0-9) by turning on the appropriate segments.

- **`update_clock()` Function**: 
  - Retrieves the current time and date.
  - Updates the 7-segment displays and greeting message.
  - Toggles colon visibility every second.

- **GUI Setup**:
  - Main window configuration with `tk.Tk()`.
  - Creates instances of `SevenSegmentDisplay` for hours, minutes, and seconds.
  - Adds labels for colons, greeting, and date.
  - Starts the clock update loop with `update_clock()`.

## Future Enhancements

- **Customizable Colors**: Allow users to select different colors for segments and text.
- **Additional Time Formats**: Support for 12-hour or 24-hour time formats.
- **Alarm Functionality**: Integrate an alarm feature with customizable alerts.
- **GUI Improvements**: Enhance the graphical interface with animations or additional themes.

## License

This project is open-source and free for personal or educational use. For commercial use, please contact the author.
