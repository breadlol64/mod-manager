import requests as r


def curseforge(mod):
    pass


def modrinth(mod):
    api_url = f"https://api.modrinth.com/v2/search?query={mod}"

    response = r.get(api_url)

    if response.status_code == 200:
        mod_list = response.json()["hits"]
        count_mod = 0
        for mod in mod_list:
            print(f"{count_mod}. Mod name: '{mod['title']}' | Mod ID: '{mod['project_id']}'")
            count_mod += 1
        mod_index = input("Choose mod (left blank if don't found what you want): ")
        if mod_index == '':
            pass
        else:
            mod_index = int(mod_index)
            mod_files_resp = r.get(f"https://api.modrinth.com/v2/project/{mod_list[mod_index]['project_id']}/version")
            mod_files = mod_files_resp.json()
            count = 0
            for mod_file in mod_files:
                print(f'{count}. {mod_file["version_number"]} | {mod_file["game_versions"]} | {mod_file["loaders"]}')
                count += 1
            mod_file_index = int(input("Choose version (0 for lastest): "))
            mod_filename = mod_files[mod_file_index]["files"][0]["filename"]
            print(f"Downloading '{mod_filename}'")
            mod_file = mod_files_resp.json()[mod_file_index]["files"][0]["url"]

            with open(mod_filename, "wb") as f:
                f.write(r.get(mod_file).content)
    else:
        print(response.status_code)


if __name__ == "__main__":
    while True:
        mod_name = input("\nEnter mod name: ")
        modrinth(mod_name)
