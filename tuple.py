def get_person_info() -> tuple:
    name = input("Enter name: ")
    if not name:
        raise ValueError("Name cannot be empty")

    age = input("Enter age: ")
    if not age.isdigit() or int(age) <= 0:
        raise ValueError("Age must be a positive integer")

    address = input("Enter address: ")
    if not address:
        raise ValueError("Address cannot be empty")

    person = (name, int(age), address)
    return person


def update_person_info(person: tuple) -> tuple:
    if not person:
        raise ValueError("Person tuple cannot be empty")

    name, age, address = person
    new_name = input("\nEnter new name (leave blank to keep current): ")
    if new_name:
        name = new_name

    new_age = input("Enter new age (leave blank to keep current): ")
    if new_age:
        if not new_age.isdigit() or int(new_age) <= 0:
            raise ValueError("Age must be a positive integer")
        age = int(new_age)

    new_address = input("Enter new address (leave blank to keep current): ")
    if new_address:
        address = new_address

    updated_person = (name, age, address)
    return updated_person


def print_person_info(person: tuple):
    name, age, address = person
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Address: {address}")


person = get_person_info()
print("\nOriginal:\n")
print_person_info(person)

updated_person = update_person_info(person)
print("\nUpdated:")
print_person_info(updated_person)
