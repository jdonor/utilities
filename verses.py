import sys

# dictionaries
compact_to_full_book = {
    # Old Testament
    "Gen": "Genesis",
    "Ex": "Exodus",
    "Lev": "Leviticus",
    "Nu": "Numbers",
    "Dt": "Deuteronomy",
    "Jsh": "Joshua",  # unverified
    "Jdg": "Judges",  # unverified
    "Ruth": "Ruth",  # unverified
    "Sam": "Samuel",
    "Kings": "Kings",  # unverified
    "Chr": "Chronicles",
    "Ezra": "Ezra",  # unverified
    "Neh": "Nehemiah",  # unverified
    "Es": "Esther",  # unverified
    "Job": "Job",  # unverified
    "Ps": "Psalm",
    "Pr": "Proverbs",  # unverified
    "Ecc": "Ecclesiastes",  # unverified
    "Songs": "Song of Songs",  # unverified
    "Isa": "Isaiah",
    "Jer": "Jeremiah",
    "Lam": "Lamentations",  # unverified
    "Eze": "Ezekiel",
    "Dan": "Daniel",  # unverified
    "Hos": "Hosea",  # unverified
    "Joel": "Joel",  # unverified
    "Amos": "Amos",  # unverified
    "Obad": "Obadiah",  # unverified
    "Jon": "Jonah",  # unverified
    "Mic": "Micah",  # unverified
    "Nah": "Nahum",  # unverified
    "Hab": "Habakkuk",  # unverified
    "Zeph": "Zephaniah",  # unverified
    "Hag": "Haggai",  # unverified
    "Zec": "Zechariah",
    "Mal": "Malachi",  # unverified

    # New Testament
    "Mt": "Matthew",
    "Mk": "Mark",
    "Lk": "Luke",
    "Jn": "John",
    "Acts": "Acts",
    "Rom": "Romans",
    "Cor": "Corinthians",
    "Gal": "Galatians",
    "Eph": "Ephesians",
    "Ph": "Philippians",  # unverified
    "Col": "Colossians",
    "Thess": "Thessalonians",  # unverified
    "Tim": "Timothy",
    "Titus": "Titus",
    "Phil": "Philemon",  # unverified
    "Heb": "Hebrews",
    "Jms": "James",
    "Pet": "Peter",
    "Jude": "Jude",  # unverified
    "Rev": "Revelation",
}


# functions
def convert_to_full_book(compact_line) -> str:
    verse_list = compact_line.split()

    if verse_list[0].isnumeric():
        compact_book = verse_list[1]
        book_position = 1
    else:
        compact_book = verse_list[0]
        book_position = 0

    full_book = compact_to_full_book[compact_book]
    verse_list[book_position] = full_book

    return " ".join(verse_list)


def wrap_with_bullet(unwrapped_line) -> str:
    return "<li>" + unwrapped_line + "</li>"


# main
with open('/Users/bridgeworship/Desktop/Verses/input.txt') as input_file:
    lines = []
    line = input_file.readline()

    for line in enumerate(input_file):
        line = convert_to_full_book(line[1])
        line = wrap_with_bullet(line)
        lines.append(line)

    with open('/Users/bridgeworship/Desktop/Verses/output.txt', 'w') as output_file:
        original_stdout = sys.stdout
        sys.stdout = output_file

        for line in enumerate(lines):
            print(line[1])

        sys.stdout = original_stdout
