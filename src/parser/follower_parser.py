import json

# This function will parse the followers_1.json file and return 
# a list of names of the people who are following you
def parse_followers(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    names_list = []
    for each in data:
        names_list.append(each["string_list_data"][0]["value"])

    return names_list

# This function will parse the following.json file and return 
# a list of names of the people you are following
def parse_following(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    names_list = []
    for each in data["relationships_following"]:
        names_list.append(each["title"])

    return names_list