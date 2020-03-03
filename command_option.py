import sys
from notebook import Note, Notebook
from menu import Menu

if __name__ == '__main__':
    print(dir(Note))
    print(dir(Notebook))
    print(dir(Menu))

    notebook = Notebook()
    notebook.new_note('Hello everyone')
    print(isinstance(notebook.notes, list))
    print(str(notebook))
