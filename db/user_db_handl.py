from db.models import User


def add_new_user(user_id: int, chat_id: int, user_name: str,
                 first_name: str, is_reminders: bool) -> None:
    if User.get_or_none(User.user_id == user_id) is not None:
        user = User.update(
            user_name=user_name,
            first_name=first_name,
            is_reminders=is_reminders
        ).where(User.user_id == user_id)
        user.execute()
    else:
        User.create(
            user_id=user_id,
            chat_id=chat_id,
            user_name=user_name,
            first_name=first_name,
            is_reminders=is_reminders
        )


def get_all_users() -> list[User]:
    users = User.select()
    return users


def get_user_is_reminder_by_chat_id(chat_id: int) -> bool:
    user = User.get(User.chat_id == chat_id)
    return user.is_reminders


def update_user_is_reminder_by_chat_id(chat_id: int, is_reminders: bool) -> None:
    user = User.update(is_reminders=is_reminders).where(User.chat_id == chat_id)
    user.execute()
