# artificial-intelligence

## Установка
Зависимости: я использовал Miniconda для Linux (http://conda.pydata.org/miniconda.html), Python 2.7
1. Клонировать репозиторий `git clone https://github.com/curious22/artificial-intelligence.git`
2. Переходим в папку artificial-intelligence
3. Запустить скрипт `bash run.sh` или:
* `conda env create -f environment.yml` - установка виртуального окружения
* `source activate py2AI` - запуст виртуального окружения

Запускать программы можно скриптами main.py из папок /lab*/gui/

## Лабораторная работа 1
Реализовать методы слепого (полного) перебора:
* поиска вширь (breadth_first_search)
* поиска в глубину (depth_first_search)

## Лабораторная работа 2
1. Реализовать просчет весов нейронов по формулам и сделать отрисовку нейронной сети
2. Реализация нейронной сети с обратным распространением ошибки
