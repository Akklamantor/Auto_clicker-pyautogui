import pyautogui
import random
import time


def auto_clicker(clicks_per_second, random_range):
    """
    Auto clicker with adjustable speed and random delays.

    :param clicks_per_second: Number of clicks per second (float or int).
    :param random_range: Tuple of (min_random_delay, max_random_delay) for random delays (seconds).
    """
    try:
        print("Auto clicker started. Press Ctrl+C to stop.")
        while True:
            pyautogui.click()  # Perform a click
            # Calculate delay between clicks
            base_delay = 1 / clicks_per_second
            random_delay = random.uniform(random_range[0], random_range[1])
            total_delay = base_delay + random_delay
            time.sleep(total_delay)
    except KeyboardInterrupt:
        print("\nAuto clicker stopped.")


if __name__ == "__main__":
    # Adjustable settings
    clicks_per_second = float(input("Enter clicks per second (e.g., 5): "))
    min_random = float(input("Enter minimum random delay (seconds, e.g., 0.1): "))
    max_random = float(input("Enter maximum random delay (seconds, e.g., 0.5): "))

    if min_random > max_random:
        print("Minimum random delay cannot be greater than maximum random delay. Please restart.")
    else:
        auto_clicker(clicks_per_second, (min_random, max_random))
