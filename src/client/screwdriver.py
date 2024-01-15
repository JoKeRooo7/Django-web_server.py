import argparse
import requests

BASE_URL = "http://127.0.0.1:8888/"


def upload_file(local_file):
    URL = BASE_URL + "upload/"

    with open(local_file, "rb") as file:
        files = {'audio_file': (local_file, file)}
        response = requests.post(URL, files=files)

    if response.status_code == 302:
        print("Получен код состояния 302 (Found), произведено перенаправление")
    elif response.status_code == 200:
        print("""
            Файл был отправлен успешно.
            Если ваш файл не был загружен на сервер,
            проверьте расширение файла и
            его уникальное названия
        """)
    else:
        print(f"HTTP error: {response.status_code}")


def music_files():
    URL = BASE_URL + "list/"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        music_files = data.get('music_files', [])
        print("Список музыкальных файлов:")
        for file in music_files:
            print(file)
    else:
        print(f"http error: {response.status_code}")


def read_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action")
    upload_parser = subparsers.add_parser("upload")
    upload_parser.add_argument("local_file", type=str)
    subparsers.add_parser("list")
    return parser.parse_args()


def main():
    args = read_args()

    if args.action == "list":
        music_files()
    if args.action == "upload":
        upload_file(args.local_file)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
