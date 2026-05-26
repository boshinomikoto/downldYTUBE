from pytubefix import YouTube, Playlist


def main():
    link = input("Введите ссылку: ").strip()

    print("\n1. Скачать видео")
    print("2. Скачать субтитры")
    print("3. Скачать плейлист")
    print("4. Получить URL каждого видео в плейлисте")

    try:
        action = int(input("\nВыберите действие: "))
    except ValueError:
        print("Ошибка: введите число от 1 до 4")
        return

    if action == 1:
        try:
            yt = YouTube(link)
            ans = input("Скачать в максимальном качестве? (y/n): ").strip().lower()
            if ans == "y":
                yt.streams.get_highest_resolution().download()
            else:
                yt.streams.first().download()
            print(yt.title, "— готово")
        except Exception as e:
            print(f"Ошибка: {e}")

    elif action == 2:
        try:
            yt = YouTube(link)
            lang = input("Введите код языка [en, ru, uk]: ").strip().lower()
            if lang in yt.captions:
                yt.captions[lang].save_captions("Sub")
                print(yt.title, "— субтитры сохранены")
            else:
                print(f"Субтитры для языка '{lang}' не найдены")
                print("Доступные языки:", list(yt.captions.keys()))
        except Exception as e:
            print(f"Ошибка: {e}")

    elif action == 3:
        try:
            playlist = Playlist(link)
            print(f"Скачиваю плейлист [{playlist.title}]")
            for video in playlist.videos:
                try:
                    video.streams.first().download()
                    print(video.title, "— готово")
                except Exception as e:
                    print(f"Ошибка при скачивании видео: {e}")
        except Exception as e:
            print(f"Ошибка: {e}")

    elif action == 4:
        try:
            playlist = Playlist(link)
            for video in playlist.videos:
                print(f"{video.title} — {video.watch_url}")
        except Exception as e:
            print(f"Ошибка: {e}")

    else:
        print("Ошибка: выберите действие от 1 до 4")


if __name__ == "__main__":
    main()