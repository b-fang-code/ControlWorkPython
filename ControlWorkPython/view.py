from notes import Notes

notes = Notes('notes.json')
notes.load_notes()


def start():
    while True:
        print()
        print('ЗАМЕТКИ ')
        print('1. Посмотреть список заметок ')
        print('2. Добавить заметку ')
        print('3. Редактировать заметку ')
        print('4. Удалить заметку ')
        print('5. Фильтровать заметки по дате ')
        print('6. Сохранить и выйти ')
        print()
        choice = input('Введите номер действия: ')

        if choice == '1':
            for note in notes.notes:
                print(f'ID: {note.note_id}, Заголовок:  {note.title}, Тело: {note.body}, Создано: {note.created_at},'
                      f' Обновлено: {note.updated_at} ')
        elif choice == '2':
            title = input('Ведите заголовок заметки: ')
            body = input('Введите тело заметки ')
            notes.add_note(title, body)
        elif choice == '3':
            note_id = int(input('Введите ID заметки, которую хотите отредактировать: '))
            new_title = input('Введите новый заголовок: ')
            new_body = input('Введите новое тело: ')
            notes.edit_note_title(note_id, new_title)
            notes.edit_note_body(note_id, new_body)
        elif choice == '4':
            note_id = int(input('Введите ID заметки, которую хотите удалить: '))
            notes.delete_note_by_id(note_id)
        elif choice == '5':
            date = input('Введите дату (гггг-мм-дд: ')
            filtered_notes = notes.filter_notes_by_date(date)
            for note in filtered_notes:
                print(f'ID: {note.note_id}, Заголовок: {note.title}, Тело: {note.body}, Создано: {note.created_at},'
                      f' Обновлено: {note.updated_at} ')
        elif choice == '6':
            notes.save_notes()
            print('Всего хорошего!')
            break
