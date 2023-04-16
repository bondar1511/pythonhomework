# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
# Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). 
# Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные),
# можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.


from curses import window
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWimdow, QMessageBox
from PyQt5.Qtcore import Qt, QTimer
import csv
import datetime

def aplic():
    app = QApplication(sys.argv)
    okno = window()
    okno.show()
    sys.exit(app.exec())
    # if__name__ == '__main__':
    #      aplic()

class Window(QMainWimdow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.id = id
        self.setWindowwTitle("заметки")
        self.setGeimetry(400, 400, 600, 300)
        self.text_data = QtWidgets.QLabel(self)
        self.text_data.setText("Выберите дату")
        self.text_data.adjustsize()
        self.text_data.move(10,52)

        self.text_time = QtWidgets.Qlabel(self)
        self.text_time.setText("выберите время")
        self.text_time.adjustsize()
        self.text_time.move(10,103)

        self.data = QtWidgets.QDateEdit(self)
        self.data.move(100,50)
        self.data.adjustSize()
        
        self.time = QtWidgets.QTimeEdit(self)
        self.time.move(110,100)
        self.time.adjustSize()

        self.sobati = QtWidgets.QLineEdit(self)
        self.sobati.setGeometry(100,150,160,30)
        self.sobati.adjustSize()
        self.sobati.setPlaceholderText("Введите событие")

        self.knopka = QtWidgets.QPushButton(self)
        self.knopka.move(210,80)
        self.knopka.setText("Готово")
        self.knopka.adjustSize()

class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NoteService:
    def __init__(self):
        self.notes = []

    def addNote(self, note):
        self.notes.append(note) 

    def editNote(self, id, title, body):
        for note in self.notes:
           if note.id == id:
                note.title = title
                note.body = body
                note.timestamp = datetime.now()
                return True
        return False

    def deleteNote(self, id):
        for i, note in enumerate(self.notes):
            if note.id == id:
                del self.notes[i]
                return True
        return False
  
    def readNote(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None
    
    def saveNotes(self, filename):
        filename = "certification\\notes.csv"
        with open(filename, 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['id', 'title', 'body', 'timestamp'])
            for note in self.notes:
                writer.writerow([note.id, note.title, note.body, note.timestamp])
    
    def loadNotes(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                id = int(row[0])
                title = row[1]
                body = row[2]
                timestamp = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
                self.notes.append(Note(id, title, body, timestamp))