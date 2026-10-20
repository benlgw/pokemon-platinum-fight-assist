from os import system, remove; system('clear||cls')

from pyscreenshot import grab
from pytesseract import image_to_string
from PIL import Image
from difflib import get_close_matches

import pokemon_stats

# --------------------------

all_pokemon = []

for pokemon in pokemon_stats.pokemon:
    all_pokemon.append(pokemon)

# ---------------------------

def get_opponent_pokemon() -> list[str]:
    check_single = single()
    if check_single:
        return check_single
    check_duo = duo()
    if check_duo:
        return check_duo
    check_duo_single = duo_single()
    if check_duo_single:
        return check_duo_single

def single() -> list[str]:
    opponent_image = grab(bbox=(5,195,330,255))
    opponent_image.save('opponent_1_name.png')
    opponent = ocr('opponent_1_name.png')
    # remove('opponent_1_name.png')
    return opponent

def duo() -> list[str]:
    opponent_image_1 = grab(bbox=(35,95,360,160))
    opponent_image_1.save('opponent_1_name.png')
    opponent_1 = ocr('opponent_1_name.png')
    # remove('opponent_1_name.png')

    opponent_image_2 = grab(bbox=(5,240,330,300))
    opponent_image_2.save('opponent_2_name.png')
    opponent_2 = ocr('opponent_2_name.png')
    # remove('opponent_2_name.png')

    return opponent_1, opponent_2

def duo_single() -> list[str]:
    opponent_image = grab(bbox=(5,240,330,300))
    opponent_image.save('opponent_1_name.png')
    opponent = ocr('opponent_1_name.png')
    # remove('opponent_1_name.png')
    return opponent

def ocr(file: str) -> Image:
    config = r'--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz. '

    image = Image.open(file)
    image = image.convert('L').resize((image.width * 2, image.height * 2), Image.NEAREST)
    image = image.point(lambda x: 0 if x < 128 else 255, '1')
    text = image_to_string(image, config = config).title().strip()

    closest = get_close_matches(text, all_pokemon, n = 1, cutoff = 0.6)

    if closest:
        return closest

    config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz. '
    text = image_to_string(image, config = config).title().strip()
    closest = get_close_matches(text, all_pokemon, n = 1, cutoff = 0.6)
    if closest:
        return closest

if __name__ == '__main__':
    print(get_opponent_pokemon())
