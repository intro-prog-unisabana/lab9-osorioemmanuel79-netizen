from car_utils import create_car_from_input, display_cars

def main():
    car_dict = {}

    while True:
        print("\nMenu:")
        print("1. Add a new car")
        print("2. View all cars")
        print("3. Drive a car")
        print("4. Paint a car")
        print("5. Exit")

        option = input("Choose an option:\n")

        if option == "1":
            car = create_car_from_input()
            car_dict[car.car_id] = car

        elif option == "2":
            display_cars(car_dict)

        elif option == "3":
            car_id = input("Enter the car ID to drive:\n")
            if car_id in car_dict:
                miles = float(input("How many miles to drive?\n"))
                car_dict[car_id].drive(miles)
                print("Mileage updated.")
            else:
                print("Car not found.")

        elif option == "4":
            car_id = input("Enter the car ID to paint:\n")
            if car_id in car_dict:
                color = input("Enter the new color:\n")
                car_dict[car_id].change_color(color)
                print("Color updated.")
            else:
                print("Car not found.")

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
