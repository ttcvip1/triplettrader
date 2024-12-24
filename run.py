import requests
from datetime import datetime
import time

# Function to authenticate user
def authenticate():
    valid_ttt_id = "triplettrader@gmail.com"
    valid_password = "@Triple_T_Trader"
    expiry_date = datetime(2070, 12, 10)

    ttt_id = input("ENTER TTT ID: ").strip()
    password = input("ENTER PASSWORD: ").strip()
    
    if ttt_id == valid_ttt_id and password == valid_password:
        today = datetime.now()
        if today <= expiry_date:
            print("\nYOUR ID APPROVED ✅")
            return True
        else:
            print("\nACCESS DENIED ❌")
            print(f"This TTT ID has expired. Please renew your subscription! Expiry date: {expiry_date.strftime('%m/%d/%Y')}")
    else:
        print("\nACCESS DENIED ❌")
        print("Invalid TTT ID or Password. Please try again!")
    return False

# Function to display the banner
def display_banner():
    GREEN = "\033[92m"
    RESET = "\033[0m"

    ascii_art = rf"""
{GREEN}
 _______ _______ _______ 
|__   __|__   __|__   __|
   | |     | |     | |   
   | |     | |     | |   
   | |     | |     | |   
   |_|     |_|     |_|   
{RESET}
    """
    print(ascii_art)
    print(f"{GREEN}   TOOL NAME - TTT ☢ GENERATOR  ")
    print(f"  ==============================")
    print(f"           TTT ☢ FUTURE ")
    print(f"           VERSION 1.00.1")
    print(f"  ===============================")

# Function to display the available assets in green
def display_assets():
    GREEM = "\033[92m"
    RESET = "\033[0m"

# Function to gather input from the user
def gather_params():
    GREEN = "\033[92m"
    BLUE = "\033[94m"  # Define BLUE color here
    RESET = "\033[0m"

    # Gather user input for selected assets
    asset_numbers = input(f"\n{GREEN}ENTER THE ASSET NAME MAX 3 ASSETS(e.g.,USDBDT-OTC, USDEGP-OTC): {RESET}").strip()
    asset_numbers_list = asset_numbers.split(",")  # Split the input by commas

    # Validate asset numbers
    valid_pairs = {
        "AUDCAD-OTC": "AUDCAD_otc", "AUDCHF-OTC": "AUDCHF_otc", "AUDJPY-OTC": "AUDJPY_otc", "AUDNZD-OTC": "AUDNZD_otc", 
        "AUDUSD-OTC": "AUDUSD_otc", "EURAUD-OTC": "EURAUD_otc", "EURCAD-OTC": "EURCAD_otc", "EURCHF-OTC": "EURCHF_otc", 
        "EURGBP-OTC": "EURGBP_otc", "EURJPY-OTC": "EURJPY_otc", "EURNZD-OTC": "EURNZD_otc", "EURSGD-OTC": "EURSGD_otc", 
        "EURUSD-OTC": "EURUSD_otc", "GBPAUD-OTC": "GBPAUD_otc", "GBPCAD-OTC": "GBPCAD_otc", "GBPCHF-OTC": "GBPCHF_otc", 
        "GBPJPY-OTC": "GBPJPY_otc", "GBPNZD-OTC": "GBPNZD_otc", "GBPUSD-OTC": "GBPUSD_otc", "NZDCAD-OTC": "NZDCAD_otc", 
        "NZDCHF-OTC": "NZDCHF_otc", "NZDJPY-OTC": "NZDJPY_otc", "USDARS-OTC": "USDARS_otc", "USDBDT-OTC": "USDBDT_otc", 
        "USDCAD-OTC": "USDCAD_otc", "USDCHF-OTC": "USDCHF_otc", "USDCOP-OTC": "USDCOP_otc", "USDDZD-OTC": "USDDZD_otc", 
        "USDEGP-OTC": "USDEGP_otc", "USDIDR-OTC": "USDIDR_otc", "USDINR-OTC": "USDINR_otc", "USDJPY-OTC": "USDJPY_otc", 
        "USDMXN-OTC": "USDMXN_otc", "USDNGN-OTC": "USDNGN_otc", "USDPHP-OTC": "USDPHP_otc", "USDPKR-OTC": "USDPKR_otc", 
        "USDTRY-OTC": "USDTRY_otc", "USDZAR-OTC": "USDZAR_otc", "USDBRL-OTC": "BRLUSD_otc","FB-OTC": "FB_otc"
    }

    pairs = []
    for asset_number in asset_numbers_list:
        asset_number = asset_number.strip()
        if asset_number in valid_pairs:
            pairs.append(valid_pairs[asset_number])

    # If no valid pairs were selected, default to "USDARS_otc"
    if not pairs:
        print(f"{GREEN}Invalid asset numbers entered. Defaulting to USDARS_otc.{RESET}")
        pairs.append("USDARS_otc")

    # Gather other inputs
    start_time = input(f"{GREEN}ENTER START TIME (e.g., 09:00): {RESET}").strip() or "09:00"
    end_time = input(f"{GREEN}ENTER END TIME (e.g., 18:00): {RESET}").strip() or "18:00"
    days = input(f"{GREEN}ENTER NUMBER OF FILTERING DAYS (DEFAULT: 5): {RESET}").strip() or "5"

    # Automatically set values for other parameters
    mode = "normal"  # Default to normal
    min_percentage = "90"  # Default to 90
    filter_value = "q"  # Default to 1
    separate = "1"  # Default to 1
    
    # Convert the list of pairs into a comma-separated string for the request
    params = {
        'start_time': start_time,
        'end_time': end_time,
        'days': days,
        'pairs': ",".join(pairs),
        'mode': mode,
        'min_percentage': min_percentage,
        'filter': filter_value,
        'separate': separate
    }

    return params

# Function to format the signals
def format_signals(raw_data):
    formatted_signals = []
    for line in raw_data.splitlines():
        if "～" in line:
            parts = line.split("～")
            if len(parts) == 4:
                time = parts[2].strip()
                pair = parts[1].replace("_otc", "-OTC").strip()
                action = parts[3].strip().upper()
                formatted_signals.append(f"{time}➤{pair}➤{action}  ")
    return formatted_signals

# Function to fetch and process signals
def send_request():
    url = "https://alltradingapi.com/signal_list_gen/qx_signal.js"
    
    # Define color variables here
    GREEN = "\033[92m"
    BLUE = "\033[94m"  # Define BLUE color here
    RESET = "\033[0m"
    
    # Gather parameters
    params = gather_params()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"\n{GREEN}Please wait...{RESET}")
    time.sleep(2)  # Simulate processing delay

    # Send request for the selected pairs
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        print(f"{GREEN}Signals received...{RESET}\n")
        print(f"𒆜TRIPLE T TRADER 𒆜\n")
        print(f"{GREEN}⏰Timezone: UTC (+06:00){RESET}")
        print(f"{GREEN}📅Date: {datetime.now().strftime('%d/%m/%Y')}{RESET}")
        print(f"{GREEN}◻️AVOID IF OPPOSITE TREND, BACK 2 BACK 3 OPPOSITE CANDLE & PREVIOUS CANDLE DOJI OR GAPES\n")
        print(f"{GREEN}SIGNALS:{RESET}\n")
        raw_data = response.text
        formatted_signals = format_signals(raw_data)
        print(f"{GREEN}" + "\n".join(formatted_signals) + f"{RESET}")
    else:
        print(f"\n{GREEN}Request failed with status code: {response.status_code}{RESET}")

# Main execution
if __name__ == "__main__":
    display_banner()
    if authenticate():
        send_request()
