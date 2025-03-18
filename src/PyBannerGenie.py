#!/usr/bin/env python3.12
#For Stability
#PyBannerGenie First Release

"""
PyBannerGenie - Version 1.0
A versatile and User-Friendly Python Tool Designed To Generate High Quality Square Banner From Text
With Options To Creat Custom Professional Banners Tailored To  YOUR Specific NEEDs
BY IRMIYA MALGWI (@VILLIAGE_CODER)
https://github.com/XchixoGhostHatkX

"""
#imports
import pyfiglet
from colorama import init, Fore, Style
from PIL import Image, ImageDraw, ImageFont
import time
import sys
import os
import argparse
from typing import Optional

# Initialize Colorama for colored terminal output (cross-platform)
init(autoreset=True)

# Available color choices
# Constants
COLORS = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "white": Fore.WHITE,
}

# Available fonts for fancy banners
FONTS = ["slant", "block", "standard", "big", "banner3", "digital"]
DEFAULT_FONT = "standard"
DEFAULT_COLOR = Fore.WHITE
OUTPUT_DIR = "banners"

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


#Professional Branded Banner
def banner():
    banner = r"""                                                           
 _____       ____                               _____            _          
|  __ \     |  _ \                             / ____|          (_)         
| |__) |   _| |_) | __ _ _ __  _ __   ___ _ __| |  __  ___ _ __  _  ___     
|  ___/ | | |  _ < / _` | '_ \| '_ \ / _ \ '__| | |_ |/ _ \ '_ \| |/ _ \    
| |   | |_| | |_) | (_| | | | | | | |  __/ |  | |__| |  __/ | | | |  __/    
|_|    \__, |____/ \__,_|_| |_|_| |_|\___|_|   \_____|\___|_| |_|_|\___|    
        __/ |                                                               
       |___/ CODED BY: IRMIYA MALGWI||EMAIL: godofnoor@protonmail.com       
                                                                            
                       https://github.com/XchixoGhostHatkX                  
                                                                            
                       https://facebook.com/irmiya.malgwi                   
                   """
    print(banner)

#Imfomatioanl Professional Banner
def banner_info(text: str, length: int = 74) -> None:
    """Displays informational text with a border."""
    border = "#" + "=" * (length - 2) + "#"
    print(border)
    print(f"=<{text}>".center(length, "="))
    print(border)

#Color Choice
def get_color_choice() -> str:
    """Asks the user for a color choice from the available colors."""
    print("\nAvailable colors: " + ", ".join(COLORS.keys()))
    while True:
        color_choice = input("Choose a color: ").strip().lower()
        if color_choice in COLORS:
            return COLORS[color_choice]
        print(Fore.RED + "Invalid color choice. Please choose again.")

#Save Banner To Text File
def save_banner_to_file(banner_text: str) -> None:
    """Saves the generated banner to a text file."""
    save_option = input("Would you like to save this banner to a file? (y/n): ").strip().lower()
    if save_option == 'y':
       filename = input("Kindly Enter The Filename (without extension): ").strip()
       if filename:
          try:
            filepath = os.path.join(OUTPUT_DIR, f"{filename}.txt")
            with open(filepath, "w", encoding="utf-8") as file:
              file.write(banner_text)
            print(Fore.GREEN + f"Banner saved as '{filepath}' successfully!")
          except Exception as e:
            print(Fore.RED + f"Error saving banner to file: {e}")
    elif save_option == 'n':
        print(Fore.RED + "Skipping Banner Saving To Text File.")
    else:
        print(Fore.YELLOW + "Error: Please Enter y or n...")
        print(Fore.RED + "Banner Not Saved.")
       
