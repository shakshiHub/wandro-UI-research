'''
# attempting map view
import tkinter as tk
from tkintermapview import TkinterMapView
import requests

curr_location = "34891 Perry Rd, Union City, CA, 94587, USA"
# getting coordinateS from address, simulating "current location"
def geocode_address(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json"}
    headers = {"User-Agent": "tkintermapview-app"}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon

w, h = 1000, 500

# create main window
root = tk.Tk()
root.title("carplay-interface")
root.configure(bg='black')

x = (root.winfo_screenwidth() - w) // 2
y = (root.winfo_screenheight() - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")

map_widget = TkinterMapView(root, corner_radius=0)
map_widget.pack(fill="both", expand=True)

# geocode the address and set position
lat, lon = geocode_address(curr_location)
sjsu_lat, sjsu_lon = geocode_address("San Jose State University")
map_widget.set_position(lat, lon)
map_widget.set_marker(lat, lon)


mid_lat = (lat + sjsu_lat) / 2
mid_lon = (lon + sjsu_lon) / 2
map_widget.set_position(mid_lat, mid_lon)
map_widget.set_zoom(10)

# Markers
marker_curr = map_widget.set_marker(lat, lon, text="Current Location")
marker_sjsu = map_widget.set_marker(sjsu_lat, sjsu_lon, text="SJSU")

# Draw path between points
path = map_widget.set_path([(lat, lon), (sjsu_lat, sjsu_lon)])

# Mainloop
root.mainloop()

'''
# all work done in main.py until organized in seperate files
import speech_recognition as sr
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
import threading

# silencing warnings
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# mic & speech recognition setup
r = sr.Recognizer() # creating instance of sr's recognizer class
mic = sr.Microphone() # creating instance of sr's microphone class

# window dimensions
w, h = 1000, 500

# create main window
root = tk.Tk()
root.title("carplay-interface")
root.configure(bg='black')

# logic for centering main window on screen
x = (root.winfo_screenwidth() - w) // 2
y = (root.winfo_screenheight() - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")

# photo sizing
largest_photo_w = 360
largest_photo_l = 216

photo_sizes = [
    (largest_photo_w, largest_photo_l),
    (round(largest_photo_w * .85), round(largest_photo_l * .85)),
    (round(largest_photo_w * .7), round(largest_photo_l * .7)),
]

# load and resize each image once
photos = []
for size in photo_sizes:
    img = Image.open("images/bunny_logo.png").resize(size)
    photo = ImageTk.PhotoImage(img)
    photos.append(photo)

i = 0
direction = 1  # +1 = forward, -1 = backward

label = tk.Label(root, bd=0, bg='black', width=largest_photo_w, height=largest_photo_l)
label.pack(expand=True)

def logo_animation_cycle():
    global i, direction

    # display the current image
    label.config(image=photos[i])

    # if at last image, reverse
    if i == len(photos) - 1:
        direction = -1

    # if at first image, go forward again
    elif i == 0:
        direction = 1

    # advance
    i += direction
    label.after(700, logo_animation_cycle)

label.config(image=photos[0])

def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio).lower()
        if "hey bunny" in text:
            logo_animation_cycle()
    except sr.UnknownValueError:
        print("Sorry, I didn’t understand that.")
    except sr.RequestError as e:
        print(f"API error: {e}")

# Start listening in the background
stop_listening = r.listen_in_background(mic, callback)

root.mainloop()





