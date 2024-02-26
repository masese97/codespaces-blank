def main():
    # Ask the user for their name, age, and location
    name = input("What is your name? ")
    age = input("How old are you? ")
    location = input("Where are you located? ")

    # Print out a personalized message
    print(f"Hello {name}! It's nice to meet you.")
    print(f"You are {age} years old and located in {location}.")

if __name__ == "__main__":
    main()
