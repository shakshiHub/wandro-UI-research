# currently unused

'''import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Display")

image = Image.open("bunny_logo.png") # Replace with your image path
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.image = photo  # Keep a reference to prevent garbage collection
label.pack()

root.mainloop()
'''



'''



with mic as source:
    print("Say something!")
    # call recognizer object's listen method on source (speech) and save as AudioData object
    audio = r.listen(source)
    

try:
    print("You said:", r.recognize_google(audio))
except:
    print("Sorry, I didn’t catch that.")
'''


'''
hello_label = tk.Label(
    root,
    text="hello",
    font=("Arial", 24),
    fg="white",
    bg="black"
)
# center it in the window
hello_label.place(x=w//2, y=h//2, anchor="center")
'''


'''
image1 = Image.open("bunny_logo.png").resize((360,216))
image2 = Image.open("bunny_logo.png").resize((300, 180))
image = Image.open("bunny_logo.png").resize((240, 144))

photo = ImageTk.PhotoImage(image)
    
label = tk.Label(root, image=photo, bd=0)
label.pack(expand=True)       # ← expand the empty space
'''


'''
def cycle_images():
    global idx, direction
    # Update label
    label.config(image=photos[idx])
  
           # ← expand the empty space
    # Advance index
    idx += direction
    # If we've hit either end, reverse direction
    if idx == len(photos) - 1 or idx == 0:
        direction *= -1
    # Schedule next update in 1000 ms (1 sec)
    root.after(1000, cycle_images)

# --- Start the loop and run ---
cycle_images()
'''


'''for i in range(3):
    label.config(image=photos[i])
    label.update()
    time.sleep(1)   
'''