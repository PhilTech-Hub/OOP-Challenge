# main.py

from pet import Pet

def main():
    my_pet = Pet("Buddy")

    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.get_status()

    # Bonus features
    my_pet.train("roll over")
    my_pet.train("fetch")
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
