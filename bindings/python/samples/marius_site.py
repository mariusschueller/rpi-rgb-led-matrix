import requests
import marius_video
import marius
import marius_no_matrix

def get_data():
    URL = "https://flask-vercel-led.vercel.app/"
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()
    return data



if __name__ == '__main__':
    data = get_data()

    #marius_video.show(data)
    a = marius.Marius()
    restored_data = marius_video.convert_to_ndarray(data)

    while True:
        for i in range(len(restored_data)):
            a.run(restored_data)


