import requests
import marius_video

def get_data():
    URL = "https://flask-vercel-led.vercel.app/"
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()
    marius_video.show(data)
    print(data)

if __name__ == '__main__':
    get_data()
