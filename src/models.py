from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column



db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
    created_at: Mapped[str] = mapped_column(DateTime(), server_default=func.now())

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_active": self.is_active,
            "created_at": self.created_at
        }


class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(1000))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    media_url: Mapped[str] = mapped_column(String(500), nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime(), server_default=func.now())

    # Relationships
    user: Mapped["User"] = db.relationship("User", backref="posts")

    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "media_url": self.media_url,
            "user_id": self.user_id,
            "created_at": self.created_at
        }


class Comment(db.Model):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime(), server_default=func.now())

    # Relationships
    user: Mapped["User"] = db.relationship("User", backref="comments")
    post: Mapped["Post"] = db.relationship("Post", backref="comments")

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "created_at": self.created_at
        }


class Like(db.Model):
    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime(), server_default=func.now())

    # Relationships
    user: Mapped["User"] = db.relationship("User", backref="likes")
    post: Mapped["Post"] = db.relationship("Post", backref="likes")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "created_at": self.created_at
        }