import tkinter as tk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk
import speech_recognition as sr
import threading
import requests
import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Globals
w, h = 1000, 500
listening_for_command = False

# GUI setup
root = tk.Tk()
root.title("carplay-interface")
root.configure(bg='black')
x = (root.winfo_screenwidth() - w) // 2
y = (root.winfo_screenheight() - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")

# Load images
largest_photo_w, largest_photo_l = 360, 216
photo_sizes = [
    (largest_photo_w, largest_photo_l),
    (round(largest_photo_w * .85), round(largest_photo_l * .85)),
    (round(largest_photo_w * .7), round(largest_photo_l * .7)),
]

photos = []
for size in photo_sizes:
    img = Image.open("images/bunny_logo.png").resize(size)
    photo = ImageTk.PhotoImage(img)
    photos.append(photo)

label = tk.Label(root, bd=0, bg='black', width=largest_photo_w, height=largest_photo_l)
label.pack(expand=True)

i = 0
direction = 1

def logo_animation_cycle():
    global i, direction
    label.config(image=photos[i])
    if i == len(photos) - 1:
        direction = -1
    elif i == 0:
        direction = 1
    i += direction
    label.after(700, logo_animation_cycle)

# Voice recognition
r = sr.Recognizer()
mic = sr.Microphone()

def geocode_address(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json"}
    headers = {"User-Agent": "tkintermapview-app"}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon

def show_map():
    map_window = tk.Toplevel(root)
    map_window.title("Navigation - SJSU")
    map_window.configure(bg='black')
    map_window.geometry(f"{w}x{h}+{x}+{y}")

    # Step 1: Create but DON'T pack yet
    map_widget = TkinterMapView(map_window, corner_radius=0)

    # Step 2: Geocode and configure
    curr_location = "34891 Perry Rd, Union City, CA, 94587, USA"
    lat, lon = geocode_address(curr_location)
    sjsu_lat, sjsu_lon = geocode_address("San Jose State University")

    mid_lat = (lat + sjsu_lat) / 2
    mid_lon = (lon + sjsu_lon) / 2
    map_widget.set_position(mid_lat, mid_lon)
    map_widget.set_zoom(10)
    map_widget.set_marker(lat, lon, text="Current Location")
    map_widget.set_marker(sjsu_lat, sjsu_lon, text="SJSU")
    map_widget.set_path([(lat, lon), (sjsu_lat, sjsu_lon)])

    # Step 3: Now pack it after everything is set
    map_widget.pack(fill="both", expand=True)


def callback(recognizer, audio):
    global listening_for_command
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {text}")

        if not listening_for_command and "hey bunny" in text:
            print("Woke up. Listening for next command...")
            listening_for_command = True
            logo_animation_cycle()

        elif listening_for_command:
            if "take me to san jose state university" in text:
                print("Opening map to SJSU...")
                show_map()
                listening_for_command = False
            else:
                print("Heard command but not recognized. Still listening...")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")

# Start voice recognition in background
stop_listening = r.listen_in_background(mic, callback)

# Start GUI
label.config(image=photos[0])
root.mainloop()
