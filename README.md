# task_misis
 #Программа на вход получает
 - химическую реакцию с правильными обозначениями(типа SiO2, Ab2Cd5, 5AbC)
 - коэффициенты уравнения уже должны быть проставлены.(типа CH4+2O2=CO2+H2O)
 - концентрации реагентов в некоторой размерности. Если выбран флаг "стехиометрическая смесь" , автоматически выставяляются молярности равные коэффициентам уравнения.
 - агрегатное состояние реагента(CO2(Gas) и т.д.)
 #Опциональные поля:
 - Энергия активации
 - Температура
 - Начальные концентрации
 - Время полного протекания
 - Порядок реакции
 - Скорость реакции при какой то температуре и концентрации
 - Время полупревращения
 - Константа скорости
 - Ввод таблицы с концентрациями во времени.
 #По этим данным:
 - программа выводит на экран саму реакцию с подписями (как решение задачи)
 - выводятся термодинамические данные, которые программа берет из своей термодинамической базы
 - определяется направление протекания реакции
 - определяется константа скорости реакции.
 - приводятся значения z
 - под уравнением прописывается формула для нахождения концентрации через z
 -  если возможно, определяется эдс реакции.
 - Исходя из опцинальных полей выполняются дополнительные рассчеты(добавить меню с вызовом рассчетов)
#Дополнение:
- Построение графиков концентрации от времени.
- Нахождение порядка реакции каким-то методом.
- Нахождение времени полупревращение при помощи интерполяции.
- Нахождение скорости реакции
- Нахождение Энергии активации
- Нахождение предэкспоненциального мноджителя для константы скорости реакции.
- и т.д.
#Модули:
- ввода данных.
- рассчетов.
- работы с базой данных.
- работы с математическими выражениями.
- работа с графиками.
