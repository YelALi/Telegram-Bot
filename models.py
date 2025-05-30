from sqlalchemy import BigInteger,String,ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(primary_key=True)
    tg_id=  mapped_column(BigInteger)

class Zherler(Base):
    __tablename__= 'Zherlergo'

    id:Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

class Kalalar(Base):
    __tablename__ = 'Kalalargo'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(120))
    ataular:Mapped[str]=mapped_column()
    zherler:Mapped[int]=mapped_column(ForeignKey('zherlergo.id'))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)