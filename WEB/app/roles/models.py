from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin



db = SQLAlchemy()

class Role(db.Model):
    """User acount modal we"""
    
    __tablename__ = 'role'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    estatus = db.Column(db.Boolean)
    
    
    def __str__(self):
        return self.name
    
     # __hash__ is required to avoid the exception TypeError: unhashable type: 'Role' when saving a User
    def __hash__(self):
        return hash(self.name)
    
    def __str__(self):
        return self.description
    
    def __str__(self):
        return self.estatus