#Save Banner To Image File
def save_banner_as_image(text: str) -> None:
        """Saves the banner as a PNG image."""
        save_option = input("Would you like to save this banner as an image? (y/n): ").strip().lower()
        if save_option == 'y':
           filename = input("Kindly Enter The Filename (without extension): ").strip()
           if filename:
              try:
                font = ImageFont.load_default()  # Consider using a specific TTF font (e.g., Arial)
                image_size = (600, 200)  # You Can Adjust based on text and font
                img = Image.new("RGB", image_size, "black")
                draw = ImageDraw.Draw(img)
                draw.text((10, 10), text, font=font, fill="white")
                filepath = os.path.join(OUTPUT_DIR, f"{filename}.png")
                img.save(filepath)
                print(Fore.GREEN + f"Banner saved as '{filepath}' successfully!")
              except Exception as e:
                print(Fore.RED + f"Error saving banner as image: {e}")
      
        elif save_option == 'n':
            print(Fore.RED + "Skipping Banner Saving As Image.")
          
        else:
            print(Fore.YELLOW + "Error: Please Enter y or n...")
            print(Fore.RED + "Banner Not Saved.")
            


#Fountion To Display Basic Square ASCII Banner
def display_square_basic_banner(text: str, color: str) -> str:
    """Displays a basic square banner with a simple border."""
    length = max(20, len(text) + 4)
    border = "#" * length
    banner_text = (
        color
        + border
        + "\n"
        + color
        + "#"
        + " " * (length - 2)
        + "#"
        + "\n"
        + color
        + f"# {text.center(length - 4)} #"
        + "\n"
        + color
        + "#"
        + " " * (length - 2)
        + "#"
        + "\n"
        + color
        + border
    )
    print(banner_text)
    return banner_text


#Fountion To Display Fancy Square ASCII Art Banner
def display_square_fancy_banner(text: str, color: str, font: str = DEFAULT_FONT) -> Optional[str]:
    
    try:
        banner_text = pyfiglet.figlet_format(text, font)
        lines = banner_text.splitlines()
        max_length = max(len(line) for line in lines)
        border = "#" * (max_length + 4)
        banner_output = color + border + "\n"
        for line in lines:
            banner_output += color + f"# {line.ljust(max_length)} #" + "\n"
        banner_output += color + border
        print(banner_output)
        return banner_text

    except pyfiglet.FontError as e:
        print(Fore.RED + f"Error with font '{font}': {e}")
        return None


def display_square_colored_banner(text: str, color: str ) -> str:
    """Displays a colorful square framed banner."""
    banner_text = display_square_basic_banner(text, color)
    return banner_text


def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate square Banners with customizable styles.  Either use command-line arguments, or run in interactive mode.",
        epilog="Example: python src/PyBannerGenie.py --text 'Hello' --color blue --type 1 --output hello --save-txt --save-img",
        formatter_class=argparse.RawTextHelpFormatter, #Keeps the epilog formatting.
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Run in interactive mode with a menu (cannot be used with other arguments).",
    )

    parser.add_argument(
        "-t", "--text", type=str, help="Text for the banner (required unless --interactive is used)."
    )

    parser.add_argument(
        "-c",
        "--color",
        type=str,
        default="white",
        help=f"Color for the banner (red, green, yellow, blue, cyan, magenta, white). Default: white.",
    )
    parser.add_argument(
        "-f",
        "--font",
        type=str,
        default="standard",
        help=f"Font for fancy banners ({', '.join(FONTS)}). Default: standard.",
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Filename to save the banner (without extension)."
    )
    parser.add_argument(
        "--type", type=int, choices=[1, 2, 3], help="Banner type: 1=Basic, 2=Fancy, 3=Colored (required unless --interactive is used)."
    )
    parser.add_argument(
        "--save-txt", action="store_true", help="Save banner to a text file."
    )
    parser.add_argument(
        "--save-img", action="store_true", help="Save banner as an image file."
    )

    return parser.parse_args()


