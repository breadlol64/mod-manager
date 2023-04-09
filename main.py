import requests as r


def curseforge(mod):
    headers = {
        'Accept': 'application/json',
        'x-api-key': '1df6b2fd-b78a-43dc-91c0-1b2a1c4d6541'
    }

    response_cf = r.get('https://api.curseforge.com/v1/mods/search', params={
        'gameId': '432',
        #'searchFilter': 'create'
    }, headers=headers)

    print(response_cf.status_code)
    print(response_cf.content)


def modrinth(mod, version):
    api_url = f"https://api.modrinth.com/v2/search?query={mod}"

    response = r.get(api_url)

    if response.status_code == 200:
        mod_list = response.json()["hits"]
        count_mod = 0
        for mod in mod_list:
            print(f"{count_mod}. Mod name: '{mod['title']}' | Mod ID: '{mod['project_id']}'")
            count_mod += 1
        mod_index = input("Choose mod (left blank if don't found what you want): ")
        if mod_index != '':
            mod_index = int(mod_index)
            mod_files_resp = r.get(f"https://api.modrinth.com/v2/project/{mod_list[mod_index]['project_id']}/version")
            mod_files = mod_files_resp.json()
            count = 0
            file_indexes = []
            for mod_file in mod_files:
                if version in mod_file["game_versions"]:
                    print(f'{count}. {mod_file["version_number"]} | {mod_file["game_versions"]} | {mod_file["loaders"]}')
                    file_indexes.append(count)
                count += 1
            mod_file_index = int(input(f"Choose version ({file_indexes[0]} for lastest): "))
            mod_filename = mod_files[mod_file_index]["files"][0]["filename"]
            print(f"Downloading '{mod_filename}'")
            mod_file = mod_files_resp.json()[mod_file_index]["files"][0]["url"]

            with open(mod_filename, "wb") as f:
                f.write(r.get(mod_file).content)
    else:
        print(response.status_code)


if __name__ == "__main__":
    mod_source = input("Choose mod source:\n1.Modrinth\n")
    if mod_source == '1':
        mod_version = input("Enter version: ")
        while True:
            mod_name = input("\nEnter mod name: ")
            modrinth(mod_name, mod_version)
    elif mod_source == '2':
        print("In development!")
