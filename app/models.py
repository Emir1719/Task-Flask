from . import db
from sqlalchemy import Boolean, Column, Integer, String, Text

class Task(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=False, nullable=False)
    content = Column(Text(), unique=False, nullable=False)
    complete = Column(Boolean(), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "complete": self.complete
        }