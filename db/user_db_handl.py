from db.models import User
from db.plna_db_handl import delete_plan_by_id, delete_plan_by_chat_id
from db.story_db_handl import delete_history_by_id


def add_user(chat_id: int, user_name: str,
             first_name: str, is_reminders: bool = False) -> None:
    User.create(
        chat_id=chat_id,
        user_name=user_name,
        first_name=first_name,
        is_reminders=is_reminders
    )


def update_user_first_name(chat_id: int, first_name: str) -> None:
    user = User.get(chat_id=chat_id)
    user.first_name = first_name
    user.save()


def get_users() -> list[User]:
    users = User.select()
    return [user for user in users]


def get_user_by_chat_id(chat_id: int) -> User | None:
    user = User.get_or_none(User.chat_id == chat_id)
    return user


def update_user_reminder_by_chat_id(chat_id: int, is_reminders: bool) -> None:
    user = User.update(is_reminders=is_reminders).where(User.chat_id == chat_id)
    user.execute()


def del_user_by_chat_id(chat_id: int) -> None:
    delete_plan_by_chat_id(chat_id)
    delete_history_by_id(chat_id)
    User.delete().where(User.chat_id == chat_id).execute()