def get_user_choice() -> str:
    """Handles user input for menu selection with validation."""
    while True:
    
        print("\nBeautiful Is Better Than Ugly.\nPlease Choose The Type of Square Banner YOU Want or Exit:\n")
        print("1. Basic Square ASCII Banner")
        print("2. Fancy Square ASCII Art Banner")
        print("3. Colorful Square Framed Banner")
        print("4. Exit From Tool\n")
        choice = input("Enter YOUR Choice (1/2/3/4): ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        print(Fore.RED + "Invalid input. Please enter 1, 2, 3, or 4.")


def get_user_text() -> str:
    """Ensures the user provides non-empty input for the banner text."""
    while True:
        text = input("Please Enter the TEXT for YOUR BANNER: ").strip()
        if text:
            return text
        print(Fore.RED + "Error: Text cannot be empty. Please try again.")


def main():
    """Main program loop for generating square banners."""
    args = parse_arguments()

    if args.interactive:
        print(Style.BRIGHT + Fore.MAGENTA + "\nHello World! Welcome To The Python Square Banner Generator Mag!c Tool!")
        print(Style.BRIGHT + Fore.MAGENTA + "Introducing MySelf!...")
        time.sleep(1)

        banner()
        banner_info(".PYBANNERGENIE. ELEVATING ASCII ART: PRECISION, CREATIVITY & CODE.")
        print(Style.BRIGHT + Fore.MAGENTA + "A User-Friendly Python Tool, Designed To Creat High Quality,\nProfessional Costum Banner, Tailored To YOUR Specific NEEDs.")
        print(Style.BRIGHT + Fore.MAGENTA + "YOU Can Copy Banner Text, Save To File Or Save To Image.")

        while True:
            choice = get_user_choice()

            if choice == '4':
                confirm_exit = input(Fore.MAGENTA + "Rethink!... Are you sure you want to exit? (y/n): ").strip().lower()
                if confirm_exit == 'y':
                    print(Style.BRIGHT + Fore.RED + "Exiting the program. See You Latter! Thanks!.")
                    sys.exit()
                elif confirm_exit == 'n':
                    continue
                else:
                    print(Fore.MAGENTA + "Invalid Choice. Please Enter y or n ...")
                    continue

            user_text = get_user_text()
            user_color = get_color_choice()
            
            try:
                if choice == '1':
                    banner_text = display_square_basic_banner(user_text, user_color)
                    if banner_text:
                        save_banner_to_file(banner_text)
                        save_banner_as_image(banner_text)
                elif choice == '2':
                    """Displays a fancy ASCII-art banner using pyfiglet In Interactive Mode."""
                    print("\nAvailable fonts: " + ", ".join(FONTS))

                    while True:
                        font_choice = input("Choose a font: ").strip().lower()
                        if font_choice in FONTS:
                          break
                        print(Fore.RED + "Invalid font choice. Please choose again.")

                    banner_text = display_square_fancy_banner(user_text, user_color)
                    if banner_text:
                        save_banner_to_file(banner_text)
                        save_banner_as_image(banner_text)
                elif choice == '3':
                    banner_text = display_square_colored_banner(user_text, user_color)
                    if banner_text:
                        save_banner_to_file(banner_text)
                        save_banner_as_image(banner_text)
                else:
                    continue

                
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}")

    else:  # Command-line mode
        if not args.text:
            print(Fore.RED + "Error: --text is required unless --interactive is used.\nRun: python src/PyBannerGenie.py -i \nOr: python src/PyBannerGenie.py -h")
            sys.exit(1)

        text = args.text
        color = args.color.lower()
        font = args.font.lower()
        output = args.output
        banner_type = args.type
        save_txt = args.save_txt
        save_img = args.save_img

        if color not in COLORS:
            print(Fore.RED + f"Error: Invalid color '{color}'. Choose from: {', '.join(COLORS.keys())}")
            sys.exit(1)

        if banner_type is None:
            print(Fore.RED + "Error: --text is required unless --interactive is used.\nRun: python src/PyBannerGenie.py -i \nOr: python src/PyBannerGenie.py -h")
            sys.exit(1)

        try:
            if banner_type == 1:
                banner_text = display_square_basic_banner(text, COLORS[color])
            elif banner_type == 2:
                banner_text = display_square_fancy_banner(text, COLORS[color], font)
            elif banner_type == 3:
                banner_text = display_square_colored_banner(text, COLORS[color])
            else:
                print(Fore.RED + "Error: Invalid banner type.")
                sys.exit(1)

            if output:
                if save_txt:
                    save_banner_to_file(banner_text)
                if save_img:
                    save_banner_as_image(banner_text)
            else:
                print(banner_text) #Print the banner to the console

        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
