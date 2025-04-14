def main():
    fahrenheit = float(input("Enter the temperature in Fahremheit:"))
    celsius = (fahrenheit - 32) * 5.0/ 9.0
    print(f"the temperature:{fahrenheit}F is =  {celsius}C")

if __name__ == '__main__':
  main()