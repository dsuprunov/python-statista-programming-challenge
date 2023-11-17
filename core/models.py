from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Unit(Base):
    __tablename__ = 'unit'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    age: Mapped[int | None]
    final_weight: Mapped[int | None]
    capital_gain: Mapped[int | None]
    capital_loss: Mapped[int | None]
    hours_per_week: Mapped[int | None]

    working_class_id: Mapped[int | None] = mapped_column(ForeignKey('working_class.id'))
    working_class: Mapped[WorkingClass | None] = relationship(back_populates='parents')

    education_id: Mapped[int | None] = mapped_column(ForeignKey('education.id'))
    education: Mapped[Education | None] = relationship(back_populates='parents')

    marital_status_id: Mapped[int | None] = mapped_column(ForeignKey('marital_status.id'))
    marital_status: Mapped[MaritalStatus | None] = relationship(back_populates='parents')

    occupation_id: Mapped[int | None] = mapped_column(ForeignKey('occupation.id'))
    occupation: Mapped[Occupation | None] = relationship(back_populates='parents')

    family_relationship_id: Mapped[int | None] = mapped_column(ForeignKey('family_relationship.id'))
    family_relationship: Mapped[FamilyRelationship | None] = relationship(back_populates='parents')

    race_id: Mapped[int | None] = mapped_column(ForeignKey('race.id'))
    race: Mapped[Race | None] = relationship(back_populates='parents')

    gender_id: Mapped[int | None] = mapped_column(ForeignKey('gender.id'))
    gender: Mapped[Gender | None] = relationship(back_populates='parents')

    native_country_id: Mapped[int | None] = mapped_column(ForeignKey('country.id'))
    native_country: Mapped[Country | None] = relationship(back_populates='parents')

    income_id: Mapped[int | None] = mapped_column(ForeignKey('income.id'))
    income: Mapped[Income | None] = relationship(back_populates='parents')

    def __str__(self) -> str:
        return (f'Unit('
                f'{self.age!r}, '
                f'{self.working_class!r}, '
                f'{self.final_weight!r}, '
                f'{self.education!r}, '
                f'{self.marital_status!r}, '
                f'{self.occupation!r}, '
                f'{self.family_relationship!r}, '
                f'{self.race!r}, '
                f'{self.gender!r}, '
                f'{self.capital_gain!r}, '
                f'{self.capital_loss!r}, '
                f'{self.hours_per_week!r}, '
                f'{self.native_country!r}, '
                f'{self.income!r}'
                ')')

    def __repr__(self) -> str:
        return str(self)


class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    country: Mapped[str] = mapped_column(unique=True)

    parents: Mapped[list[Unit]] = relationship(
        back_populates='native_country',
        cascade='all, delete-orphan'
    )

    def __str__(self) -> str:
        return f'Country({self.id}, {self.country!r})'

    def __repr__(self) -> str:
        return str(self)


class Education(Base):
    __tablename__ = 'education'
    __table_args__ = (
        UniqueConstraint('education', 'years'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    education: Mapped[str] = mapped_column(unique=True)
    years: Mapped[int] = mapped_column(unique=True)

    parents: Mapped[list[Unit]] = relationship(
        back_populates='education',
        cascade='all, delete-orphan'
    )

    def __str__(self) -> str:
        return f'Education({self.id}, {self.education!r}, {self.years!r})'

    def __repr__(self) -> str:
        return str(self)


class FamilyRelationship(Base):
    __tablename__ = 'family_relationship'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    family_relationship: Mapped[str] = mapped_column(unique=True)

    parents: Mapped[list[Unit]] = relationship(
        back_populates='family_relationship',
        cascade='all, delete-orphan'
    )

    def __str__(self) -> str:
        return f'FamilyRelationship({self.id}, {self.family_relationship!r})'

    def __repr__(self) -> str:
        return str(self)


class Gender(Base):
    __tablename__ = 'gender'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    gender: Mapped[str] = mapped_column(unique=True)

    parents: Mapped[list[Unit]] = relationship(
        back_populates='gender',
        cascade='all, delete-orphan'
    )

    def __str__(self) -> str:
        return f'Gender({self.id}, {self.gender!r})'

    def __repr__(self) -> str:
        return str(self)


class Income(Base):
    __tablename__ = 'income'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    income: Mapped[str] = mapped_column(unique=True)

    parents: Mapped[list[Unit]] = relationship(
        back_populates='income',
        cascade='all, delete-orphan'
    )

    def __str__(self) -> str:
        return f'Income({self.id}, {self.income!r})'

    def __repr__(self) -> str:
        return str(self)


class MaritalStatus(Base):
    __tablename__ = 'marital_status'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    marital_status: Mapped[str] = mapped_column(unique=True)

    parents: Mapped[list[Unit]] = relationship(
        back_populates='marital_status',
        cascade='all, delete-orphan'
    )

    def __str__(self) -> str:
        return f'MaritalStatus({self.id}, {self.marital_status!r})'

    def __repr__(self) -> str:
        return str(self)


class Occupation(Base):
    __tablename__ = 'occupation'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    occupation: Mapped[str] = mapped_column(unique=True)

    parents: Mapped[list[Unit]] = relationship(
        back_populates='occupation',
        cascade='all, delete-orphan'
    )

    def __str__(self) -> str:
        return f'Occupation({self.id}, {self.occupation!r})'

    def __repr__(self) -> str:
        return str(self)


class Race(Base):
    __tablename__ = 'race'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    race: Mapped[str] = mapped_column(unique=True)

    parents: Mapped[list[Unit]] = relationship(
        back_populates='race',
        cascade='all, delete-orphan'
    )

    def __str__(self) -> str:
        return f'Race({self.id}, {self.race!r})'

    def __repr__(self) -> str:
        return str(self)


class WorkingClass(Base):
    __tablename__ = 'working_class'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    working_class: Mapped[str] = mapped_column(unique=True)

    parents: Mapped[list[Unit]] = relationship(
        back_populates='working_class',
        cascade='all, delete-orphan'
    )

    def __str__(self) -> str:
        return f'WorkingClass({self.id}, {self.working_class!r})'

    def __repr__(self) -> str:
        return str(self)
