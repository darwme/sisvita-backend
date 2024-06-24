from utils.db import db
from dataclasses import dataclass
import pandas as pd

@dataclass
class Ubicacion(db.Model):
    __tablename__='ubicacion'
    id_ubicacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ubigeo = db.Column(db.String(6))
    distrito = db.Column(db.String(50))
    provincia = db.Column(db.String(50))
    y = db.Column(db.Float)
    x = db.Column(db.Float)

    def __init__(self, ubigeo: str, distrito: str, provincia: str, y: float, x: float):
        self.ubigeo = ubigeo
        self.x = x
        self.y = y
        self.provincia = provincia
        self.distrito = distrito

    @staticmethod
    def upload_ubicacion_peru():

        file_path = 'utils/data.xlsx'

        df = pd.read_excel(file_path, header=0, usecols=['ubigeo', 'distrito', 'provincia', 'y', 'x'])

        print('Columnas: ', df.columns)

        if Ubicacion.query.first() is not None:
            print('Ubicacion ya cargada')
            return
            
                
        for index, row in df.iterrows():
            ubigeo = str(row['ubigeo'])
            distrito = str(row['distrito'])
            provincia = str(row['provincia'])
            y = float(row['y'])
            x = float(row['x'])

                
            ubicacion = Ubicacion(ubigeo, distrito, provincia, x, y)
            db.session.add(ubicacion)

        print('Ubicacion cargada')
        db.session.commit()