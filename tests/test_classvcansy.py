# -*- coding: utf-8 -*-
import pytest
from src.class_vcacansy import Vacancy

@pytest.fixture
def example_vacancy():
    return Vacancy(
        name='Software Engineer',
        url='https://example.com',
        city='Moscow',
        salary_from=100000,
        salary_to=150000,
        currency='RUB',
        requirements='3+ years of experience in Python'
    )

def test_vacancy_str(example_vacancy):
    expected_output = ("Название вакансии: Software Engineer\n"
                       "Ссылка: https://example.com\n"
                       "Город: Moscow\n"
                       "Зарплата: 100000-150000 RUB.\n"
                       "Требования: 3+ years of experience in Python\n"
                       "---")
    assert str(example_vacancy) == expected_output

def test_vacancy_eq(example_vacancy):
    other_vacancy = Vacancy(
        name='Frontend Developer',
        url='https://example.com',
        city='Moscow',
        salary_from=100000,
        salary_to=150000,
        currency='RUB',
        requirements='3+ years of experience in React'
    )
    assert example_vacancy == other_vacancy

def test_vacancy_lt(example_vacancy):
    higher_salary_vacancy = Vacancy(
        name='Senior Developer',
        url='https://example.com',
        city='Moscow',
        salary_from=200000,
        salary_to=250000,
        currency='RUB',
        requirements='5+ years of experience in Python'
    )
    assert example_vacancy < higher_salary_vacancy

def test_vacancy_gt(example_vacancy):
    lower_salary_vacancy = Vacancy(
        name='Junior Developer',
        url='https://example.com',
        city='Moscow',
        salary_from=50000,
        salary_to=80000,
        currency='RUB',
        requirements='1+ years of experience in Python'
    )
    assert example_vacancy > lower_salary_vacancy
