# У вас є текстовий файл, який містить інформацію про котів. 
# Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.  
# Наприклад:
# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5
# Ваше завдання - розробити функцію get_cats_info(path), 
# яка читає цей файл та повертає список словників з інформацією про кожного кота.


def get_cats_info(path: str):
    try:
        cats = list()
        with open(path, 'r', encoding='UTF-8') as fh:
            lines = fh.readlines()
            for line in lines:
                columns = line.split(',') 
                cat_info = dict(id = columns[0], name = columns[1], age = columns[2].replace('\n',''))
                cats.append(cat_info)
        return cats
    except FileNotFoundError as e:
        print("Please input correct way to file", e)
        
        
cats = get_cats_info('task2/task2.txt')
for cat in cats:
    print(cat)
        