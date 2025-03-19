# PyBannerGenie

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/[YourUsername]/PyBannerGenie/actions/workflows/test.yml/badge.svg)](https://github.com/[YourUsername]/PyBannerGenie/actions/workflows/test.yml)

**Generate eye-catching square banners with ease using Python!**

PyBannerGenie is a versatile Python tool designed to create custom, high-quality square banners. Perfect for social media, marketing materials, or adding flair to your projects. Choose from basic, fancy ASCII art, or colorful framed banner styles.  Use it interactively, or via command-line arguments.

## Table of Contents

1.  [Features](#features)
2.  [Installation](#installation)
3.  [Usage](#usage)
4.  [Command-Line Usage](#command-line-usage)
5.  [Contributing](#contributing)
6.  [License](#license)
7.  [Support](#support)
8.  [Monetization](#monetization)
9.  [Code of Conduct](#code-of-conduct)
10. [Credits](#credits)

## Features

*   **Multiple Banner Styles:**
    *   Basic Square ASCII Banner
    *   Fancy Square ASCII Art Banner (using `pyfiglet`)
    *   Colorful Square Framed Banner
*   **Customizable:**
    *   Choose from a variety of fonts (for fancy banners)
    *   Select banner colors from a predefined palette
    *   Text-based customization
*   **Save Options:**
    *   Save banners as `.txt` files
    *   Save banners as `.png` images
*   **User-Friendly Interface:** Interactive command-line menu for easy navigation.
*   **Command-Line Arguments:**  Generate banners directly from the command line for scripting and automation.
*   **Cross-Platform Compatibility:**  Works on any system with Python 3.6+ installed.

## Installation

See [docs/installation.md](docs/installation.md) for detailed installation instructions.  (Typically involves cloning the repo, creating a virtual environment, and installing dependencies).

## Usage

See [docs/usage.md](docs/usage.md) for detailed usage instructions and examples of the interactive mode.

## Command-Line Usage

PyBannerGenie can also be used from the command line. Here are some examples:

*   **Basic Banner:**

    ```
    python src/PyBannerGenie.py --text "Hello World" --color blue --type 1 --output hello --save-txt --save-img
    ```

*   **Fancy Banner with a specific font:**

    ```
    python src/PyBannerGenie.py --text "Python Rocks!" --color green --type 2 --font slant --output python_rocks --save-img
    ```

**Command-Line Arguments:**

*   `--interactive`: Run in interactive mode with a menu.
*   `--text`: Text for the banner (required unless `--interactive` is used).
*   `--color`: Color for the banner (red, green, yellow, blue, cyan, magenta, white). Default: white.
*   `--font`: Font for fancy banners (slant, block, standard, big, banner3, digital). Default: standard.
*   `--output`: Filename to save the banner (without extension).
*   `--type`: Banner type: 1=Basic, 2=Fancy, 3=Colored (required unless `--interactive` is used).
*   `--save-txt`: Save banner to a text file.
*   `--save-img`: Save banner as an image file.

## Contributing

We welcome contributions! See [docs/development.md](docs/development.md) for guidelines on how to contribute to the project.

## License

This project is licensed under the [MIT License](LICENSE).  See the `LICENSE` file for details.

## Support

For bug reports, feature requests, or general questions, please use GitHub issues.

## Monetization

*   **GitHub Sponsors:**  Sponsors are Welcome users to support My work directly.
*   **Premium Features (Future):**  Premium features (On Request) More fonts, advanced customization options, commercial licenses and Batch Creation in a paid version or through a subscription model. Using Gumroad or Lemon Squeezy.
*   **Consulting/Customization Services:**  We Offer custom banner design services or tailor the tool to specific client needs.
*   **Affiliate Marketing (Related Tools):**  We Offer Promotion of related tools or resources (e.g., graphic design software) To earn affiliate commissions.

## Code of Conduct

Please note that this project has a Code of Conduct. By participating in this project, you agree to abide by its terms.

## Credits

*   Developed by Irmiya Malgwi (@Village\_Coder)
*   Uses the following open-source libraries:
    *   `pyfiglet`
    *   `colorama`
    *   `Pillow`


*   Please Collaborate with Me.
*   Thanks!