# BestBuy Product Availability Checker

This is a Python program that checks the availability of products on BestBuy.com using the BestBuy API. It allows you to monitor the stock status of specific products and get notified when they become available.

## Prerequisites

- Python 3.x
- `urllib` library
- `simplejson` library
- `webbrowser` library
- `playsound` library

## Getting Started

1. Clone this repository to your local machine or download the program file.
2. Install the required libraries using pip:
3. Open the program file in a text editor of your choice.

## Usage

1. Replace the placeholder value `'xxxxxxxxxxxxxxxx'` with your BestBuy API key. You can obtain an API key by signing up for a BestBuy developer account.
2. Modify the `sku` list to include the SKUs (product IDs) of the products you want to monitor. Add or remove SKUs as necessary.
3. Run the program:
4. The program will check the availability of each product in the `sku` list. If a product is not in stock, it will wait for a specified period of time and check again.
5. Once a product becomes available, the program will open the BestBuy website page for that product and play an alarm sound to notify you.

Note: Please ensure that you have a working internet connection while running this program.

## Customization

- `period` variable: This variable represents the time interval (in seconds) between each availability check. You can adjust this value according to your needs. The default value is 0.5 seconds.
- `alarm.wav` file: The program plays an alarm sound when a product becomes available. Replace the `alarm.wav` file in the same directory with your desired sound file.

## License

This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
