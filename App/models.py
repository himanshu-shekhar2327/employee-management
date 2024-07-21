from .db_instance import db
#from flask_sqlalchemy import SQLALchemy

#db=SQLALchemy(app)
class Employee(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer,nullable=False)
    def __init__(self,name,department,age):
        self.name=name
        self.department=department
        self.age=age
    def to_dict(self):
        return {
               "id":self.id,
               "name":self.name,
               "department":self.department,
               "age":self.age
            }
    def __repr__(self):
        return f'<Employee {self.name}>'