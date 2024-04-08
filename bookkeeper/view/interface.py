import random
import sys
from bookkeeper.view.date_budget_count import *

from PySide6 import QtWidgets

def row_of_widgets(*widgets):
    hl = QtWidgets.QHBoxLayout()
    for w in widgets:
        hl.addWidget(w)
    return hl


class MyWindow(QtWidgets.QWidget):

    def __init__(self, repo,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repo=repo
        self.expenses=[["2023-01-09 15:09:00","105.99","Хлеб","Черный и свежий"],["2023-01-09 15:09:00","105.99","Хлеб","Черный и свежий"]]
        self.catg=["Хлеб"]
        self.restrictions=[0,0,0]
        try:
            with open("bookkeeper/repository/content/restictions.txt", "r") as f:
                z=f.read().split()
                self.restrictions=[float(z[0]),float(z[1]),float(z[2])]
        except:
            pass

        self.constracte_image()
        self.update()

    def click(self):
        self.label.setText(random.choice(self.greetings))

    def update(self):
        self.expenses=self.repo.list_spend()
        self.catg=self.repo.list_catg()
        #print(self.expenses,self.catg)
        self.table_length=len(self.expenses)
        self.table.setRowCount(self.table_length)
        self.update_image()

    def constracte_image(self):
        self.table_length=len(self.expenses)
        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(self.table_length)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Дата", "Сумма", "Категория", "Комментарий"])
        self.table_buttons_delete=[]
        for i in range(self.table_length):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.expenses[i][0]))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(self.expenses[i][1]))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(self.expenses[i][2]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(self.expenses[i][3]))
            #bt=QtWidgets.QPushButton('Удалить')
            #self.table_buttons_delete.append(bt)
            #self.table.setCellWidget(i, 4, bt)
        #self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)



        self.table_b = QtWidgets.QTableWidget()
        self.table_b.setRowCount(3)
        self.table_b.setColumnCount(3)
        self.table_b.setHorizontalHeaderLabels(["Сумма", "Бюджет", ""])
        self.table_b.setVerticalHeaderLabels(["День", "Неделя", "Месяц"])
        for i in range(3):
                self.table_b.setItem(i, 0, QtWidgets.QTableWidgetItem("0"))
        self.restrict_edit1=QtWidgets.QLineEdit('0')
        self.restrict_edit1.textEdited.connect(self.func_restrict_edit)
        self.restrict_edit2=QtWidgets.QLineEdit('0')
        self.restrict_edit2.textEdited.connect(self.func_restrict_edit)
        self.restrict_edit3=QtWidgets.QLineEdit('0')
        self.restrict_edit3.textEdited.connect(self.func_restrict_edit)
        self.table_b.setCellWidget(0, 1, self.restrict_edit1)
        self.table_b.setCellWidget(1, 1, self.restrict_edit2)
        self.table_b.setCellWidget(2, 1, self.restrict_edit3)
        self.table_b.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        

        self.edit_spent = QtWidgets.QLineEdit("0")
        self.combo_spent = QtWidgets.QComboBox()
        for k in self.catg:
            self.combo_spent.addItem(k)
        self.button_spent_add = QtWidgets.QPushButton('Добавить запись')
        self.button_spent_add.clicked.connect(self.func_button_spent_add)

        self.combo_spentEdit = QtWidgets.QComboBox()
        self.combo_spentEdit.currentIndexChanged.connect(self.func_combo_spentEdit)
        self.edit_spentEditDate = QtWidgets.QLineEdit("")
        self.edit_spentEdit = QtWidgets.QLineEdit("0")
        self.combo_spentEditK = QtWidgets.QComboBox()
        self.edit_spentEditComment = QtWidgets.QLineEdit("")
        for k in self.catg:
            self.combo_spent.addItem(k)
        self.button_spentEdit = QtWidgets.QPushButton('Редактировать запись')
        self.button_spentDelete = QtWidgets.QPushButton('Удалить запись')
        self.button_spentEdit.clicked.connect(self.func_button_spentEdit)
        self.button_spentDelete.clicked.connect(self.func_button_spentDelete)


        self.edit_k = QtWidgets.QLineEdit("Название категории")
        self.combo_k = QtWidgets.QComboBox()
        for k in self.catg:
            self.combo_k.addItem(k)
        self.button_k_delete = QtWidgets.QPushButton('Удалить категорию')
        self.button_k_add = QtWidgets.QPushButton('Добавить категорию')
        self.button_k_delete.clicked.connect(self.func_button_k_delete)
        self.button_k_add.clicked.connect(self.func_button_k_add)
        
        

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(QtWidgets.QLabel("Последние расходы"))
        self.vbox.addWidget(self.table)
        self.vbox.addWidget(QtWidgets.QLabel("Бюджет"))
        self.vbox.addWidget(self.table_b)
        self.vbox.addWidget(QtWidgets.QLabel("Добавить запись о расходах:"))
        self.vbox.addLayout(row_of_widgets(QtWidgets.QLabel("Сумма"), self.edit_spent))
        self.vbox.addLayout(row_of_widgets(QtWidgets.QLabel("Категория"), self.combo_spent))
        self.vbox.addWidget(self.button_spent_add)

        self.vbox.addWidget(QtWidgets.QLabel("   "))
        self.vbox.addWidget(QtWidgets.QLabel("   "))

        self.vbox.addWidget(QtWidgets.QLabel("Редактировать/удалить запись о расходах:"))
        self.vbox.addLayout(row_of_widgets(QtWidgets.QLabel("Выберите статью расхода:"), self.combo_spentEdit))
        self.vbox.addLayout(row_of_widgets(QtWidgets.QLabel("Дата"), self.edit_spentEditDate))
        self.vbox.addLayout(row_of_widgets(QtWidgets.QLabel("Сумма"), self.edit_spentEdit))
        self.vbox.addLayout(row_of_widgets(QtWidgets.QLabel("Категория"), self.combo_spentEditK))
        self.vbox.addLayout(row_of_widgets(QtWidgets.QLabel("Комментарий"), self.edit_spentEditComment))
        self.vbox.addLayout(row_of_widgets(self.button_spentEdit,self.button_spentDelete))

        self.vbox.addWidget(QtWidgets.QLabel("   "))
        self.vbox.addWidget(QtWidgets.QLabel("   "))
        
        self.vbox.addWidget(QtWidgets.QLabel("Редактирование категорий:"))
        self.vbox.addLayout(row_of_widgets(self.edit_k, self.button_k_add))
        self.vbox.addLayout(row_of_widgets(self.combo_k, self.button_k_delete))
        #self.vbox.addWidget(self.edit)
        #self.vbox.addWidget(self.table)
        

        self.setLayout(self.vbox)
        self.setWindowTitle('Управление личными финансами (Бобков)')
        self.resize(600, 800)

        
    def update_image(self):
        for i in range(self.table_length):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.expenses[i][0]))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(self.expenses[i][1]))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(self.expenses[i][2]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(self.expenses[i][3]))

        summ=[0,0,0]
        for sp in self.expenses:
            if date_dif_now(sp[0])[0]:summ[0]+=float(sp[1])
            if date_dif_now(sp[0])[1]:summ[1]+=float(sp[1])
            if date_dif_now(sp[0])[2]:summ[2]+=float(sp[1])
        for i in range(3):
            self.table_b.setItem(i, 0, QtWidgets.QTableWidgetItem(str(summ[i])))
            if summ[i]>self.restrictions[i]:
                self.table_b.setItem(i, 2, QtWidgets.QTableWidgetItem("ПРЕВЫШЕНИЕ!"))
            else:
                self.table_b.setItem(i, 2, QtWidgets.QTableWidgetItem(""))
        self.restrict_edit1.setText(str(self.restrictions[0]))
        self.restrict_edit2.setText(str(self.restrictions[1]))
        self.restrict_edit3.setText(str(self.restrictions[2]))

        N=self.combo_spent.count()
        for k in range(N):
            self.combo_spent.removeItem(0)
        for k in self.catg:
            self.combo_spent.addItem(k)

        N=self.combo_spentEdit.count()
        for k in range(N):
            self.combo_spentEdit.removeItem(0)
        for k in self.expenses:
            self.combo_spentEdit.addItem("Дата: "+str(k[0])+", сумма: "+str(k[1]))

        N=self.combo_spentEditK.count()
        for k in range(N):
            self.combo_spentEditK.removeItem(0)
        for k in self.catg:
            self.combo_spentEditK.addItem(k)

        N=self.combo_k.count()
        for k in range(N):
            self.combo_k.removeItem(0)
        for k in self.catg:
            self.combo_k.addItem(k)

    def func_button_spent_add(self):
        self.repo.add(float(self.edit_spent.text()), self.combo_spent.currentText(), '-')
        self.edit_spent.setText('0')
        self.update()

    def func_button_k_delete(self):
        self.repo.delete_ctg(self.repo.pk_catg()[str(self.combo_k.currentIndex())])
        self.update()
        #print(self.repo.pk_spend())
        #print(self.repo.pk_catg())

    def func_button_k_add(self):
        self.repo.add_catg(self.edit_k.text())
        self.edit_k.setText('Название категории')
        self.update()

    def func_button_spentEdit(self):
        self.repo.update(self.repo.pk_spend()[str(self.combo_spentEdit.currentIndex())], self.edit_spentEditDate.text(), self.edit_spentEdit.text(), self.combo_spentEditK.currentText(), self.edit_spentEditComment.text())
        self.update()

    def func_button_spentDelete(self):
        self.repo.delete(self.repo.pk_spend()[str(self.combo_spentEdit.currentIndex())])
        self.update()

    def func_combo_spentEdit(self):
        z=self.repo.list_spend()[self.combo_spentEdit.currentIndex()]
        self.edit_spentEditDate.setText(z[0])
        self.edit_spentEdit.setText(z[1])
        self.combo_spentEditK.setCurrentIndex(self.combo_spentEditK.findText(z[2]))
        self.edit_spentEditComment.setText(z[3])

    def func_restrict_edit(self):
        self.restrictions[0]=float(self.restrict_edit1.text())
        self.restrictions[1]=float(self.restrict_edit2.text())
        self.restrictions[2]=float(self.restrict_edit3.text())
        with open("bookkeeper/repository/content/restictions.txt", "w") as f:
            f.write(str(self.restrictions[0])+" "+str(self.restrictions[1])+" "+str(self.restrictions[2]))
        self.update()

    


#app = QtWidgets.QApplication(sys.argv)
#window = MyWindow()
#window.setWindowTitle('Управление личными финансами (Бобков)')
#window.resize(600, 800)
#window.show()
#sys.exit(app.exec())
