import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, 
    QScrollArea, QFrame
)
from PyQt6.QtCore import Qt

# --- Placeholder functions for your data model ---
def get_elements_list():
    # Replace with your implementation
    return ["Button A", "Button B", "Button C", "Button D"]

def get_first_text(label):
    # Replace with your implementation
    return f"First text for {label}"

def get_second_text(label):
    # Replace with your implementation
    return f"Second text for {label}"

def record_pressed_button(button_id):
    print(f"Button {button_id} pressed")  # Replace with your implementation

# --- Main application window ---
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt App")
        self.setGeometry(100, 100, 400, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.show_list_screen()

    # Screen 1: List of clickable buttons
    def show_list_screen(self):
        self.clear_layout()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        self.button_labels = get_elements_list()
        for label in self.button_labels:
            btn = QPushButton(label)
            btn.clicked.connect(lambda checked, l=label: self.show_detail_screen(l))
            scroll_layout.addWidget(btn)

        scroll.setWidget(scroll_content)
        self.layout.addWidget(scroll)

    # Screen 2: Detail screen
    def show_detail_screen(self, label):
        self.clear_layout()
        self.current_label = label

        # Text display
        self.text_label = QLabel(get_first_text(label))
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.text_label, stretch=1)

        # Middle button
        self.middle_button = QPushButton("Show more")
        self.middle_button.clicked.connect(self.show_second_text)
        self.layout.addWidget(self.middle_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Bottom buttons
        bottom_layout = QHBoxLayout()
        for i in range(1, 4):
            btn = QPushButton(f"Button {i}")
            btn.clicked.connect(lambda checked, x=i: self.bottom_button_pressed(x))
            bottom_layout.addWidget(btn)
        self.layout.addLayout(bottom_layout)

    # Middle button click
    def show_second_text(self):
        self.text_label.setText(get_second_text(self.current_label))
        self.middle_button.hide()

    # Bottom buttons click
    def bottom_button_pressed(self, button_id):
        record_pressed_button(button_id)
        self.text_label.setText(get_first_text(self.current_label))
        self.middle_button.show()

    # Helper to clear layout
    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
