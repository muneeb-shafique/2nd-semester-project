from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy, QDateEdit, QComboBox, QStackedWidget, QMenuBar, QMenu, QAction, QWidget, QMessageBox
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QDate
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SocialMace")
        self.setGeometry(500, 200, 400, 600)
        self.setStyleSheet("background-color: #E3F2FD; border-radius: 0px;")
        
        # Create a modern menu bar
        self.menu_bar = self.menuBar()
        self.menu_bar.setStyleSheet("""
            QMenuBar {
                background-color: #1565C0;
                color: white;
                font: bold 14px;
            }
            QMenuBar::item {
                padding: 10px;
                border: none;
            }
            QMenuBar::item:selected {
                background-color: #42A5F5;
            }
            QMenu {
                background-color: #1565C0;
                border: none;
                padding: 5px;
            }
            QMenu::item {
                padding: 10px;
                background-color: #1565C0;
                color: white;
            }
            QMenu::item:selected {
                background-color: #42A5F5;
            }
        """)
        
        file_menu = self.menu_bar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        edit_menu = self.menu_bar.addMenu("Edit")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        edit_menu.addAction(about_action)

        # Create a stacked widget to switch between login and signup forms
        self.stacked_widget = QStackedWidget(self)

        # Create login and signup forms
        self.login_form = LoginForm(self)
        self.signup_form = SignupForm(self)

        # Add forms to the stacked widget
        self.stacked_widget.addWidget(self.login_form)
        self.stacked_widget.addWidget(self.signup_form)

        # Set the initial form to login
        self.stacked_widget.setCurrentIndex(0)

        # Set the stacked widget as the central widget
        self.setCentralWidget(self.stacked_widget)

    def switch_to_signup(self):
        self.stacked_widget.setCurrentIndex(1)

    def switch_to_login(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_about(self):
        print("About SocialMace")


class LoginForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Big "SocialMace" label at the top with margin
        self.title_label = QLabel("SocialMace", self)
        self.title_label.setFont(QFont("Arial", 36, QFont.Bold))
        self.title_label.setStyleSheet("color: #1565C0;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setContentsMargins(0, 20, 0, 0)  # Adding top margin
        layout.addWidget(self.title_label)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Login form content
        self.label = QLabel("Login", self)
        self.label.setFont(QFont("Arial", 20, QFont.Bold))
        self.label.setStyleSheet("color: #1565C0;")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.username.setFont(QFont("Arial", 12))
        self.username.setStyleSheet(self.get_input_style())
        self.username.setFixedWidth(320)
        self.username.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.username, alignment=Qt.AlignCenter)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setFont(QFont("Arial", 12))
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet(self.get_input_style())
        self.password.setFixedWidth(320)
        self.password.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.password, alignment=Qt.AlignCenter)

        self.login_button = QPushButton("Login", self)
        self.login_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.login_button.setStyleSheet(self.get_button_style())
        self.login_button.setFixedWidth(320)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        self.signup_label = QLabel("Not already a user? <a href='#'>Click here to sign up</a>", self)
        self.signup_label.setFont(QFont("Arial", 10))
        self.signup_label.setStyleSheet("color: #1565C0;")
        self.signup_label.setAlignment(Qt.AlignCenter)
        self.signup_label.setOpenExternalLinks(False)
        self.signup_label.linkActivated.connect(self.parent().switch_to_signup)
        layout.addWidget(self.signup_label)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def get_input_style(self):
        return (
            "background-color: white; color: black; border: none; "
            "padding: 10px; border: 2px solid #42A5F5; border-radius: 10px;"
        )

    def get_button_style(self):
        return (
            "background-color: #42A5F5; color: white; border-radius: 10px; "
            "padding: 10px; border: none;"
        )

    def login(self):
        print("Login button clicked")


class SignupForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Big "SocialMace" label at the top with margin
        self.title_label = QLabel("SocialMace", self)
        self.title_label.setFont(QFont("Arial", 36, QFont.Bold))
        self.title_label.setStyleSheet("color: #1565C0;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setContentsMargins(0, 20, 0, 0)  # Adding top margin
        layout.addWidget(self.title_label)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Signup form content
        self.label = QLabel("Signup", self)
        self.label.setFont(QFont("Arial", 20, QFont.Bold))
        self.label.setStyleSheet("color: #1565C0;")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.full_name = QLineEdit(self)
        self.full_name.setPlaceholderText("Full Name")
        self.full_name.setFont(QFont("Arial", 12))
        self.full_name.setStyleSheet(self.get_input_style())
        self.full_name.setFixedWidth(320)
        self.full_name.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.full_name, alignment=Qt.AlignCenter)

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.username.setFont(QFont("Arial", 12))
        self.username.setStyleSheet(self.get_input_style())
        self.username.setFixedWidth(320)
        self.username.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.username, alignment=Qt.AlignCenter)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setFont(QFont("Arial", 12))
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet(self.get_input_style())
        self.password.setFixedWidth(320)
        self.password.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.password, alignment=Qt.AlignCenter)

        self.date_of_birth = QDateEdit(self)
        self.date_of_birth.setDate(QDate.currentDate())
        self.date_of_birth.setFont(QFont("Arial", 12))
        self.date_of_birth.setStyleSheet(self.get_input_style() + " QDateEdit::drop-down {border: none;}")  # Removing up-down buttons
        self.date_of_birth.setFixedWidth(320)
        self.date_of_birth.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.date_of_birth, alignment=Qt.AlignCenter)

        self.country = QComboBox(self)
        self.country.addItems(["Select Country", "USA", "Canada", "UK", "Australia", "India"])
        self.country.setFont(QFont("Arial", 12))
        self.country.setStyleSheet(self.get_input_style() + " QComboBox::drop-down {border: none;} QComboBox::down-arrow {border: none;}")  # Removing dropdown arrow
        self.country.setFixedWidth(320)
        layout.addWidget(self.country, alignment=Qt.AlignCenter)

        self.signup_button = QPushButton("Signup", self)
        self.signup_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.signup_button.setStyleSheet(self.get_button_style())
        self.signup_button.setFixedWidth(320)
        self.signup_button.clicked.connect(self.signup)
        layout.addWidget(self.signup_button, alignment=Qt.AlignCenter)

        self.login_label = QLabel("Already a user? <a href='#'>Click here to login</a>", self)
        self.login_label.setFont(QFont("Arial", 10))
        self.login_label.setStyleSheet("color: #1565C0;")
        self.login_label.setAlignment(Qt.AlignCenter)
        self.login_label.setOpenExternalLinks(False)
        self.login_label.linkActivated.connect(self.parent().switch_to_login)
        layout.addWidget(self.login_label)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def get_input_style(self):
        return (
            "background-color: white; color: black; border: none; "
            "padding: 10px; border: 2px solid #42A5F5; border-radius: 10px;"
        )

    def get_button_style(self):
        return (
            "background-color: #42A5F5; color: white; border-radius: 10px; "
            "padding: 10px; border: none;"
        )

    def signup(self):
        # Validation
        if not self.full_name.text() or not self.username.text() or not self.password.text() or self.country.currentIndex() == 0:
            QMessageBox.warning(self, "Input Error", "All fields must be filled!")
            return
        print("Signup button clicked")
        print(f"Full Name: {self.full_name.text()}")
        print(f"Username: {self.username.text()}")
        print(f"Password: {self.password.text()}")
        print(f"Date of Birth: {self.date_of_birth.date().toString('yyyy-MM-dd')}")
        print(f"Country: {self.country.currentText()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
