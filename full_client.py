from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.repository.sqlite_repository import SQLRepository
from bookkeeper.utils import read_tree
from bookkeeper.view.interface import MyWindow
from PySide6 import QtWidgets
import sys

repo = SQLRepository[Category]()

##cats = '''
##продукты
##    мясо
##        сырое мясо
##        мясные продукты
##    сладости
##книги
##одежда
##'''.splitlines()

#Category.create_from_tree(read_tree(cats), cat_repo)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow(repo)
window.update()

window.show()
sys.exit(app.exec())

        
