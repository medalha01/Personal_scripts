import pyautogui

def print_mouse_position():
    try:
        while True:
            # Get the current position of the mouse cursor
            mouse_position = pyautogui.position()
            print(f"Current mouse position: {mouse_position}")
            
            # Pause for a short duration to prevent excessive printing
            pyautogui.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    print_mouse_position()
