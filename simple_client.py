from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.repository.sqlite_repository import SQLRepository
from bookkeeper.utils import read_tree

repo = SQLRepository[Category]()
print(repo.list_spend())
print(repo.list_catg())

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

while True:
    try:
        cmd = input('$> ')
    except EOFError:
        break
    if not cmd:
        continue
    if cmd == 'list_ctg':
        #print(*cat_repo.get_all(), sep='\n')
        repo.show_catg()
    elif cmd == 'list_expense':
        #print(*exp_repo.get_all(), sep='\n')
        repo.show_spend()
    elif cmd == 'delete_first_expense':
        repo.delete(1)
    elif cmd == 'delete_first_ctg':
        repo.delete_ctg(1)
    elif cmd[0].isdecimal():
        amount, name, comment = cmd.split(maxsplit=2)
        #try:
        #    cat = cat_repo.get_all({'name': name})[0]
        #except IndexError:
        #    print(f'категория {name} не найдена')
        #    continue
        #exp = Expense(int(amount), cat.pk)
        repo.add(float(amount), name, comment)
        print("add expense: ",float(amount), name, comment)
    else:
        repo.add_catg(cmd)
        print("add category: ",cmd)



        
