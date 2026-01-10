# -*- coding: utf-8 -*-

import os
import pytest


@pytest.fixture()
def change_test_dir(request):
    os.chdir(request.fspath.dirname)
    yield
    os.chdir(request.config.invocation_dir)


@pytest.fixture()
def text(change_test_dir):
    with open('./Kolobok.md', mode='r', encoding="utf-8") as output_file:
        return output_file.read()


def test_has_header(text):
    assert '# Сказка про колобка' in text

def test_has_subheader_3_2(text):
    assert '### 3.2 Волк' in text

def test_has_subheader_3_3(text):
    assert '### 3.3 Свин' in text

def test_has_subheader_3_4(text):
    assert '### 3.4 Медведь' in text

def test_has_subheader_3_5(text):
    assert '### 3.5 Лиса' in text

def test_subheaders_order_is_correct(text):
    order = [
        '### 3.1 Заяц',
        '### 3.2 Собака серая',
        '### 3.3 Свин',
        '### 3.4 Медведь',
        '### 3.5 Лиса',
    ]
    positions = []
    for marker in order:
        pos = text.find(marker)
        assert pos != -1, f'Не найден заголовок: {marker}'
        positions.append(pos)
    assert positions == sorted(positions), 'Заголовки 3.x идут в неверном порядке'
