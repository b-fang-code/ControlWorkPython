class Note:
    # Конструктор, класса Note, для инициализации свойств каждой заметки
    def __init__(self, note_id, title, body, created_at, updated_at):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at

    # метод, преобразующий объект заметки в словарь
    def to_dict(self):
        return {
            'note_id': self.note_id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
