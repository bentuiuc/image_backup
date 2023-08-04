from pathlib import Path

def split_to_batch(p: str = '..'):
    pictures_location = Path(p)
    pictures_filename = [f for f in pictures_location.iterdir()]
    print(pictures_filename[0])

if __name__ == "__main__":
    split_to_batch()

