import pytest

from core.models import Base
from core.models import Unit
from core.models import Country
from core.models import Education
from core.models import FamilyRelationship
from core.models import Gender
from core.models import Income
from core.models import MaritalStatus
from core.models import Occupation
from core.models import Race
from core.models import WorkingClass


def test_base():
    base = Base()
    assert isinstance(base, Base)


def test_unit():
    unit = Unit()
    assert isinstance(unit, Unit)


def test_country():
    country = Country()
    assert isinstance(country, Country)


def test_education():
    education = Education()
    assert isinstance(education, Education)


def test_family_relationship():
    family_relationship = FamilyRelationship()
    assert isinstance(family_relationship, FamilyRelationship)


def test_gender():
    gender = Gender()
    assert isinstance(gender, Gender)


def test_income():
    income = Income()
    assert isinstance(income, Income)


def test_marital_status():
    marital_status = MaritalStatus()
    assert isinstance(marital_status, MaritalStatus)


def test_occupation():
    occupation = Occupation()
    assert isinstance(occupation, Occupation)


def test_race():
    race = Race()
    assert isinstance(race, Race)


def test_working_class():
    working_class = WorkingClass()
    assert isinstance(working_class, WorkingClass)
