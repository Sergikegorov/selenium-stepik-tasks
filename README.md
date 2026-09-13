# Selenium WebDriver — практические задания (Stepik)

Репозиторий с решениями заданий курса по Selenium WebDriver на Python.
Каждый скрипт решает отдельную задачу: поиск элементов, работа с формами,
alert, вкладками, ожиданиями и загрузкой файлов.

lesson6_step4.py	Поиск элементов с помощью Selenium	By.TAG_NAME, By.NAME, By.CLASS_NAME, By.ID, By.CSS_SELECTOR   
lesson6_step6.py	Поиск элемента по тексту ссылки	By.LINK_TEXT, math   
lesson6_step6_6.py	Использование find_elements	find_elements, цикл по 100 полям   
lesson6_step7.py	Поиск элемента по XPath	By.XPATH, //button[text()='Submit']   
import_math1.py	Капча для роботов	.text, calc(x), checkbox, radiobutton   
import_math2.py	Сокровище через get_attribute	get_attribute("valuex")   
import_math3.py	Выпадающий список	Select, select_by_value   
import_math4.py	execute_script и прокрутка	scrollIntoView, перекрытый футер   
import_math5.py	Загрузка файла	input[type='file'], send_keys(path), os.path   
import_math6.py	Принимаем alert	switch_to.alert, .accept()   
import_math7.py	Переход на новую вкладку	window_handles, switch_to.window   
import_math8.py	Явные ожидания	WebDriverWait, text_to_be_present_in_element   
registration1_2.py	Уникальность селекторов (рабочая страница)	Уникальные CSS-селекторы   
registration2_1.py	Уникальность селекторов (страница с багом)	Падение с NoSuchElementException   
generate_tests.py	Генерация тестов (allpairs)	Попарное тестирование   

## Требования

- Python 3.8+
- Google Chrome (или Chromium)
- Selenium 4.x
## Замечания
Файлы registration1_2.py и registration2_1.py — пример задачи
«уникальность селекторов»: тест должен проходить на registration1.html
и падать с NoSuchElementException на registration2.html.

## Установка зависимостей:

```bash
pip install selenium

# Run 

python lesson6_step4.py
