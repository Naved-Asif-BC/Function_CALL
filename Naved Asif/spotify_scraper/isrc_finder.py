##Code for finding isrc of any song if available using its ID.



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

song_id = []

# Open the CSV file
with open('Spotify_data.csv', 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Specify the column index
    column_index = 1

    # Iterate through each row
    for row in reader:
        # Check if the row has enough columns
        if len(row) > column_index:
            # Access the value in the specified column
            column_value = row[column_index]
            if column_value == "ID":
                continue
            song_id.append(column_value)

# Set up the WebDriver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed

# Go to the website
driver.get("https://www.isrcfinder.com/")

# Store the data for each song
song_data_list = []

# Iterate through the song list
for song in song_id:
    # Find the search input element and enter the song ID
    search_input = driver.find_element("name", "URI")
    search_input.clear()  # Clear any previous search
    search_input.send_keys(song)
    search_input.send_keys(Keys.RETURN)

    strong_tags = driver.find_elements(By.TAG_NAME, "strong")

    # Check if the desired index is within the range of available <strong> tags
    index = 0  # Example index number
    if index < len(strong_tags):
        # Access the desired <strong> tag by its index
        desired_strong_tag = strong_tags[index]

        # Get the text content of the <strong> tag
        data = desired_strong_tag.text

        # Store the data in the song_data_list
        song_data_list.append(data)
    else:
        song_data_list.append("Data not found")  # Or handle the case when data is not found for a song

# Prepare the song data in a format suitable for writing to CSV
data = []
for item in song_data_list:
    track = {}
    track["ISRC"] = item
    data.append(track)

# Writing data to CSV file
filename = 'Spotify_ISRC.csv'
fields = ['ISRC']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

# Close the browser
driver.quit()
