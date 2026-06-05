from pet import Pet

class TestPet:
    @staticmethod
    def main():

        # Create object
        my_pet = Pet()

        # User input
        name = input("Enter pet name: ")
        animal_type = input("Enter pet type (Dog, Cat, Bird, etc.): ")
        age = int(input("Enter pet age: "))

        # Set values
        my_pet.set_name(name)
        my_pet.set_animal_type(animal_type)
        my_pet.set_age(age)

        # Output
        print("\n=== PET INFORMATION ===")
        print("Name:", my_pet.get_name())
        print("Type:", my_pet.get_animal_type())
        print("Age:", my_pet.get_age())


TestPet.main()