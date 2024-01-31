import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import IntVar,StringVar
from tkinter import PhotoImage, Button
from ttkbootstrap.icons import Icon
from tkinter.font import Font
import time
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import numpy as np  # Make sure to import numpy
# plot function is created for  
# plotting the graph in  
# tkinter window 

plots_created = False

def plot():
    global plots_created
    if plots_created:
        return
    # the figure that will contain the plots
    fig = Figure(figsize=(10, 5), dpi=100)  # Adjusted for a wider figure

    # list of squares for the first plot
    y = [i**2 for i in range(101)]

    # Adding the first subplot for squares
    plot1 = fig.add_subplot(121)  # 1 row, 2 columns, first plot
    plot1.plot(y)
  

    # Data for the second plot (sine wave)
    x = np.linspace(0, 2 * np.pi, 100)
    y2 = np.sin(x)

    # Adding the second subplot for sine wave
    plot2 = fig.add_subplot(122)  # 1 row, 2 columns, second plot
    plot2.plot(x, y2)
    
    # Creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=blank_tab)
    canvas.draw()

    # Placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # Creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, blank_tab)
    toolbar.update()

    # Placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

    # Activate zoom mode
    toolbar.zoom()

    plots_created = True


def gear_label_click(event):
    # Assuming gears are numbered 1-6 and 'N' for Neutral.
    # You can adjust the list to match the actual gears of your car.
    gears = ['N', '1', '2', '3', '4', '5', '6', 'R']  # 'R' for Reverse
    current_gear = event.widget.cget("text")
    next_gear_index = (gears.index(current_gear) + 1) % len(gears)
    event.widget.config(text=gears[next_gear_index])

def create_gear_display(master):
    gear_frame = ttk.Frame(master, padding=5)
    gear_frame.pack(side='left', expand=True, padx=30)
    
    gear_label = ttk.Label(gear_frame, text="N", font=("Helvetica", 72, "bold"), bootstyle="light")
    gear_label.pack(pady=20)
    
    # Bind the mouse click event to the gear label
    gear_label.bind("<Button-1>", gear_label_click)
    
    return gear_label

def create_data_labelframe(master, text, value):
    labelframe = ttk.LabelFrame(master, text=text, bootstyle="success")
    labelframe.pack(fill='x', expand='yes', padx=5,)
    value_label = ttk.Label(labelframe, text=value, anchor="center", bootstyle="light")
    value_label.pack()

def create_data_labelframe_right(master, text, value):
    labelframe = ttk.LabelFrame(master, text=text, bootstyle="warning")
    labelframe.pack(fill='x', expand='yes', padx=5)
    value_label = ttk.Label(labelframe, text=value, anchor="center", bootstyle="light")
    value_label.pack()

def start_stopwatch():
    global stopwatch_running, start_time
    if not stopwatch_running:
        stopwatch_running = True
        start_time = time.time()
        update_stopwatch()

def update_stopwatch():
    if stopwatch_running:
        elapsed_time = int(time.time() - start_time)
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_label.config(text=f"{hours}:{minutes:02d}:{seconds:02d}")
        app.after(1000, update_stopwatch)

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

# Function to handle progress bar dragging
def on_drag(event):
    widget_width = progressbar.winfo_width()
    new_value = int((event.x / widget_width) * 100)
    progress_var.set(new_value)
def update_progress(value):
    progress_var.set(value)  # Set the value of the progress_var

def on_tab_changed(event):
    selected_tab = notebook.tab(notebook.select(), "text")
    if selected_tab == "Stats":
        plot()

app = ttk.Window(title="UTA FSAE", themename="cyborg")
notebook = ttk.Notebook(app,bootstyle="light")
notebook.pack(expand=True, fill='both')

# Tab for your existing application
app_tab = ttk.Frame(notebook)
notebook.add(app_tab, text="Meters")

stopwatch_control = StringVar(value="stop")

