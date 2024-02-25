# lecture2
# to run file: python -W ignore::DeprecationWarning .\main1.py
PyQt-homework
Login Page

main1.py - მთავარი ფაილი სადაც შექმნილია ორი "QDialog" საბკლასი, "LoginWindow" და "Success", რომლებიც დაკავშირებულია ერთმანეთთან QtWidgets.QStackedWidget()-ით.
ფაილის აშვებისას იხსნება LoginWindow, რომელიც შედგება ორი "QLineEdit" (username & password) და ორი "QPushButton" (pushButton & showpass)

ავტორიზაცია ხდება pushButton-ზე დაკლიკებით ან password ფილდ-ში ენთერის დაჭერით.

showpass - password- ფილდის მალულ ან ხილვად რეჯიმში გადაყვანა (default=hidden)

tab order -> username -> password -> showpass -> pushButton


username & password ფილდებზე გამოყენებულია შესაბამისი ფლეისჰოლდერები, რომლიბიც ფოკუსის შემთხვევაში იშლება და შესაძლებელი ველში ინფორმაციის შეყვანა, თუ ფოკუსის გადასვლისას ველი ცარიელია, ველი ივსება ისევ ფლეისჰოლდერის მნიშვნელობით

