# Vending Machine

This is a simple vending machine implemented in Python that simulates the operation of a real vending machine. The vending machine allows users to select items and pay for them using coins.
Installation

To run the vending machine, you will need Docker installed on your system. Once you have Docker installed, follow these steps:

# Clone this repository to your local machine:
```console
 git clone https://github.com/zeinabmontazeri/Vending-Machine.git
 ```

# Build the Docker image:
```console
 docker build -t vendingmachine_web .
 ```

# Usage
To use the vending machine, run main.py file. You will see a list of available items and their prices. To purchase an item, select it and enter the required coins. The vending machine will dispense the item if the correct amount of coins has been entered.

# Data Storage
This vending machine implementation uses in-memory data storage, which means that all data is stored in the memory of the running Python process. This approach was chosen for simplicity and ease of use.

# Unit Testing
This vending machine implementation includes unit tests to ensure that the code is working correctly. To run the tests, use the following command:
```console
python -m unittest discover tests
```

This will run all of the unit tests in the tests directory.
