# Import required libraries
import tkinter as tk
import calendar
import datetime

# Define a class for the Calendar application
class CalendarApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        # Create a Text widget to display the calendar
        self.calendar = tk.Text(self, height=10, width=25)
        self.calendar.pack(side=tk.LEFT)

        # Create an Entry widget for user to input date
        self.date_entry = tk.Entry(self, width=10)
        self.date_entry.pack()
        self.date_entry.insert(0, "DD-MM-YYYY")  # Placeholder text

        # Create a Button to go to the calendar view based on user input date
        self.go_to_date_button = tk.Button(self, text="Go to Date", command=self.go_to_date)
        self.go_to_date_button.pack()

        # Display the calendar on initialization
        self.display_calendar()

    def display_calendar(self, input_date=None):
        # Get the current year and month or use the provided input date
        if input_date is None:
            year = calendar.datetime.date.today().year
            month = calendar.datetime.date.today().month
        else:
            year = input_date.year
            month = input_date.month

        # Generate the calendar for the specified year and month
        cal = calendar.month(year, month)

        # Clear the previous content and display the new calendar
        self.calendar.delete('1.0', tk.END)

        # Add a remark for the current day
        today = datetime.date.today()
        cal_with_remark = cal.replace(str(today.day), f"[{today.day:^2}]")

        self.calendar.insert(tk.END, cal_with_remark)

    def go_to_date(self):
        # Go to the calendar view based on the user-input date
        try:
            input_date = datetime.datetime.strptime(self.date_entry.get(), "%d-%m-%Y").date()
            self.display_calendar(input_date)
        except ValueError:
            self.calendar.delete('1.0', tk.END)
            self.calendar.insert(tk.END, "Invalid date format")

# Define a class for the Calculator application
class CalculatorApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        # Create Entry widget for number input
        self.number_entry = tk.Entry(self, width=10)
        self.number_entry.grid(row=0, column=0)

        # Create dropdown menu for time units
        self.unit_dropdown = tk.StringVar()
        self.unit_dropdown.set("minutes")
        unit_options = ["minutes", "days", "weeks", "months", "years"]
        self.unit_menu = tk.OptionMenu(self, self.unit_dropdown, *unit_options)
        self.unit_menu.grid(row=0, column=1)

        # Create dropdown menu for time position
        self.position_dropdown = tk.StringVar()
        self.position_dropdown.set("ago")
        position_options = ["ago", "later"]
        self.position_menu = tk.OptionMenu(self, self.position_dropdown, *position_options)
        self.position_menu.grid(row=0, column=2)

        # Create a button to calculate the date
        self.calculate_button = tk.Button(self, text="Calculate", width=10, command=self.calculate_date)
        self.calculate_button.grid(row=0, column=3)

        # Create a list of buttons for numeric and operation input
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create and place the buttons on the grid
        for i, button_text in enumerate(self.buttons):
            button = tk.Button(self, text=button_text, width=5)
            button.grid(row=i // 4 + 1, column=i % 4)
            button.bind('<Button-1>', self.button_click)

        # Create a label to display the result
        self.result = tk.Label(self, text="Result:")
        self.result.grid(row=5, column=0, columnspan=4)

    def button_click(self, event):
        # Handle button clicks
        text = event.widget.cget("text")
        if text == "=":
            # Calculate result when "=" button is pressed
            expression = self.number_entry.get()
            try:
                result = eval(expression)
                self.result.config(text="Result: " + str(result))
            except:
                self.result.config(text="Invalid Expression")
        elif text == "C":
            # Clear the entry when "C" button is pressed
            self.number_entry.delete(0, tk.END)
        else:
            # Append the button text to the entry
            self.number_entry.insert(tk.END, text)
            if text == "Calculate":  # Check if the button text is "Calculate"
                # Trigger date calculation when "Calculate" button is pressed
                self.calculate_date()

    def calculate_date(self):
        # Calculate the date based on user input
        try:
            number = float(self.number_entry.get())
            unit = self.unit_dropdown.get()
            position = self.position_dropdown.get()

            today = datetime.date.today()
            delta = self.get_timedelta(number, unit, position)
            result_date = today + delta
            
            # Format the result date as "day - month - year"
            formatted_date = result_date.strftime("%d - %b - %Y")
            
            self.result.config(text="Result: " + formatted_date)
        except:
            self.result.config(text="Invalid Expression")

    def get_timedelta(self, number, unit, position):
        # Calculate timedelta based on the selected unit and position
        if unit == "minutes":
            delta = datetime.timedelta(minutes=number)
        elif unit == "days":
            delta = datetime.timedelta(days=number)
        elif unit == "weeks":
            delta = datetime.timedelta(weeks=number)
        elif unit == "months":
            delta = datetime.timedelta(days=30.44 * number)
        elif unit == "years":
            delta = datetime.timedelta(days=365.25 * number)

        # Adjust timedelta based on position (ago/later)
        if position == "ago":
            delta *= -1

        return delta

# Create the main application window
root = tk.Tk()

# Create the calendar side
calendar_frame = tk.Frame(root)
calendar_app = CalendarApp(calendar_frame)
calendar_frame.pack(side=tk.LEFT)

# Create the calculator side
calculator_frame = tk.Frame(root)
calculator_app = CalculatorApp(calculator_frame)
calculator_frame.pack(side=tk.RIGHT)

# Run the application
root.mainloop()
