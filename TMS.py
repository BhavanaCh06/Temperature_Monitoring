def get_temperature():
    """Read temperature from the user."""
    return float(input("Enter temperature (°C): "))


def get_status(temperature):
    """Determine the temperature status."""
    if temperature < 80:
        return "NORMAL"
    elif temperature < 100:
        return "WARNING"
    else:
        return "CRITICAL"


def display_status(temperature, status):
    """Display temperature and its status."""
    print(f"Temperature: {temperature}°C")
    print(f"Status: {status}")

    if status == "CRITICAL":
        print("ALERT: Critical temperature detected!")


def main():
    """Run the temperature monitoring system."""
    while True:
        try:
            temperature = get_temperature()
            status = get_status(temperature)
            display_status(temperature, status)

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

        choice = input("\nContinue monitoring? (y/n): ").lower()

        if choice != "y":
            print("Temperature monitoring stopped.")
            break


if __name__ == "__main__":
    main()