Аналіз результатів

1.	DFS (Пошук в глибину):
•	Алгоритм DFS досліджує якомога глибше кожен шлях перед поверненням і дослідженням альтернативних варіантів. Це означає, що він буде “занурюватися” до кінця графа або до знаходження цільової вершини, що іноді призводить до довших шляхів.
•	Вихідний шлях DFS може відрізнятися за кількістю пройдених вершин, якщо є кілька можливих шляхів.
2.	BFS (Пошук в ширину):
•	BFS проходить граф у ширину, досліджуючи всі сусідні вузли першого рівня, потім вузли другого рівня, і так далі. Це дозволяє знайти найкоротший шлях у графі за кількістю вершин.
•	BFS завжди знайде найкоротший шлях у графі з однаковою вагою для всіх ребер.

Пояснення різниці в шляхах

•	DFS може знайти довший шлях, оскільки йому не обов’язково вибирати найкоротший маршрут: він “занурюється” до першої можливості дістатися кінцевої станції. Тому шлях DFS може містити більше кроків, ніж BFS.
•	BFS завжди знаходить шлях з мінімальною кількістю кроків від початкової до кінцевої станції, оскільки досліджує всі сусідні вершини на кожному рівні перед переходом на наступний.

Таким чином, BFS є оптимальним для задачі знаходження найкоротшого шляху в незважених графах, а DFS може бути корисним для задач, де важливо повністю дослідити всі можливі шляхи або перевірити, чи існує шлях між вузлами.