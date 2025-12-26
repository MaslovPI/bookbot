from collections import Counter


def get_num_words(text):
    return len(text.split())


def get_num_characters(text):
    symbols = Counter(text)
    return symbols


def sort_on(items):
    return items["num"]


def sort_characters(characters):
    return sorted(
        [{"char": k, "num": v} for k, v in characters.items()],
        key=sort_on,
        reverse=True,
    )
