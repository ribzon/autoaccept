import pyautogui
import time
from PIL import ImageGrab
import sys

def perform_click_sequence():

    try:
        # Click at the green pixel location
        pyautogui.click(510, 240)
        # Wait a moment before continuing
        time.sleep(1)
    except Exception:
        # Silent error handling for clicks
        time.sleep(0.5)
        
def main():
    target_color = (54, 183, 82)
    coords_green = (510, 240)
    
    # Main infinite loop
    while True:
        try:
            # Try pyautogui first
            try:
                current_color = pyautogui.pixel(coords_green[0], coords_green[1])
            except Exception:
                # Fallback to ImageGrab
                try:
                    screenshot = ImageGrab.grab(bbox=(coords_green[0], coords_green[1], 
                                                     coords_green[0] + 1, coords_green[1] + 1))
                    current_color = screenshot.getpixel((0, 0))
                except Exception:
                    # If both methods fail, just continue to the next iteration
                    time.sleep(0.2)
                    continue

            # Check if target color found
            if current_color == target_color:
                perform_click_sequence()
            
            # Sleep to prevent excessive CPU usage
            time.sleep(1)
            
        except Exception:
            # Global error handler - prevents crashes by catching any unexpected errors
            time.sleep(0.5)
            continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
