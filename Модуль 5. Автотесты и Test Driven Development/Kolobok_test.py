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


def test_has_subheader_медведь(text):
    assert '### 3.4 Медведь' in text


def test_есть_глава_про_волка(text):
    assert '### 3.2 Волк' in text


def test_нет_собаки_серой(text):
    assert 'Собака серая' not in text