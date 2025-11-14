from dataclasses import dataclass
import json
from pathlib import Path
import csv
from typing import Dict

CARDSET_PATH = "Data"


def get_cardsets() -> set[str]:
    with open('cardsets.json', 'r') as f:
        card_list = json.load(f)[["cardsets"]]

    return set(card_list)


def load_cardset(cardset_name: str) -> list[Dict]:
    """ 
    Load a cardset from a JSON file and return its cards as a list of dictionaries.

    Args:
        cardset_name (str): the name of the cardset to load

    Returns:
        list[Dict]: a list of cards in the cardset
    """
    with open(Path(CARDSET_PATH, f"{cardset_name}.json"), 'r') as f:
        cardset = json.load(f)["cards"]

    return cardset


def add_cardset(csv_path: Path) -> None:
    """
    Convert a CSV file to JSON and save it in the cardsets directory.

    The CSV file should have the following format:
    id,front,back
    1,Hello,Hola
    2,Goodbye,Adiós

    The resulting JSON file will have the following format:
    {
      "cards": [
        {
          "id": "1",
          "front": "Hello",
          "back": "Hola",
          "confidence": 0
        },
        {
          "id": "2",
          "front": "Goodbye",
          "back": "Adiós",
          "confidence": 0
        }
      ]
    } 

    """
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        cards = []
        for row in csv_reader:
            if line_count == 0:
                csv_header = row
                if csv_header != ['id', 'front', 'back']:
                    return None  # raise error
            else:
                id, front, back = row
                cards.append({
                    "id": id,
                    "front": front,
                    "back": back,
                    "confidence": 0
                })
            line_count += 1

        with open(Path(CARDSET_PATH, f"{csv_path.stem}.json"), 'w') as json_file:
            json.dump({"cards": cards}, json_file, indent=4)

        with open('cardsets.json', 'r') as f:
            cardsets = json.load(f)
            
        cardsets["cardsets"].append(csv_path.stem)
        with open('cardsets.json', 'w') as f:
            json.dump(cardsets, f, indent=4)


def update_word(cardset_name: str, card_id: str, confidence: int) -> None:
    pass

