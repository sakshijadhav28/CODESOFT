import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from chatbot import find_response

class ChatbotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # title
        self.setWindowTitle("Chatbot")

        # size of the window
        self.setMinimumSize(600, 400)

        # layout
        layout = QtWidgets.QVBoxLayout()

        self.text = QtWidgets.QTextEdit()
        self.text.setReadOnly(True)

        self.text.setStyleSheet("background-color: lightpink;font-size: 15pt;")

        # scroll bar
        self.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn) 

        layout.addWidget(self.text)

        self.entry = QtWidgets.QLineEdit()
        layout.addWidget(self.entry)
        self.entry.setStyleSheet("font-size: 16pt;")

        # click enter button to send the input to the chatbot
        self.entry.returnPressed.connect(self.on_send)

        # Create the send button
        send_button = QtWidgets.QPushButton("Send")
        
        send_button.setStyleSheet("color: white; background-color: black;font-size: 15pt;")
        
        send_button.clicked.connect(self.on_send)
        layout.addWidget(send_button)

        self.setLayout(layout)

    def on_send(self):
        message = self.entry.text()

        self.entry.clear()

        # Storing user msg to display
        self.text.append("You: " + message)

        # Find a response for the message
        response = find_response(message)

        self.text.append("Bot: " + response)

# Opening The APP
app = QtWidgets.QApplication(sys.argv)
window = ChatbotWindow()
window.show()

# MAIN Run
sys.exit(app.exec_())
