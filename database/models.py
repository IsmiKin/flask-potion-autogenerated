from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Index, Integer, String, Table, text
from sqlalchemy.dialects.mysql.base import MEDIUMBLOB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import db

Base = declarative_base()
metadata = Base.metadata


class Button(Base):
    __tablename__ = 'Button'

    id = Column(Integer, primary_key=True)
    name = Column(String(45, 'latin1_spanish_ci'))
    description = Column(String(200, 'latin1_spanish_ci'))
    image = Column(MEDIUMBLOB)
    imagetype = Column(String(45, 'latin1_spanish_ci'))
    imagepath = Column(String(255, 'latin1_spanish_ci'))
    file = Column(Integer, server_default=text("'0'"))
    url = Column(String(255, 'latin1_spanish_ci'))
    active = Column(Integer)
    buttontype = Column(Integer, server_default=text("'0'"))
    Campaign_id = Column(Integer, nullable=False)
    Campaign_Category_id = Column(Integer, index=True)


class Campaign(db.Model):
    __tablename__ = 'Campaign'

    id = db.Column(Integer, primary_key=True)
    adservercampid = db.Column(Integer)
    campname = db.Column(String(45))
    description = db.Column(String(255))
    url = db.Column(String(255))
    imageicon = db.Column(String(255))
    imagecarrusel = db.Column(String(255))
    email = db.Column(String(75))
    zoneid = db.Column(Integer, nullable=False)
    category_name = db.Column(String(45))
    zone_name = db.Column(String(45))
    template = db.Column(String(255))
    client = db.Column(Integer, nullable=False, server_default=text("'0'"))
    Category_id = db.Column(Integer, nullable=False, index=True)


class Category(Base):
    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50, 'latin1_spanish_ci'), nullable=False)
    description = Column(String(145, 'latin1_spanish_ci'))


class Client(Base):
    __tablename__ = 'Client'

    id = Column(Integer, primary_key=True)
    name = Column(String(45, 'latin1_spanish_ci'))
    url = Column(String(255, 'latin1_spanish_ci'))
    description = Column(String(255, 'latin1_spanish_ci'))
    location = Column(String(45, 'latin1_spanish_ci'))
    address = Column(String(45, 'latin1_spanish_ci'))
    gpslong = Column(String(45, 'latin1_spanish_ci'))
    gpslat = Column(String(45, 'latin1_spanish_ci'))
    cp = Column(Integer)
    province = Column(String(45, 'latin1_spanish_ci'))
    country = Column(String(45, 'latin1_spanish_ci'))
    city = Column(String(45, 'latin1_spanish_ci'))
    email = Column(String(145, 'latin1_spanish_ci'))
    woeid = Column(Integer)
    Campaign_id = Column(Integer, index=True)
    usuario_acceso = Column(Integer)


class Log(Base):
    __tablename__ = 'Log'

    id = Column(Integer, primary_key=True)
    message = Column(String(360, 'latin1_spanish_ci'))
    timestamp = Column(DateTime)
    Terminal_id = Column(ForeignKey('Terminal.id'), index=True)

    Terminal = relationship('Terminal')


class Statistic(Base):
    __tablename__ = 'Statistics'

    id = Column(Integer, primary_key=True)
    clicks = Column(BigInteger)
    datetime = Column(DateTime)
    Terminal_id = Column(Integer, index=True)
    Campaign_id = Column(Integer, index=True)


class Template(Base):
    __tablename__ = 'Template'

    id = Column(Integer, primary_key=True)
    name = Column(String(45, 'latin1_spanish_ci'))
    description = Column(String(45, 'latin1_spanish_ci'))
    path = Column(String(255, 'latin1_spanish_ci'))


class Terminal(Base):
    __tablename__ = 'Terminal'

    id = Column(Integer, primary_key=True, unique=True)
    terminalname = Column(String(45, 'latin1_spanish_ci'))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    statustime = Column(DateTime)
    updatetime = Column(Integer, server_default=text("'65'"))
    ip = Column(String(45, 'latin1_spanish_ci'), server_default=text("'0'"))
    macwlan = Column(String(45, 'latin1_spanish_ci'))
    notas = Column(String(245, 'latin1_spanish_ci'))
    needupdate = Column(Integer, server_default=text("'0'"))
    updatedb = Column(Integer, server_default=text("'0'"))
    Client_id = Column(Integer)


class Zone(Base):
    __tablename__ = 'Zone'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, 'latin1_spanish_ci'), nullable=False)
    adserverzone_id = Column(Integer, nullable=False)
    Terminal_id = Column(Integer, index=True)
    active = Column(Integer, server_default=text("'1'"))
    province = Column(String(45, 'latin1_spanish_ci'))
    country = Column(String(45, 'latin1_spanish_ci'))


t_Zone_has_Campaign = Table(
    'Zone_has_Campaign', metadata,
    Column('Zone_id', Integer, index=True),
    Column('Campaign_id', Integer),
    Column('Campaign_Category_id', Integer),
    Index('fk_Zone_has_Campaign_Campaign1_idx', 'Campaign_id', 'Campaign_Category_id')
)
