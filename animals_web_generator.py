import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_html_template(html_path):
    """reads a html template file"""
    with open(html_path, "r", encoding="utf-8") as html_file:
        return html_file.read()


def write_new_html(html_string):
    """writes a new html file"""
    with open("animals.html", "w", encoding="utf-8") as new_html_file:
        new_html_file.write(html_string)


def get_data_from_file(animal):
    """gets the value of the fields name, diet, first location and type from
    one animal of the animal data"""
    animal_name = animal.get("name")
    animal_taxonomy = animal.get("taxonomy")
    animal_scientific_name = animal_taxonomy.get("scientific_name")
    animal_characteristics = animal.get("characteristics")
    animal_diet = animal_characteristics.get("diet")
    animal_slogan = animal_characteristics.get("slogan")
    animal_location = animal.get("locations")[0]
    animal_type = animal_characteristics.get("type")
    dict_data = {
        "Scientific name": animal_scientific_name,
        "Diet": animal_diet,
        "Location": animal_location,
        "Type": animal_type,
        "Slogan": animal_slogan,
    }
    return animal_name, dict_data


def serialize_animal(animal_obj):
    """creates a html card for an item"""
    output = ""
    output += '<li class="cards__item">\n'
    a_name, data = get_data_from_file(animal_obj)
    output += f'<div class ="card__title"> {a_name} </div>\n'
    output += '<p class="card__text">\n'
    for label, value in data.items():
        if value:
            output += f"<strong>{label}:</strong> {value}<br/>\n"
    output += "</p>\n"
    output += "</li>\n"
    return output


def main():
    animals_data = load_data("animals_data.json")
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    html_data = read_html_template("animals_template.html")
    html_new_data = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
    write_new_html(html_new_data)


if __name__ == "__main__":
    main()
