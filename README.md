# web_map

Користувач вказує для фільмів якого року він бажає побудувати карту та свою локацію як широту (latitude) та довготу (longitude) (e.g. 49.83826,24.02324), і як результат отримує HTML файл. На веб-карті зображується інформація про місця де знімалися фільми, які були зняті того чи іншого року.


### Передумови

Необхідно встановити бібліотеки folium, pandas та geopy. 
```
pip install folium
```
```
pip install pandas
```
```
pip install geopy
```

### Структура html файлу



### Приклад запуску введення та скріншот згенерованої мапи
```
>>> python main.py
Please enter a year you would like to have a map for: 2000
Please enter your location (format: lat, long): 49.83826, 24.02324
Map is generating...
Please wait...
Finished. Please have look on the map 2000_movies_map.html
```

### Висновок

## Автори

* **Дар'я Омелькіна**
