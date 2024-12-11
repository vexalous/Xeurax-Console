import os
import time

def convert_temperature(from_unit, to_unit, value):
  """Converts temperature between Fahrenheit and Celsius."""
  if (from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius") or (from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit"):
    if from_unit.lower() == "fahrenheit":
      return (value - 32) * 5 / 9
    else:
      return (value * 9 / 5) + 32
  else:
    raise ValueError("Invalid units.")

def convert_length(from_unit, to_unit, value):
  """Converts length between feet and meters."""
  if from_unit == "feet" and to_unit == "meters":
    return value * 0.3048
  elif from_unit == "meters" and to_unit == "feet":
    return value / 0.3048
  else:
    raise ValueError("Invalid units.")

def convert_fuel_economy(from_unit, to_unit, value):
  """Converts fuel economy between kilometers per liter and miles per gallon."""
  if from_unit == "kmpl" and to_unit == "mpg":
    return value * 0.425144
  elif from_unit == "mpg" or "miles per gallon" or "mile per gallon" and to_unit == "kmpl" or "kilometers per liter" or "kilometer per liter":
    return value * 2.35215
  else:
    raise ValueError("Invalid units.")

def convert_energy(from_unit, to_unit, value):
  """Converts energy between Joules and Kilocalories."""
  if from_unit == "joules" and to_unit == "kilocalories":
    return value / 4184
  elif from_unit == "kilocalories" and to_unit == "joules":
    return value * 4184
  elif from_unit == "foot pound" and to_unit == "joules":
    return value * 1.356
  elif from_unit == "joules" or "joule" and to_unit == "foot pound":
    return value / 1.356
  elif from_unit == "kilocalories" and to_unit == "foot pound":
    return value * 3086
  elif from_unit == "foot pound" and to_unit == "kilocalories":
    return value / 3086
  elif from_unit == "kilojoule" and to_unit == "joules":
    return value * 1000
  elif from_unit == "joules" and to_unit == "kilojoule":
    return value / 1000
  else:
    raise ValueError("Invalid units.")

def did_you_mean(command):
    """Suggests a similar command if the user enters it slightly wrong."""
    valid_commands = ["fahrenheittocelcius", "celciustofahrenheit", "feettometers", "meterstofeet", "kmpltomgpg", "mpgtokmpl", "joulestokilocalories", "kilocaloriestojoules", "stopwatch"]
    for valid_command in valid_commands:
        if levenshtein_distance(command, valid_command) <= 2:
            return valid_command
    return None

def levenshtein_distance(s1, s2):
    """Calculates the Levenshtein distance between two strings."""
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

stopwatch_running = False
start_time = 0

while True:
    print("Welcome to Xeurax Console")

    xrx_cnsl_mn_mnu_cmnd_chc = input("Enter a command to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    xrx_cnsl_mn_mnu_cmnd_chc = xrx_cnsl_mn_mnu_cmnd_chc.lower()

    if xrx_cnsl_mn_mnu_cmnd_chc == "help":
        print("Available commands:")
        print("  convert: Converts values between different units.")
        print("    Valid units:")
        print("      Temperature: Fahrenheit, Celsius")
        print("      Length: Feet, Meters")
        print("      Fuel economy: kmpl, mpg")
        print("      Energy: Joules, Kilocalories, Foot Pound")
        print("  stopwatch: Starts and stops a stopwatch.")
    elif xrx_cnsl_mn_mnu_cmnd_chc == "convert":
        while True:
            try:
                from_unit = input("Enter the unit to convert from: ")
                if from_unit == "exit":
                    break

                from_unit = from_unit.lower()

                suggested_unit = did_you_mean(from_unit)
                if suggested_unit:
                    if input(f"Did you mean '{suggested_unit}'? (y/n): ").lower() == "y":
                        from_unit = suggested_unit

                to_unit = input("Enter the unit to convert to: ")
                if to_unit == "exit":
                    break

                to_unit = to_unit.lower()

                suggested_unit = did_you_mean(to_unit)
                if suggested_unit:
                    if input(f"Did you mean '{suggested_unit}'? (y/n): ").lower() == "y":
                        to_unit = suggested_unit

                value = float(input(f"Enter value in {from_unit}: "))

                if (from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius") or (from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit"):
                    if from_unit.lower() == "fahrenheit":
                        result = convert_temperature(from_unit, to_unit, value)
                        print(f"{value} degrees {from_unit} is equal to {result:.2f} degrees {to_unit}.")
                    else:
                        result = convert_temperature(from_unit, to_unit, value)
                        print(f"{value} degrees {from_unit} is equal to {result:.2f} degrees {to_unit}.")
                elif from_unit.lower() == "feet" and to_unit.lower() == "meters":
                    result = convert_length(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "meters" and to_unit.lower() == "feet":
                    result = convert_length(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "kmpl" and to_unit.lower() == "mpg":
                    result = convert_fuel_economy(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "mpg" and to_unit.lower() == "kmpl":
                    result = convert_fuel_economy(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "joules" and to_unit.lower() == "kilocalories":
                    result = convert_energy(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "kilocalories" and to_unit.lower() == "joules":
                    result = convert_energy(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "foot pound" and to_unit.lower() == "joules":
                    result = convert_energy(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "joules" and to_unit.lower() == "foot pound":
                    result = convert_energy(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "kilocalories" and to_unit.lower() == "foot pound":
                    result = convert_energy(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "foot pound" and to_unit.lower() == "kilocalories":
                    result = convert_energy(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                elif from_unit.lower() == "kilojoule" and to_unit.lower() == "joules":
                    result = convert_energy(from_unit, to_unit, value)
                    print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
                else:
                    raise ValueError("Invalid units.")

                break

            except ValueError as e:
                print(e)
    elif xrx_cnsl_mn_mnu_cmnd_chc == "stopwatch":
        if not stopwatch_running:
            start_time = time.time()
            stopwatch_running = True
            print("Stopwatch started.")
            while stopwatch_running:
                input()
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Elapsed time: {elapsed_time:.2f} seconds")
                stopwatch_running = False
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            stopwatch_running = False
    else:
        suggested_command = did_you_mean(xrx_cnsl_mn_mnu_cmnd_chc)
        if suggested_command:
            print(f"'{xrx_cnsl_mn_mnu_cmnd_chc}' is not recognized as an operable command. Did you mean '{suggested_command}'?")
        else:
            print(f"'{xrx_cnsl_mn_mnu_cmnd_chc}' is not recognized as an operable command. Please try again.")
