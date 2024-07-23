# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. 
# Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
# Наприклад:
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню
# суму заробітної плати всіх розробників.

def total_salary(path: str):
    try:
        with open(path, 'r', encoding='UTF-8') as fh:
            lines = fh.readlines()
            total_sum = 0
            for line in lines:
                elements = line.split(',')
                total_sum = total_sum + float(elements[1]) # Get salary from line and convert it to float
            
            avg_salary = total_sum / len(lines) # Calculate average salary
            return total_sum, avg_salary
    except FileNotFoundError as e:
        print("Please input correct way to file", e)

        
total, average = total_salary('task1/task1.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")