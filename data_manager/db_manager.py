from .base import BaseManager, BaseModel
import psycopg2 as pg
import psycopg2.extras

class DBManager(BaseManager):
    
    def __init__(self, config: dict) -> None:
        super().__init__(config)  # {'db_config':{'dbname':'', 'host':'', 'password':'', 'user':'', ...}}
        self._db_config = config['db_config']
        self.__conn = pg.connect(**self._db_config)


    def create(self, m: BaseModel):
        pass

    def read(self, id: int, model_cls: type) -> BaseModel:
        assert issubclass(model_cls, BaseModel)
        assert getattr(model_cls, 'TABLE_NAME', None), "Could not find TABLE NAME"
        
        # Read from DB
        curs = self.__conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        curs.execute(f"SELECT * FROM {model_cls.TABLE_NAME} WHERE _id = %s", (id, ))
        model_data:dict = curs.fetchone()
        curs.close()

        # Convert to Model
        return model_cls.from_dict(model_data)


    def update(self, m: BaseModel) -> None:
        pass


    def delete(self, id: int, model_cls: type) -> None:
        pass

    def read_all(self, model_cls: type):
        pass