import requests as r


def curseforge(mod):
    pass


def modrinth(mod):
    api_url = f"https://api.modrinth.com/v2/search?query={mod}"

    response = r.get(api_url)

    if response.status_code == 200:
        mod_list = response.json()["hits"]
        for mod in mod_list:
            print(f"Mod name: '{mod['title']}' | Mod ID: '{mod['project_id']}'")
    else:
        print(response.status_code)


if __name__ == "__main__":
    mod_name = input("Enter mod name: ")
    modrinth(mod_name)
