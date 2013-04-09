import datetime

import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class TimestampMixin(object):
    last_update = sa.Column(sa.TIMESTAMP,
                            nullable=False,
                            default=datetime.datetime.now())


class FilmActor(TimestampMixin, Base):
    __tablename__ = 'film_actor'
    actor_id = sa.Column(sa.SmallInteger(unsigned=True),
                         sa.ForeignKey("actor.actor_id"),
                         nullable=False,
                         primary_key=True)
    film_id = sa.Column(sa.SmallInteger(unsigned=True),
                        sa.ForeignKey("film.film_id"),
                        nullable=False,
                        primary_key=True)


class Film(TimestampMixin, Base):
    __tablename__ = 'film'
    film_id = sa.Column(sa.SmallInteger(unsigned=True),
                        nullable=False,
                        primary_key=True)
    title = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text)
    release_year = sa.Column(mysql.YEAR)
    language_id = sa.Column(mysql.TINYINT(unsigned=True),
                            sa.ForeignKey("language.language_id"),
                            nullable=False)
    original_language_id = sa.Column(mysql.TINYINT(unsigned=True),
                                     sa.ForeignKey("language.language_id"))
    rental_duration = sa.Column(sa.SmallInteger(unsigned=True),
                                default=3)
    rental_rate = sa.Column(sa.Numeric(scale=(4, 2), asdecimal=True),
                            nullable=False,
                            default=4.99)
    length = sa.Column(sa.SmallInteger(unsigned=True),
                       nullable=True)
    replacement_cost = sa.Column(sa.Numeric(scale=(5, 2), asdecimal=True),
                                 nullable=True,
                                 default=19.99)
    rating = sa.Column(sa.Enum('G','PG','PG-13','R','NC-17'),
                       nullable=True,
                       default='G')
    special_features = sa.Column(mysql.SET('Trailers',
                                           'Commentaries',
                                           'Deleted Scenes',
                                           'Behind the Scenes'))

    actors = relationship('FilmActor')
    language = relationship(
        'Language',
        primaryjoin="Film.language_id==Language.language_id")
    original_language = relationship(
        'Language',
        primaryjoin="Film.original_language_id==Language.language_id")
    categories = relationship('FilmCategory')

    __table_args__ = (sa.UniqueConstraint('title', 'language_id', 'original_language_id'),
                     )


class Actor(TimestampMixin, Base):
    __tablename__ = 'actor'
    actor_id = sa.Column(sa.SmallInteger(unsigned=True), nullable=False,
                         primary_key=True)
    first_name = sa.Column(sa.String(45), nullable=False)
    last_name = sa.Column(sa.String(45), nullable=False)


class Language(TimestampMixin, Base):
    __tablename__ = 'language'
    language_id = sa.Column(mysql.TINYINT(unsigned=True),
                            nullable=False,
                            primary_key=True)
    name = sa.Column(mysql.CHAR(20),
                     nullable=False)


class FilmCategory(TimestampMixin, Base):
    __tablename__ = 'film_category'
    film_id = sa.Column(sa.SmallInteger(unsigned=True),
                        sa.ForeignKey("film.film_id"),
                        nullable=False,
                        primary_key=True)
    category_id = sa.Column(mysql.TINYINT(unsigned=True),
                            sa.ForeignKey("category.category_id"),
                            nullable=False,
                            primary_key=True)


class Category(TimestampMixin, Base):
    __tablename__ = 'category'
    category_id = sa.Column(mysql.TINYINT(unsigned=True),
                            nullable=False,
                            primary_key=True)
    name = sa.Column(sa.String(25),
                     nullable=False)


class Inventory(TimestampMixin, Base):
    __tablename__ = 'inventory'
    inventory_id = sa.Column(mysql.MEDIUMINT(unsigned=True),
                             nullable=False,
                             primary_key=True)
    film_id = sa.Column(sa.SmallInteger(unsigned=True),
                        sa.ForeignKey('film.film_id'),
                        nullable=False)

    film = relationship('Film')


class Rental(TimestampMixin, Base):
    __tablename__ = 'rental'
    rental_id = sa.Column(sa.Integer,
                          nullable=False,
                          primary_key=True)
    rental_date = sa.Column(sa.DateTime,
                            nullable=False)
    inventory_id = sa.Column(mysql.MEDIUMINT(unsigned=True),
                             sa.ForeignKey('inventory.inventory_id'),
                             nullable=True)
    return_date = sa.Column(sa.DateTime)

    inventory = relationship('Inventory')

    __table_args__ = (sa.UniqueConstraint('rental_date', 'inventory_id'),)


class Payment(TimestampMixin, Base):
    __tablename__ = 'payment'
    payment_id = sa.Column(sa.SmallInteger(unsigned=True),
                           nullable=True,
                           primary_key=True)
    rental_id = sa.Column(sa.Integer,
                          sa.ForeignKey('rental.rental_id'))
    amount = sa.Column(sa.Numeric(scale=(4, 2), asdecimal=True),
                       nullable=False)
    payment_date = sa.Column(sa.DateTime,
                             nullable=False)

    rental = relationship('Rental')
