def get_list_of_food_nutrients(fooddata):
    for search_result in fooddata:
        for section in search_result:
            if isinstance(section, list):
                for table in section:
                    print table["nutrient"]
            else:
                print section
            print ""

def parse_sections(section):
    nutrient_names = ["Total lipid (fat)", "Calcium, Ca", "Carbohydrate, by difference", "Energy", "Sugars, total"]

    entries = {}

    for table in section:
        if table["nutrient"] in nutrient_names:
            entries[table["nutrient"]] = table["value"] + table["unit"]

    return entries

def show_nutrients(fooddata):
    results = {}
    cur_result = ""
    
    for search_result in fooddata:
        for section in search_result:
            if not isinstance(section, list):
                results[section] = {}
                cur_result = section
            else:
                results[cur_result] = parse_sections(section)

    return results    
