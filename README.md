# Deutschlernen

python app to learn germaan vocabulary

## Structure of the code

IO operations are in io.py
  
Methods:

  - get_cardsets()
  - load_cardset(cardset_name: str)
  - add_cardset(csv_path: Path)
  - update_word(cardset_name: str, card_id: str, confidence: int)


Flashcard logic is in flashcard.py. 
A dataclass is used to store the current cardset.

Props:

   - CardSetName: str = ""
   - Cards: list | None = None
   - current_card_index: int = 0

Methods: 

  - def get_firstpage_buttons(self)
  - def get_random_card(self)
  - def load_new_set(self, set_name: str)
  - def get_front_text(self)
  - def get_back_text(self)
  - def register_button_press(self, button_id: int)

Main app logic is in app.py

## How is the data stored

In json files in the Data/ folder

The json schema is the following:
{
  "cardsets": [
    "set1",
    "set2"
  ]
}

Each cardset is stored as a json file named <cardset_name>.json

The cardset json schema is the following:

{
  "cards": [
    {
      "id": "1",
      "front": "Hello",
      "back": "Hallo",
      "confidence": 0
    },
    {
      "id": "2",
      "front": "Goodbye",
      "back": "Auf Wiedersehen",
      "confidence": 0
    }
  ]
}

The data can be imported from CSV files using the add_cardset function in io.py

The CSV file should have the following format:

id,front,back
1,Hello,Hallo
2,Goodbye,Auf Wiedersehen
