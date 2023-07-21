# BitGap Price Monitoring Algorithm

## Overview

The BitGap Price Monitoring Algorithm is a tool designed to monitor price changes in Bitcoin (BTC) across two platforms: Coinbase and an external source (e.g., an exchange or data provider). The algorithm helps track and identify price discrepancies between these platforms, commonly known as "arbitrage opportunities."

This README.md file provides an overview of the algorithm, its functionality, setup instructions, and other essential information.

## Features

- Real-time Price Monitoring: The algorithm fetches the latest BTC price data from both Coinbase and an external source in real-time.
- Price Comparison: It compares the prices between Coinbase and the external source to calculate the price gap.
- Notification System: If a significant price gap is detected, the algorithm can trigger a notification, such as an email or push notification, to alert the user about the potential arbitrage opportunity.

## Prerequisites

Before using the BitGap Price Monitoring Algorithm, ensure you have the following prerequisites in place:

1. Python: The algorithm is implemented in Python, so you must have Python installed on your system.
2. Coinbase API Key: To access Coinbase's price data, you need an API key. Obtain one by signing up for a Coinbase account and generating an API key with read-only permissions.
3. API Access to External Source: Similarly, you need an API key or any necessary credentials to access the price data from the external source.

## Setup

1. Clone the Repository: Begin by cloning this repository to your local machine.

```bash
git clone https://github.com/your-username/bitgap-algorithm.git
cd bitgap-algorithm

...

3. Configuration: Open the `config.py` file and replace the placeholder API keys and other configurations with your actual API credentials and preferences.

```
python
# Configurations for Coinbase API
COINBASE_API_KEY = "YOUR_COINBASE_API_KEY"
COINBASE_API_SECRET = "YOUR_COINBASE_API_SECRET"
COINBASE_API_PASSPHRASE = "YOUR_COINBASE_API_PASSPHRASE"

# Configurations for External Source API
EXTERNAL_SOURCE_API_KEY = "YOUR_EXTERNAL_SOURCE_API_KEY"

# Price Gap Threshold
PRICE_GAP_THRESHOLD = 100  # Replace with the threshold value you desire
