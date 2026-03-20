.PHONY: test setup build html open clean

# Установка зависимостей — делается ОДИН РАЗ, ДО сборки
setup:
	pip3 install --upgrade pip
	pip3 install markdown2 pytest flake8

# Очистка
clean:
	rm -rf ./build/

# Сборка HTML — зависит от setup (если нужно)
html:
	mkdir -p ./build
	python3 -m markdown2 Kolobok.md > ./build/Kolobok.html

# Создание директории и сборка
build: html

# Открытие в браузере
open: build
	open ./build/Kolobok.html

# Тесты — зависят от setup, но не от build
test: setup build
	python3 -m pytest

