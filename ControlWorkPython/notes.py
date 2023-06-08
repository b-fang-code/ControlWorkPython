import json
from constructor import Note
from datetime import datetime


class Notes:
    #  конструктор класса Notes, который принимает путь к файлу с заметками
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []

    #  метод загрузки заметок из файла
    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(
                        note_data['note_id'],
                        note_data['title'],
                        note_data['body'],
                        note_data['created_at'],
                        note_data['updated_at']
                    )
                    self.notes.append(note)

            print('Заметки успешно загружены')
        except FileNotFoundError:
            print('Файл с заметками не найден. Создан новый файл')

    #  метод поиска заметки по её ID
    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    #  метод для сохранения заметок в файле
    def save_notes(self):
        data = [note.to_dict() for note in self.notes]
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print('Заметки успешно сохранены')

    #  метод для добавления новой заметки
    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note = Note(note_id, title, body, now, now)
        self.notes.append(note)
        print('Заметка успешно добавлена')

    # метод для изменения заголовка заметки
    def edit_note_title(self, note_id, new_title):
        note = self.find_note_by_id(note_id)
        if note:
            note.title = new_title
            note.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('Заголовок заметки успешно изменен ')
        else:
            print('Заметка с указанным ID не найдена ')

    # метод для изменения тела заметки
    def edit_note_body(self, note_id, new_body):
        note = self.find_note_by_id(note_id)
        if note:
            note.body = new_body
            note.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('Тело заметки успешно изменено')
        else:
            print('Заметка с указанным ID не найдена ')

    #  метод удаления заметки
    def delete_note_by_id(self, note_id):
        note = self.find_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            print('Заметка успешно удалена ')
        else:
            print('Заметка с указанным ID не найдена ')

    # метод фильтрации заметок по дате
    def filter_notes_by_date(self, date):
        filtered_notes = []
        for note in self.notes:
            if note.created_at.split()[0] == date or note.updated_at.split()[0] == date:
                filtered_notes.append(note)
        return filtered_notes