sw_frame = ttk.Frame(app_tab)
sw_frame.pack(side="top", anchor="w", pady=5)  # anchor 'w' aligns to the left (west)

# Start and Stop Radio Buttons
start_rb = ttk.Radiobutton(master=sw_frame, text="", variable=stopwatch_control, value="start", command=start_stopwatch, bootstyle="success")
start_rb.pack(side="left", padx=5)

stop_rb = ttk.Radiobutton(master=sw_frame, text="", variable=stopwatch_control, value="stop", command=stop_stopwatch, bootstyle="danger")
stop_rb.pack(side="left", padx=5)

# Digital Stopwatch (Time Label)
stopwatch_running = False
start_time = 0

# Stopwatch Label
time_label = ttk.Label(master=sw_frame, font=("helvetica", 16), bootstyle="light")
time_label.pack(pady=10,side="right")

# Frame for car data information
info_frame = ttk.Frame(app_tab)
info_frame.pack(side="left", fill="y", padx=10)

# Labels for car data
create_data_labelframe(info_frame, "Average Speed", "0 M/S")
create_data_labelframe(info_frame, "Consumption", "0 M/L")
create_data_labelframe(info_frame, "Driveable Distance", "0 M/L")

# Frame for meters
meter_frame = ttk.Frame(app_tab)
meter_frame.pack(pady=20, expand=True)

large_font_meter=Font(family="Helvetica", size=28, weight="bold")
# First Meter (Speed)
meter = ttk.Meter(
    master=meter_frame,
    metersize=360,
    padding=5,
    amountused=130,
    amounttotal=300,
    metertype="semi",
    subtext="Speed",
    textfont="-size 40 -weight bold",
    subtextfont="-size 16",
    interactive=True,
    stripethickness=4,
    meterthickness=30,
    textright='mph',
    bootstyle="success"
)
meter.pack(side='left')

current_gear_label = create_gear_display(meter_frame)

# Second Meter (RPM)
meter_2 = ttk.Meter(
    master=meter_frame,
    metersize=360,
    padding=5,
    meterthickness=20,
    amountused=2,
    amounttotal=10,
    metertype="semi",
    subtext="RPM",
    interactive=True,
    stripethickness=27,
    textright='x1000',
    bootstyle="warning",
    textfont="-size 56 -weight bold",
    subtextfont="-size 16",
)
meter_2.pack(side='left')

right_info_frame = ttk.Frame(meter_frame)
right_info_frame.pack(side="right", fill="y", expand=True)

# Labelframes for car data on the right
create_data_labelframe_right(right_info_frame, "Odometer", "0 m")
create_data_labelframe_right(right_info_frame, "Od. Partial", "0 m")


# Frame for progress bar and temperature labels
progress_frame = ttk.Frame(app_tab)
progress_frame.pack(pady=10, padx=20)



cold_icon_image = PhotoImage(data=Icon.info)  # Update with the actual path to your cold icon
hot_icon_image = PhotoImage(data=Icon.warning)

# Cold Label
large_font = Font(family="Helvetica", size=14, weight="bold")

# Label with increased size
cold_label = ttk.Label(progress_frame, text="°C", bootstyle="primary", font=large_font)
cold_label.pack(side='left')

# Progress Bar
progress_var = IntVar(value=0)
progressbar = ttk.Progressbar(
    master=progress_frame,
    orient='horizontal',
    length=300,
    bootstyle="danger",
    variable=progress_var,
    maximum=100
)
progressbar.pack(side='left')
update_progress(25)
progressbar.bind('<B1-Motion>', on_drag)

# Hot Label
hot_label = ttk.Label(progress_frame, text="Hot (100°C)", image=hot_icon_image,bootstyle="danger")
hot_label.pack(side='left')

#--------------------------------------------2nd tab

blank_tab = ttk.Frame(notebook)
notebook.add(blank_tab, text="Stats")

# Button for plotting
notebook.bind("<<NotebookTabChanged>>", on_tab_changed)



app.mainloop()
