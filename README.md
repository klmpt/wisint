### wisint

wisint is a modular osint framework. the tool is designed for data collection, digital footprint analysis, and basic security assessment of resources.

[![stars](https://badgen.net/github/stars/klmpt/wisint?icon=github)](https://github.com/klmpt/wisint/stargazers)
[![forks](https://badgen.net/github/forks/klmpt/wisint?icon=github)](https://github.com/klmpt/wisint/network/members)

### main modules

* **recon.py**: automated link collection for target research.
* **extractor.py**: deep analysis of html content, metadata, and hidden paths.
* **web_logger.py**: php trap generation to capture ip addresses and user-agent strings.
* **image_analyzer.py**: extraction of exif data from image files.
* **port_scanner.py**: network port scanning.
* **dns_enum.py**: dns record analysis.
* **file_entropy.py**: file entropy calculation for identifying hidden data.

### compatibility

the tool has been tested and is verified to function on the following distributions:

* linux mint
* debian
* ubuntu

### installation

1. clone the repository:
`git clone https://github.com/klmpt/wisint`
`cd wisint`
2. install dependencies:
`pip install colorama pyfiglet`
3. run:
`python3 main.py`

### logging

all actions are automatically recorded in the `logs/` directory. log files are generated based on the current date. the main menu includes an option to view the most recent log entries.

### security and ethics

this tool is intended strictly for educational purposes and authorized security testing of resources you own or have explicit permission to test. the author is not responsible for any misuse or illegal activities conducted with this software.
