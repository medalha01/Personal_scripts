import pyautogui
import time

def main():
    i = 1
    time.sleep(3)
    while (i < 21):
        i += 1
        time.sleep(0.1)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.1)
        pyautogui.click(x=654, y=228)
        time.sleep(0.1)
        
                    # Simulate pressing Ctrl+A (select all)
        pyautogui.hotkey('ctrl', 'a')
            
            # Simulate pressing Ctrl+C (copy)
        pyautogui.hotkey('ctrl', 'c')
        # Click at a specified position (x, y)
        time.sleep(0.1)
        pyautogui.click(x=827, y=64)
        pyautogui.click(x=827, y=64)
        
        pyautogui.press('backspace')

        
        pyautogui.write(str(i))
        pyautogui.press('enter')

        time.sleep(0.1)
        
        pyautogui.hotkey('alt', 'tab')   
        pyautogui.click(x=1182, y=651)   
        pyautogui.hotkey('ctrl', 'v')  
        # Wait for 1 second
        time.sleep(2)
        
        # Write a number

if __name__ == "__main__":
    main()
