import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QPushButton, QVBoxLayout

USER = "Admin"
PASSWORD = "Passport"

class LoginWindow(QDialog):

    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi('login1.ui', self)

        # self.showEvent = self.on_dialog_shown


        self.FocusedField = None

        self.pw_firsttry = True
        self.pw_hidden = True
        self.nm_firsttry = True
        self.pw_toggle = False


        self.password.mousePressEvent = self.on_password_click
        self.username.mousePressEvent = self.on_user_click

        self.password.focusOutEvent = self.on_edit_finished
        self.username.focusOutEvent = self.on_edit_finished

        self.password.focusInEvent = self.on_password_focused
        self.username.focusInEvent = self.on_user_focused


        self.showpass.clicked.connect(self.toggle_pass)

        self.password.returnPressed.connect(self.validate)
        self.pushButton.clicked.connect(self.validate)

    def on_password_click(self, event):

        self.FocusedField = "password"
        if self.pw_firsttry:
            self.pw_firsttry = False
            self.password.clear()
            print("clear password")
            if self.pw_hidden: self.password.setEchoMode(QLineEdit.Password)

        QLineEdit.mousePressEvent(self.password, event)

    def on_password_focused(self, event):
        print("password focused")
        self.FocusedField = "password"
        if self.pw_firsttry:
            self.pw_firsttry = False
            self.password.clear()
            if self.pw_hidden: self.password.setEchoMode(QLineEdit.Password)

        QLineEdit.focusInEvent(self.password, event)

    def on_user_click(self, event):
        self.FocusedField = "username"
        if self.nm_firsttry:
            self.username.clear()
            print("clear username")
            self.nm_firsttry = False

        QLineEdit.mousePressEvent(self.username, event)

    def on_user_focused(self, event):
        print("user focused")
        self.FocusedField = "username"
        if self.nm_firsttry:
            self.username.clear()
            print("clear username")
            self.nm_firsttry = False

        QLineEdit.focusInEvent(self.username, event)


    def validate(self):
        passwd = self.password.text()
        user = self.username.text()

        if user == USER and passwd == PASSWORD:
            #send to next page
            widget.setCurrentWidget(success_window)
        else:
            #clear password, count try attempts
            self.password.clear()
            QtWidgets.QMessageBox.warning(self, "Invalid Credentials", "Username or password is incorrect.")
            #widget.setCurrentWidget(login_window)
            self.password.setFocus()
            self.show()
        print(f"user {user}\npassword {passwd}")

    def on_edit_finished(self, event):
        field = getattr(self, self.FocusedField)
        print("focusfinished",self.FocusedField)
        #print(str(field.objectName()))
        if not field.text():
            if self.FocusedField == "password":
                self.pw_firsttry = True
                self.password.setEchoMode(QLineEdit.Normal)
            else:
                self.nm_firsttry = True
            field.setText(self.FocusedField)
        if field:
            QLineEdit.focusOutEvent(field, event)

    def toggle_pass(self):
        if not self.pw_toggle:
            self.pw_toggle = not self.pw_toggle
            self.showpass.setIcon(QtGui.QIcon("imgs/open.png"))
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.pw_toggle = not self.pw_toggle
            self.showpass.setIcon(QtGui.QIcon("imgs/closed.png"))
            if not self.pw_firsttry: self.password.setEchoMode(QLineEdit.Password)

class Success(QDialog):
    def __init__(self):
        super(Success, self).__init__()
        loadUi('success.ui', self)

        if not self.layout():
            self.setLayout(QVBoxLayout())

        self.button = QPushButton("Go back")

        self.button.clicked.connect(self.logout)

        self.layout().addWidget(self.button)

    def logout(self):
        widget.setCurrentWidget(login_window)




if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login_window = LoginWindow()
    #print(dir(login_window.pushButton))
    success_window = Success()

    widget.addWidget(login_window)
    widget.addWidget(success_window)
    widget.setFixedWidth(550)
    widget.setFixedHeight(650)
    widget.show()
    sys.exit(app.exec_())
