# EtterForge

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## version 0.0.001 beta
EtterForge is a Python script designed for educational and testing purposes to facilitate the changing of MAC addresses of network interfaces. It allows users to select a network interface, specify a new MAC address, and apply the changes. Please note that changing the MAC address of a network interface may have legal and ethical implications, and it is important to ensure proper authorization before doing so.

## Features

- Retrieve the latest version of EtterForge from a remote repository
- Check for updates automatically
- Backup the existing script before updating
- Apply new MAC address to the selected network interface

## Prerequisites

To run EtterForge, you need the following prerequisites:

- Python 3.x: Make sure Python is installed on your system.
- requests library: Install the requests library using the following command:
    ```bash
    pip install requests
    ```
- Rich library: Install the Rich library using the following command:
    ```bash
    pip install rich
    ```

## Installation

1. Clone the EtterForge repository:

```bash
git clone https://github.com/happy-kitty0821/EtterForge.git
```

2. Install the required libraries if not installed:

```bash
pip install rich
```

## Usage

1. Open a terminal and navigate to the EtterForge directory.
```bash
cd EtterForge
```
1. Run the script copy 1 of 2 command:

```bash
python EtterForge.py
```

```bash
python3 EtterForge.py
```

3. Read and agree to the terms and conditions.

4. Select the network interface you want to change the MAC address of.

5. Enter the new MAC address in the format XX:XX:XX:XX:XX:XX, where X is a hexadecimal digit.

6. The script will apply the changes and bring the interface back online.

## Code Explanation

- **updateCheck.py**: This module handles the code responsible for checking for updates. It retrieves the latest version of EtterForge from a remote repository using the GitHub API and compares it with the local version. If an update is available, it backs up the existing script, downloads the latest version, and replaces the existing script.

- **EtterForge.py**: This is the main script that allows users to change the MAC address of a network interface. It prompts users to read and agree to the terms and conditions, displays the available network interfaces, prompts for the selection of an interface and a new MAC address, validates the input, and applies the changes using the `subprocess` module.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request.

## Acknowledgements

The EtterForge script is built upon the work of the open-source community and various Python libraries. Special thanks to the contributors of the requests and Rich, OS, subprocess, time, re libraries.

## Disclaimer

- This script is provided for educational and testing purposes only. The author does not guarantee its 100% working rate and anonymity.
- The users must use this script at their own risk and ensure they have proper authorization before making any changes to network interfaces.

## Contact

For any inquiries or feedback, please contact [author-name](https://github.com/happy-kitty0821).
mail ayushhaang09@gmail.com
