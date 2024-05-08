from db.models import User


def add_user(chat_id: int, user_name: str,
             first_name: str, is_reminders: bool = False) -> None:
    User.create(
        chat_id=chat_id,
        user_name=user_name,
        first_name=first_name,
        is_reminders=is_reminders
    )


def get_users() -> list[User]:
    users = User.select()
    return users


def get_user_by_chat_id(chat_id: int) -> User | None:
    user = User.get_or_none(User.chat_id == chat_id)
    return user


def check_reminder_by_chat_id(chat_id: int) -> bool:
    user = User.get(User.chat_id == chat_id)
    return user.is_reminders


def update_user_reminder_by_chat_id(chat_id: int, is_reminders: bool) -> None:
    user = User.update(is_reminders=is_reminders).where(User.chat_id == chat_id)
    user.execute()
