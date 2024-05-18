grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
res=[sum(row) / len(row) for row in grades] # Считаем среднее для кажджой строки матрицы
students=sorted(students) #Сортируем в алфавитном порядке студентов
point_=dict(zip(students,res)) #объедениям и формируем словарь
print(point_)