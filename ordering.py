from sqlalchemy.orm import session
from main import User ,Session, engine

session = Session(bind=engine)

#assending order
users = session.query(User).order_by(User.username).all()

for user in users:
    print(user.username, user.id, user.email)

session.commit()