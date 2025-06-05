import random
import string
import time

import requests
import os


def random_email_generator(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


email = random_email_generator() + '@yopmail.com'


def random_username_generator(length=8):
    characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(characters) for i in range(length))
    if username[0].isdigit():
        username = random.choice(string.ascii_letters) + username[1:]
    return username


random_username = random_username_generator(3)
print(random_username)


def get_random_word_from_api():
    try:
        response = requests.get("https://api.datamuse.com/words?ml=meaning_like&max=100000")
        response.raise_for_status()
        words = [item["word"] for item in response.json()]
        return random.choice(words)
    except requests.RequestException as e:
        print("Datamuse API request failed:", e)
        return None


print("Random word:", get_random_word_from_api())


# Predefined list of words
words = [
    "ability", "absence", "accept", "advice", "agency", "allergy", "amazing", "amount", "analysis", "ancient",
    "applied", "awesome", "balance", "beacon", "benefit", "bitter", "bright", "candle", "caring", "charge",
    "clarity", "classic", "comfort", "common", "concrete", "content", "courage", "create", "danger", "delight",
    "design", "divine", "dynamic", "eager", "eclipse", "engage", "entity", "essential", "fancy", "feature",
    "fellow", "fiend", "flavor", "freedom", "future", "gather", "genuine", "global", "grace", "guitar", "happy",
    "honest", "impose", "impact", "inspire", "island", "journey", "jungle", "knight", "laptop", "legacy", "letter",
    "lively", "magic", "measure", "method", "miracle", "mosaic", "muse", "nature", "noble", "novel", "ocean",
    "officer", "optimize", "origin", "puzzle", "perfect", "power", "present", "quiet", "quirky", "quote", "react",
    "reach", "remark", "reveal", "ritual", "rocket", "sail", "sample", "silent", "simple", "smart", "sober", "soul",
    "space", "spirit", "stone", "survey", "tactics", "taste", "temple", "thrive", "tooth", "unique", "universe",
    "valid", "value", "vivid", "voice", "vulture", "wealth", "wings", "wonder", "yarn", "yearn", "zeal", "zen",
    "zebra", "zero", "zodiac", "zoom", "affection", "baggage", "billion", "chaos", "classical", "discovery",
    "enchanted", "examine", "euphoria", "feeling", "frighten", "harmful", "innocence", "jovial", "kingdom",
    "laughter", "mansion", "mystery", "nourish", "optimistic", "potion", "quicksand", "quaint", "romance", "safeguard",
    "seafood", "serenity", "twilight", "unveil", "visionary", "wanderer", "whisper", "wish", "alchemy", "blossom",
    "brilliance", "breeze", "divinity", "explore", "fancy", "flicker", "galaxy", "glitter", "graceful", "harmonic",
    "imaginary", "irony", "jewel", "landscape", "mermaid", "paradise", "poetry", "scenic", "serenity", "thunder",
    "transcend", "universe", "voyage", "whimsical", "wonder", "youth", "zealot", "ambition", "melody", "tapestry",
    "embark", "fascinate", "pinnacle", "alchemy", "legacy", "grace", "whimsy", "intrepid", "seraphic", "elusive",
    "mythic", "conscious", "unveil", "aspire", "odyssey", "glistening", "quench", "immortal", "ethereal", "radiance",
    "solitude", "vibrance", "effervescent", "mystical", "passionate", "echo", "vibrant", "expedition", "tantalizing",
    "spirited", "contemplative", "delight", "phantom", "majestic", "agile", "serene", "tranquil", "epic", "arcane",
    "celestial", "turbulent", "reverence", "utopia", "illusion", "fiery", "unleash", "luminous", "destiny", "fortitude",
    "resolve", "dazzle", "elemental", "harmony", "adventure", "arcadia", "solace", "leap", "solstice", "frost",
    "flicker", "awaken", "vivid", "persistent", "clarity", "conquer", "insight", "flame", "infinity", "elevate",
    "gracious", "creativity", "crimson", "valor", "wander", "lush", "rebirth", "inspired", "radiant", "bold",
    "vanguard", "eternal", "sacred", "whimsical", "rejuvenate", "cascade", "refine", "beacon", "apex", "aura",
    "glimmer", "majestic", "invincible", "diverse", "bold", "persistence", "storm", "discovery", "seeker", "inspire",
    "passion", "rise", "moonlight", "zephyr", "mystic", "brave", "shift", "bliss", "sparkle", "spark", "awakening",
    "luminary", "noble", "dream", "elixir", "pursuit", "wanderlust", "vision", "sublime", "vital", "flare", "glow",
    "journey", "inspire", "celestial", "whisper", "eternity", "spark", "dawn", "ignite", "tornado", "perspective",
    "paragon", "epiphany", "meditation", "peaceful", "pursue", "overcome", "wild", "boundary", "seeking", "exhilarate",
    "discovery", "invincible", "awaken", "renew", "vigil", "rising", "reflection", "blissful", "sky", "constellation",
    "thrive", "illumination", "endless", "resilience", "adventure", "ethereal", "shining", "restoration", "glimmer",
    "harmony", "mountain", "vibrance", "grace", "ethereal", "divinity", "thrive", "echo", "ascend", "rays", "momentum"
]

def get_random_word():
    if words:
        word = random.choice(words)  # Select a random word
        words.remove(word)  # Remove the word to ensure it won't be repeated
        print(f"Random word use: {word}")
    else:
        print("No more words left to choose from!")

get_random_word()  # Call the function multiple times to get different words

def random_password_generator(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    all_characters = uppercase + lowercase + digits + special_characters
    password += [random.choice(all_characters) for i in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)


random_password = random_password_generator(12)


def get_relative_image_path(base_file_path, image_file_path):
    return os.path.relpath(image_file_path, os.path.dirname(base_file_path))


base_path = "/home/web-h-028/PycharmProjects/shrubs_automation/shrubs_web/test_positive_flow.py"
image_path = "/home/web-h-028/PycharmProjects/shrubs_automation/shrubs_web/image"
relative_path = get_relative_image_path(base_path, image_path)
print(relative_path)
