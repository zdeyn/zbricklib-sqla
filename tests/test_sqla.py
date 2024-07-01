from flask import Flask
from zbricklib_sqla import zSQLAlchemy, Base
from zbricklib_sqla import Mapped, mapped_column
from zbricklib_sqla import select, inspect


from zbricklib.extension import zExtension

def test_is_zextension():
    sqla = zSQLAlchemy()
    assert isinstance(sqla, zExtension)

def test_can_install_into_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    sqla : zSQLAlchemy = zSQLAlchemy()
    sqla.init_app(app)
    assert app.extensions['sqla'] is sqla
    # with app.app_context():
    #     sqla.engine.echo = True
    
    class ExampleModel(Base):
        __tablename__ = 'example'
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column()
    
    with app.app_context():
        sqla.create_all()
    
    # Check if the table for ExampleModel has been created
    with app.app_context():        
        inspector = inspect(sqla.engine)
        tables = inspector.get_table_names()
        assert 'example' in tables