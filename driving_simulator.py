def car_logic_simulator():
    print("Welcome to the car logic Simulator!")
    print("Controls:")
    print(" - Press 'c' for clutch")
    print(" - Press 'i' to turn on the ignition")
    print(" - Press 'I' to turn off the ignition")
    print(" - Press 'h' to release the handbrake")
    print(" - Press 'H' to apply the handbrake (Warning: Pressing while driving will cause an accident)")
    print(" - Press gear numbers (1-5) with clutch to gear up or down")
    print(" - Press '0' with clutch for neutral")
    print(" - Press 'a' to accelerate")
    print(" - Press 'b' to brake")
    print(" - Press 'r' for reverse gear")
    print(" - Press 'q' to quit (Only after turning off ignition and applying handbrake)")

    ignition_on = False
    handbrake_released = False
    clutch_pressed = False
    gear = 0  # Neutral
    speed = 0
    reverse = False

    # Speed limits for each gear
    gear_speed_limits = {1: 20, 2: 40, 3: 60, 4: 80, 5: 120}

    while True:
        command = input("Enter command: ")

        # Ignition ON
        if command == 'i':
            if ignition_on:
                print("Ignition is already ON.")
            elif gear != 0:
                print("Please shift to neutral before turning on the ignition.")
            elif not handbrake_released:
                print("Release the handbrake before turning on the ignition!")
            else:
                ignition_on = True
                print("Ignition turned ON. Engine has started and is ready to drive!")

        # Ignition OFF
        elif command == 'I':
            if not ignition_on:
                print("Ignition is already OFF.")
            elif speed > 0:
                print("Please stop the car completely before turning off the ignition.")
            elif handbrake_released:
                print("Apply the handbrake before turning off the ignition.")
            else:
                ignition_on = False
                print("Ignition turned OFF. You can now quit safely.")

        # Handbrake Release
        elif command == 'h':
            if speed > 0:
                print("Accident occurred! You pressed the handbrake while driving.")
                break
            handbrake_released = True
            print("Handbrake released. Ready to drive!")

        # Handbrake Apply
        elif command == 'H':
            if speed > 0:
                print("Accident occurred! You applied the handbrake while driving.")
                break
            handbrake_released = False
            print("Handbrake applied. Car is stationary.")

        # Clutch
        elif command == 'c':
            clutch_pressed = True
            print("Clutch pressed.")

        # Gear Change
        elif command in ['1', '2', '3', '4', '5'] and clutch_pressed:
            new_gear = int(command)
            if reverse:
                print("Cannot shift to forward gear while in reverse.")
            elif abs(new_gear - gear) > 1:
                print("You can only shift up or down by one gear at a time.")
            elif gear == 0 or new_gear > gear:  # Neutral or gear up
                if speed <= gear_speed_limits[new_gear]:
                    gear = new_gear
                    reverse = False
                    clutch_pressed = False
                    print(f"Shifted to gear {gear}.")
                else:
                    print(f"Reduce speed to below {gear_speed_limits[new_gear]} km/h before shifting to gear {new_gear}.")
            elif new_gear < gear:  # Gear down
                gear = new_gear
                clutch_pressed = False
                print(f"Shifted to gear {gear}.")

        # Reverse Gear
        elif command == 'r' and clutch_pressed:
            if speed == 0:
                reverse = True
                gear = -1  # Reverse gear
                clutch_pressed = False
                print("Shifted to reverse gear.")
            else:
                print("Cannot shift to reverse while moving.")

        # Accelerate
        elif command == 'a':
            if ignition_on and handbrake_released and (gear > 0 or reverse):
                if reverse:
                    if speed > -20:
                        speed -= 5
                        print(f"Accelerating in reverse... Current speed: {abs(speed)} km/h.")
                    else:
                        print("Cannot accelerate further in reverse. Max speed is 20 km/h.")
                else:
                    max_speed = gear_speed_limits.get(gear, 0)
                    if speed < max_speed:
                        speed += 10
                        print(f"Accelerating... Current speed of car is {speed} km/h.")
                        if gear == 5 and speed == gear_speed_limits[5]:
                            print("Max speed achieved! You are at the top speed of the car.")
                    else:
                        print(f"Cannot accelerate further. Max speed for gear {gear} is {max_speed} km/h.")
                        print("Shift to a higher gear to increase speed.")
            else:
                print("Cannot accelerate. Ensure ignition is on, handbrake is released, and correct gear is engaged.")

        # Brake
        elif command == 'b':
            if speed > 0:
                speed -= 10
                print(f"Braking... Current speed: {speed} km/h.")
                for g, limit in gear_speed_limits.items():
                    if speed <= limit:
                        if gear > g:
                            print(f"Speed has reduced to {speed} km/h. Shift down to gear {g}.")
                        break
                if speed == 0:
                    print("Car has stopped. Shift to the correct gear before accelerating.")
            elif speed < 0:
                speed += 10
                print(f"Braking in reverse... Current speed: {abs(speed)} km/h in reverse.")
            else:
                print("The car is already stopped.")

        # Quit
        elif command == 'q':
            if ignition_on:
                print("Turn off the ignition before quitting.")
            elif handbrake_released:
                print("Apply the handbrake before quitting.")
            else:
                print("Exiting simulator. Drive safe!")
                break

        # Invalid Command
        else:
            print("Invalid command or action. Check the instructions.")

# Start the simulator
car_logic_simulator()
