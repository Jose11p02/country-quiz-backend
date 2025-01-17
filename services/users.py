from models.users import users as users_m
from schemas.users import users as users_s
from sqlalchemy import func

class UsersServices():
    def __init__(self,db):
        self.db = db

    def add(self,users:users_s):
        new_user = users_m(**users.model_dump())
        self.db.add(new_user)
        self.db.commit()

    def get_top(self):
        result = self.db.query(users_m).order_by(users_m.score.desc()).limit(3).all()
        return result
    
    def get_users_by_country(self):
        users_by_country = self.db.query(users_m.country,func.count(users_m.id).label('user_count')).group_by(users_m.country).all()
        result = [{'country':country,'user_count':user_count }for country,user_count in users_by_country]
        return result