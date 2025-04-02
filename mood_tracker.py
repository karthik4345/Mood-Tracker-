#mood_tracker


# Simple Mood Tracker - Step 1

# Ask the user for their mood
mood = input("How are you feeling today? (Happy, Sad, Excited, Stressed, etc.): ")

# Store the mood in a text file
with open("mood_data.txt", "a") as file:
    file.write(mood + "\n")

print("Your mood has been recorded. Have a great day!")



import csv
import os
from datetime import datetime

# Ask the user for their mood
mood = input("How are you feeling today? (Happy, Sad, Excited, Stressed, etc.): ").strip()

# Ensure valid input
if not mood:
    print("❌ Mood cannot be empty. Please enter a valid mood.")
    exit()

# Define the CSV file path
file_path = "mood_data.csv"
file_exists = os.path.exists(file_path)

# Open the CSV file in append mode
with open(file_path, mode="a", newline="") as file:
    writer = csv.writer(file)
    
    # If the file is new, write the header row
    if not file_exists:
        writer.writerow(["Mood", "Timestamp"])
    
    # Generate a correctly formatted timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write mood and timestamp to CSV
    writer.writerow([mood, timestamp])

    
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Ensures proper HH:MM:SS format



print("✅ Your mood has been recorded correctly!")


