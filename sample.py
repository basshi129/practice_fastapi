import requests
import json

def main():
    url="http://127.0.0.1:8000"
    body={
        "x": 2,
        "y": 3
    }
    res = requests.post(url, json.dumps(body))

    print(res.json())

    res = requests.get(url)
    print(res.json())


if __name__ == "__main__":
    main()