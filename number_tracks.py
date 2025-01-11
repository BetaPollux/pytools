from mutagen.easyid3 import EasyID3
import argparse
import os

parser = argparse.ArgumentParser(
    prog="Number Mp3 titles",
    description="Prefixes ID3 tag title with track number, because many cars play albums alphabetically by title",
)

parser.add_argument("dir", help="Directory of MP3 files to process")

args = parser.parse_args()

proceed = input(
    f"Change titles for ALL MP3 tracks within {args.dir} and its subdirectories? (Y/N): "
)

if proceed.upper() == "Y":
    for dirpath, dirnames, filenames in os.walk(args.dir):
        print(dirpath)
        for f in filenames:
            if f.endswith(".mp3"):
                path = os.path.join(dirpath, f)
                audio = EasyID3(path)
                audio["title"] = f"{audio['tracknumber'][0]} {audio['title'][0]}"
                audio.save()
                print(*audio["title"])
else:
    print("Cancelled")
