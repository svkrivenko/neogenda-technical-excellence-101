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


def test_has_subheader_3_4(text):
    assert '### 3.4 Медведь' in text


def test_final_not_empty(text):
    final_header = '## 4. Финал. Встреча с Лисой-колбасой'
    assert final_header in text
    final_part = text.split(final_header, 1)[1].strip()
    assert final_part and final_part != '...'