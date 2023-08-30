import pyautogui as auto
import time
import keyboard
from PIL import ImageGrab
import os

total_page = 353
target_name = 'UX_UI_디자이너를_위한_실무_피그마'
left_top = ()
right_bottom = ()

# Determine relative path based on the location of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(current_directory, 'image')

# User prompt
print('This program works on the assumption that pressing the right arrow key will take you to the next page.')
print('Place the mouse cursor in the upper left corner of the screenshot target and press q.')

# Wait until the user presses "q" to capture the top left position
while True:
    if keyboard.is_pressed("q"):
        left_top = auto.position()
        time.sleep(0.2)
        break

print('Place the mouse cursor in the lower right corner of the screenshot target and press q.')

# Wait until the user presses "q" to capture the bottom right position
while True:
    if keyboard.is_pressed("q"):
        right_bottom = auto.position() 
        time.sleep(0.2)
        break

# Extracting the x and y coordinates and dimensions of the region to be captured
left_top_x = left_top[0]
left_top_y = left_top[1]
capture_width = right_bottom[0]-left_top[0]
capture_height = right_bottom[1]-left_top[1]

# Function to capture screenshot
def screenshot(i):
    file_name = target_name + '_' + str(i+1).zfill(4) + '.png'
    file_path = os.path.join(image_folder_path, file_name)
    auto.screenshot(file_path, region=(left_top_x, left_top_y, capture_width, capture_height))

# Giving the user some time to prepare (e.g., opening the book) before starting the screenshot process
time.sleep(3.)

# Capturing screenshots for half the total pages (since each screenshot has 2 pages)
for i in range(int(total_page/2)):
    screenshot(i)
    time.sleep(0.1) # Short delay after taking screenshot
    auto.press('right') # Move to the next page
    time.sleep(0.1) # Short delay after pressing the right arrow key
    print(str(i+1), '/', int(total_page/2)) # Display progress

# Rename the image folder to the book name after capturing all screenshots
new_folder_path = os.path.join(current_directory, target_name)
os.rename(image_folder_path, new_folder_path)

# Create a new image folder for future use
os.mkdir(image_folder_path)
