import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os
import sys

# Total number of agents (including the new agent)
TOTAL_AGENTS = 25  # Here you define the total number of agents, updated for the new character

# Function to load images
def load_images():
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    agent_images = {}
    for agent_number in range(1, TOTAL_AGENTS + 1):  # Use the constant to include all agents
        image_path = os.path.join(base_path, "src", f"{agent_number}.png")
        image = Image.open(image_path)
        image = image.resize((200, 200))
        image = ImageTk.PhotoImage(image)
        agent_images[agent_number] = image
    return agent_images

# Function to assign agents to users
def assign_agents():
    agent_numbers = list(range(1, TOTAL_AGENTS + 1))  # Use the constant to include all agents
    random.shuffle(agent_numbers)
    assignments = {user: agent_numbers.pop() if agent_numbers else None for user in users}
    return assignments

# Function to display the assigned agent images
def show_images(agent_images):
    assignments = assign_agents()
    for i, user in enumerate(users):
        agent_number = assignments.get(user)
        if agent_number is not None:
            labels_images[i].config(image=agent_images[agent_number])
        else:
            labels_images[i].config(image=None)
        labels_names[i].config(text=user)

# Function to read names from the text file
def read_names_from_file(file):
    try:
        with open(file, 'r') as f:
            # Read lines, ignore those starting with # or empty lines
            names = [line for line in f.read().splitlines() if line and not line.startswith('#')]
        return names
    except FileNotFoundError:
        print(f"The file {file} was not found.")
        return []

# Main window configuration
root = tk.Tk()
root.title("Agent Assignment for Valorant")
root.configure(bg="#1f1f1f")  # Set the background color to dark mode

# Container for the images
frame_images = tk.Frame(root, bg='#1f1f1f')
frame_images.pack(pady=20)

# Read the names of the users from the text file
users = read_names_from_file("users.txt")

# Create labels to display images and names
labels_images = []
labels_names = []
for user in users:
    frame = tk.Frame(frame_images, bg='#1f1f1f')
    frame.pack(side="left", padx=10)
    
    label_image = tk.Label(frame, bg='#1f1f1f')
    label_image.pack()
    labels_images.append(label_image)

    label_name = tk.Label(frame, text=user, bg='#1f1f1f', fg='white')
    label_name.pack()
    labels_names.append(label_name)

# Button for re-roll
btn_reroll = tk.Button(root, text="Re-roll", command=lambda: show_images(agent_images), bg='#333333', fg='white', activebackground='#555555', activeforeground='white')
btn_reroll.pack(pady=10)

# Load images on startup
agent_images = load_images()
# Show the images and names on startup
show_images(agent_images)

# Run the application
root.mainloop()