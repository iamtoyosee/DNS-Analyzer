# DNS-Analyzer
Advanced DNS Analyzer

## DNS Scan Tool with ChatGPT Integration

This script performs a DNS scan for a given domain, outputs the results, and sends the results to OpenAI's ChatGPT for further analysis. The script is written in Python and uses threading for efficient scanning.

## Features

- Scans for DNS records of a specified domain
- Outputs the DNS records to the console and optionally to a file
- Integrates with ChatGPT to provide an analysis of the scan results
- Supports multithreading for faster scanning

## Requirements

- Python 3.6 or higher
- `openai` library
- OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/dnscan.git
cd dnscan
```
2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

##Usage
Update the script with your OpenAI API key. Replace your-api-key-here with your actual API key in the script:

```python
openai.api_key = 'your-api-key-here'
```

3. Run the script:
   
```bash
$ python dnscan.py example.com

Scanning example.com for A records
example.com - 93.184.216.34
example.com - 93.184.216.35
example.com - 93.184.216.36

ChatGPT Analysis:
The DNS scan results for example.com indicate that there are multiple A records associated with the domain. The IP addresses found are:

93.184.216.34
93.184.216.35
93.184.216.36
These IP addresses are likely load balanced to distribute traffic evenly across multiple servers, improving the site's reliability and performance.
