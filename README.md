# Завдання

Вам потрібно розробити алгоритм програми, яка повинна виконувати наступне:
- програма приймає на вхід довільний текст і знаходить в кожному слові цього тексту найперший символ, який більше НЕ повторюється в аналізуємому слові
- далі із отриманого набору символів програма повинна вибрати перший унікальний (тобто той, який більше не зустручається в наборі) і повернути його.

Наприклад, якщо програма отримує на вхід текст нижче:

The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"

то повинна повернути вона символ "m".

# Використання програми обробки тексту

Файл text_process.py - це скріп написаний для обробки тексту. Він обробляє текст надрукоаний у файлі або переданий як аргумент.

Приклад використання для читання з файлу.
```console
python text_process.py -f <path to file with text>
```

Приклад використання з переданим текстом як параметром.
```console
python text_process.py -t "text begin ... text end"
```




   