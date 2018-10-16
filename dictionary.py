import requests
import json

cache = []
error = []

with open("error.json", "r") as e:
    error = json.load(e)

with open("data.json", "r") as f:
    cache = json.load(f)

app_id = #Enter app id
app_key = #Enter app key
language = 'en'


# DB error Search

def search(word_id):
    for i in error:
        if word_id == i["kw"]:
            print("No result found")
            return "No result found"

            # DB Search

    for i in cache:
        if word_id == i["kw"]:
            print(i)
            return i

            # Search

    else:
        try:
            url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
            r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
            resp = dict(
                kw=word_id,
                resp=r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
            )
            cache.append(resp)
            print(resp)
            with open('data.json', 'w') as f:
                json.dump(cache, f, indent=4)
            return resp

        # Exception dumping

        except Exception as e:
            er = dict(kw=word_id)
            print("No result found")
            error.append(er)
            with open('error.json', 'w') as f:
                json.dump(error, f, indent=4)
            return "No result found"

if __name__ == '__main__':
    word_id = input("search :")
    search(word_id)
