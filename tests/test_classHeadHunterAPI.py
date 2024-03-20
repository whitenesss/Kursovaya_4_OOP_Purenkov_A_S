# -*- coding: utf-8 -*-
import pytest
from src.class_HeadHunterAPI import HeadHunterAPI
from unittest.mock import patch


def test_get_params():
    hh_api = HeadHunterAPI()
    params = hh_api.get_params('python', '1')
    assert params == {
        'text': 'python',
        'area': '1',
        'per_page': 30,
        'order_by': 'relevance'
    }


@patch('builtins.input', side_effect=['Сортировка по релевантности'])
def test_input_set(mock_input):
    hh_api = HeadHunterAPI()
    hh_api.input_set()
    assert hh_api.order_by == 'relevance'


@patch('requests.get')
def test_requests_get(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'items': []}
    hh_api = HeadHunterAPI()
    with patch('builtins.input', side_effect=['python', 'москва']):
        result = hh_api.requests_get
    assert result == {'items': []}
