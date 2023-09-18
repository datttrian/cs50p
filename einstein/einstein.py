def main():
    # Prompt the user for mass as an integer (in kilograms)
    mass = int(input("Enter mass (in kilograms): "))

    # The speed of light in meters per second
    speed_of_light = 300000000

    # Calculate enerygy using the E = mc² formula
    energy = mass * (speed_of_light**2)

    # Print the equivalent energy as an integer
    print(energy)


if __name__ == "__main__":
    main()
