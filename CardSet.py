from dataclasses import dataclass
from typing import List, Set


@dataclass
class CardSet:
    CardSetName: str = ""
    Cards: list | None = None
    current_card_index: int = 0
    
    def get_firstpage_buttons(self):
      pass
      
    def get_random_card(self):
      pass
    
    def load_new_set(self, set_name: str):
      pass
    
    def get_front_text(self):
      pass
    
    def get_back_text(self):
      pass
    
    def register_button_press(self, button_id: int):
      pass