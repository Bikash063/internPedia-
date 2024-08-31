import requests

# Define a list of available currencies
CURRENCIES = ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'JPY', 'CNY']

def fetch_exchange_rate(source_currency, target_currency):
    """Fetch the live exchange rate between two currencies."""
    api_key = "dc88f31953014908a2f7e39fd870f47f"  # Replace with your actual API key
    url = f"https://openexchangerates.org/api/latest.json?app_id={dc88f31953014908a2f7e39fd870f47f}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        rates = response.json().get("rates", {})

        if source_currency not in rates or target_currency not in rates:
            raise ValueError("Invalid currency code.")

        # Calculate the conversion rate
        conversion_rate = rates[target_currency] / rates[source_currency]
        return conversion_rate

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

def get_currency_choice(prompt):
    """Get a valid currency choice from the user."""
    while True:
        currency = input(prompt).upper()
        if currency in CURRENCIES:
            return currency
        else:
            print("Invalid currency. Please choose from the available options.")

def get_amount():
    """Get a valid amount from the user."""
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount < 0:
                print("Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")

def display_conversion(amount, source_currency, target_currency, converted_amount):
    """Display the conversion result with appropriate formatting."""
    print(f"\n{amount:.2f} {source_currency} is equal to {converted_amount:.2f} {target_currency}")

def main():
    print("Currency Converter")
    print("==================")

    while True:
        print("\nAvailable Currencies:", ", ".join(CURRENCIES))
        
        source_currency = get_currency_choice("Enter the source currency: ")
        target_currency = get_currency_choice("Enter the target currency: ")
        amount = get_amount()

        conversion_rate = fetch_exchange_rate(source_currency, target_currency)

        if conversion_rate:
            converted_amount = amount * conversion_rate
            display_conversion(amount, source_currency, target_currency, converted_amount)

        another = input("\nWould you like to perform another conversion? (y/n): ").lower()
        if another != 'y':
            break

    print("Thank you for using the Currency Converter!")

if __name__ == "__main__":
    main()
