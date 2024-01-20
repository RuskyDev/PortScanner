# Port Scanner

## Overview

Port Scanner is a straightforward Python tool designed to scan open ports on a specified target IP address.

## Features

- Multi-threaded port scanning
- Easy configuration via `config.json`
- Records open ports in `open_ports.txt` after scanning

## Usage

1. **Download:**
    - Download the `PortScanner.zip` from the Releases tab on GitHub.

2. **Unzip:**
    - Unzip the contents of `PortScanner.zip` to a location of your choice.

3. **Configuration:**
    - Open `config.json` using a text editor of your choice.
    - Modify the necessary settings such as `target_ip`, `start_port`, and `end_port`.

4. **Run:**
    - Once the configuration is complete, run `PortScanner.exe`.

That's it! The tool will perform a multi-threaded scan of the specified target IP address within the defined port range. The results will be recorded in `open_ports.txt`.

## Notes

- Ensure that you have the necessary permissions to scan the target IP address.
- For any issues or inquiries, please check the [Issues](https://github.com/RuskyDev/PortScanner/issues) section on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
