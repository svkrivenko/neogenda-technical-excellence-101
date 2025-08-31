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
    assert '### 3.2 Серый Волк' in text

def test_has_subheader_3_4(text):
    assert '### 3.4 Медведь' in text

def test_no_zaec_word_any_case(text):
    assert 'ЗАЕЦ' not in text.upper()

def test_no_kolovbok_word(text):
    assert 'коловбок' not in text.lower()

def test_no_medved_word(text):
    assert 'Медвед-' not in text
