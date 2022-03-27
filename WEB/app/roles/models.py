from email.policy import default
from .. import db
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

class Role(RoleMixin, db.Model):
    """User acount modal we"""
    
    __tablename__ = 'role'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
