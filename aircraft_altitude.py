from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:")
    aircraft = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):")

        command = command.strip()

        if command == "X":
            break

        parts = command.split()

        # Evita errores si el input está mal
        if len(parts) != 2:
            continue

        action = parts[0]
        value = parts[1]

        # Evita crash si no es número
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