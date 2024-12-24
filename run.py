from datetime import datetime, timedelta
import random

# Function to display a colorful banner
def display_banner():
    # Define ANSI escape codes for colors and reset
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # ASCII art with colors
    ascii_art = rf"""
    {RED}
 _______ _______  _____ 
|__   __|__   __|/ ____|
   | |     | |  | |    
   | |     | |  | |    
   | |     | |  | |____
   |_|     |_|   \_____|
   {RESET}
    """
    print(ascii_art)

# Function to generate signals based on total time range
def generate_timed_signals(asset, direction, start_time, end_time):
    signals = []
    total_minutes = int((end_time - start_time).total_seconds() / 60)

    # Calculate the number of signals based on total time range
    hours = total_minutes // 60
    num_signals = random.randint(8, 12) * (hours + 1)
    signal_time = start_time

    for _ in range(num_signals):
        interval = timedelta(minutes=random.randint(4, 7))
        signal_time += interval
        if signal_time >= end_time:
            break
        signals.append(f"{signal_time.strftime('%H:%M')} - {asset} - {direction}")

    return signals

# Main function
def main():
    # Display banner
    display_banner()

    # Get asset name input from the user
    asset = input("Enter asset name: ").strip()

    # Get direction input
    direction = input("Enter direction (CALL/PUT): ").strip().upper()
    if direction not in ["CALL", "PUT"]:
        print("Invalid direction. Please enter 'CALL' or 'PUT'.")
        return

    # Get start and end times
    start_time_str = input("Enter start time (HH:MM): ")
    end_time_str = input("Enter end time (HH:MM): ")
    try:
        start_time = datetime.strptime(start_time_str, "%H:%M")
        end_time = datetime.strptime(end_time_str, "%H:%M")
        if start_time >= end_time:
            print("End time must be later than start time.")
            return
    except ValueError:
        print("Invalid time format. Please enter in HH:MM format.")
        return

    # Generate and display signals
    print("\nGenerated Signals:")
    signals = generate_timed_signals(asset, direction, start_time, end_time)
    for signal in signals:
        print(signal)

if __name__ == "__main__":
    main()
