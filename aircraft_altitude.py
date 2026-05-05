from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:")
    aircraft = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):")

        if command.strip() == "X":
            break

        parts = command.strip().split()

        if len(parts) != 2:
            continue

        action, value = parts

        try:
            feet = int(value)
        except:
            continue

        if action == "A":
            aircraft.ascent(feet)
        elif action == "D":
            aircraft.descent(feet)

    print(f"Final altitude: {aircraft.altitude} feet")


if __name__ == "__main__":
    main()