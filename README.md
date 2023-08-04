
# Mazza Value Invest

## Overview

Mazza Value Invest is a data-driven investment project that leverages value investing principles to identify the best investment opportunities. This project is built on openBB, a powerful financial analytics tool.

## Getting Started

To get started with Mazza Value Invest, you'll need to set up your environment and install the necessary dependencies. Here's a step-by-step guide.

### Prerequisites

- Python 3.9 or above
- Conda package manager

### Installation

#### Step 1: Install openBB

First, install openBB. You can do this using pip, the Python package manager. If you're using Conda, you'll want to create and activate a new environment for openBB.

Here's how to do it:

```shell
# Create a new Conda environment
conda env create -n obb --file https://raw.githubusercontent.com/OpenBB-finance/OpenBBTerminal/main/build/conda/conda-3-9-env.yaml

# Activate the new Conda environment
conda activate obb

# Install openBB
pip install openbb --no-cache-dir
```

For more information, please refer to the [openBB installation guide](https://docs.openbb.co/terminal/installation/pypi).

#### Step 2: Set Up Your API Keys

You'll need to provide your own API keys to use Mazza Value Invest. Insert your API keys into a file named `api.yaml` and move this file to the `credentials` directory. The format of `api.yaml` should be as follows:

```yaml
keys:
    fmp: 'your-api-key-here'
```

Replace `'your-api-key-here'` with your actual API key.

Now, you're ready to start using Mazza Value Invest to identify the best value investment opportunities!

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the terms of the MIT license.

Enjoy identifying the best value investment opportunities with Mazza Value Invest!