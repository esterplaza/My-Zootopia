import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_data_from_file(animal):
    """gets the value of the fields name, diet, first location and type from
    one animal of the animal data"""
    animal_name = animal.get("name")
    animal_characteristics = animal.get("characteristics")
    animal_diet = animal_characteristics.get("diet")
    animal_location = animal.get("locations")[0]
    animal_type = animal_characteristics.get("type")
    return animal_name, animal_diet, animal_location, animal_type


def main():
    animals_data = load_data("animals_data.json")
    for animal in animals_data:
        a_name, a_diet, a_location, a_type = get_data_from_file(animal)
        data = {"Name": a_name, "Diet": a_diet, "Location": a_location,
                "Type": a_type}
        for label, value in data.items():
            if value:
                print(f"{label}: {value}")
        print()


if __name__ == "__main__":
    main()
