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
        mod_id = input("Enter mod id: ")

        mod_files_resp = r.get(f"https://api.modrinth.com/v2/project/{mod_id}/version")
        print(f'Downloading \'{mod_files_resp.json()[0]["files"][0]["filename"]}\'')
        mod_file = mod_files_resp.json()[0]["files"][0]["url"]

        with open(mod_files_resp.json()[0]["files"][0]["filename"], "wb") as f:
            f.write(r.get(mod_file).content)
    else:
        print(response.status_code)


if __name__ == "__main__":
    mod_name = input("Enter mod name (left blank if search by id): ")
    modrinth(mod_name)
