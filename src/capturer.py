import pyautogui
import time
import os

class KindleCapturer:
    def __init__(self, direction='ltr'):
        self.direction = direction

        # Fail-safe: moving mouse to upper-left corner will throw exception
        pyautogui.FAILSAFE = True
        
    def wait_for_focus(self, seconds=5):
        """Waits for a few seconds to let user focus the window."""
        for i in range(seconds, 0, -1):
            print(f"Starting in {i} seconds... Please focus the Kindle window!")
            time.sleep(1)
        print("Started!")

    def capture_loop(self, output_dir, page_count=None):
        """Captures pages in a loop."""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        else:
            print(f"Cleaning up {output_dir}...")
            for filename in os.listdir(output_dir):
                file_path = os.path.join(output_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")

        page_num = 1
        print("Press Ctrl+C in this terminal to stop capturing early.")
        
        try:
            while True:
                if page_count and page_num > page_count:
                    print(f"Reached limit of {page_count} pages.")
                    break

                filename = os.path.join(output_dir, f"page_{page_num:04d}.png")
                print(f"Capturing page {page_num}...")
                
                # Take screenshot
                self._screenshot_page(filename)
                
                # Turn page
                self._next_page()
                
                # Wait for page turn animation
                # Kindle for PC animation can be slow. 1.5s is a safe starting point.
                time.sleep(1.5)
                
                page_num += 1
                
        except KeyboardInterrupt:
            print("\nCapture stopped by user.")

    def _screenshot_page(self, filename):
        """Screenshots the entire screen."""
        # We capture the full screen. User should be in Full Screen mode (F11).
        # If we wanted to be fancy, we could let user define a region, but full screen is easiest.
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

    def _next_page(self):
        """Sends the arrow key to turn the page."""
        if self.direction == 'rtl':
            pyautogui.press('left')
        else:
            pyautogui.press('right')
