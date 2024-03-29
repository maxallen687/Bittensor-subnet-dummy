# Bittensor Subnet Dummy

This is a simple Bittensor subnet that implements a dummy forward pass. The purpose of this example is to demonstrate how to create a basic subnet in Bittensor.

## Prerequisites

- Python 3.x
- Bittensor (installable via `pip install bittensor`)
- Local Subnet running in port 9944
- Registred wallet "miner" and "validate" on netuid 1

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/eliasful/bittensor-subnet-dummy.git

### Install dependencies:

```
pip install -r requirements.txt
```

### Usage
Run the `neurons/miner.py` and `neurons/validator.py` script to start the subnet:


### How it works
The dummy subnet implements a simple forward pass that takes a nonce as input and returns a SHA-256 hash of the nonce. This example is purely illustrative and should not be used in a real production environment.
