# DNS Poisoning Detector

## Overview

The DNS Poisoning Detector is a Python-based tool designed to monitor DNS traffic, detect potential DNS poisoning attacks, and generate detailed PDF reports of its findings. This tool is particularly useful for network administrators and security professionals who want to enhance their network's security posture against DNS-based attacks.

## Features

- Real-time DNS traffic monitoring
- Detection of suspicious DNS responses
- Customizable detection parameters
- Detailed PDF report generation
- Easy-to-use command-line interface



## Installation

1. Clone the repository:
   ```
   git clone https://github.com/akintunero/dns_poisoning_detector.git
   cd dns_poisoning_detector
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the DNS Poisoning Detector:

```
sudo python3 main.py
```

Note: Sudo privileges are required for packet sniffing.

The tool will monitor DNS traffic for a specified duration (default is 60 seconds) and generate a PDF report in the `reports/` directory if any suspicious activities are detected.

## Configuration

You can customize the tool's behavior by modifying the `config/config.yaml` file. Available options include:

- `monitoring_duration`: Duration of DNS traffic monitoring in seconds
- `suspicious_ip_threshold`: Threshold for considering an IP address suspicious
- `report_filename`: Custom filename for the generated PDF report

## Development

To contribute to the project:

1. Fork the repository
2. Create a new branch 
3. Create a new Pull Request


## Dependencies

- Python 3.7+
- Scapy: For packet sniffing and analysis
- ReportLab: For PDF report generation
- PyYAML: For configuration file parsing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational and professional use only. Always obtain proper authorization before monitoring network traffic on systems you do not own or have explicit permission to test.


## Extending the Tool

The modular structure allows for easy extensions:

- `detector.py`: Implement new detection algorithms or enhance existing ones.
- `report_generator.py`: Customize report formats or add new visualization types.
- `utils.py`: Add utility functions for data processing or analysis.

## Troubleshooting

Common issues and solutions:

1. **Permission Denied**: Ensure the script is run with sudo privileges.
2. **No Packets Captured**: Verify network interface settings and firewall rules.
3. **ImportError**: Confirm all dependencies are correctly installed.
4. **Configuration Errors**: Check `config.yaml` for syntax errors or invalid values.

For detailed error information, refer to the log file specified in the configuration.


## Future Enhancements

- Implement real-time alerting system for immediate threat notification.
- Develop a web-based interface for easier configuration and result visualization.
- Add support for exporting results in various formats (CSV, JSON, etc.).
- Integrate machine learning algorithms for more accurate threat detection.

For feature requests or bug reports, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
