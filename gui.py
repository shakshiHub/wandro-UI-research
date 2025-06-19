# gui.py
import tkinter as tk
from tkintermapview import TkinterMapView
import requests

def geocode_address(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json"}
    headers = {"User-Agent": "tkintermapview-app"}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon

def show_map(curr_location, destination="San Jose State University"):
    map_window = tk.Toplevel()
    map_window.title("Map View")
    map_window.geometry("1000x500")

    map_widget = TkinterMapView(map_window, corner_radius=0)
    map_widget.pack(fill="both", expand=True)

    lat, lon = geocode_address(curr_location)
    dest_lat, dest_lon = geocode_address(destination)

    mid_lat = (lat + dest_lat) / 2
    mid_lon = (lon + dest_lon) / 2
    map_widget.set_position(mid_lat, mid_lon)
    map_widget.set_zoom(10)

    map_widget.set_marker(lat, lon, text="Current Location")
    map_widget.set_marker(dest_lat, dest_lon, text=destination)
    map_widget.set_path([(lat, lon), (dest_lat, dest_lon)])
