from datetime import date, datetime, timedelta

from db.models import Story


def add_report_pray(chat_id: int, is_pray: bool, date_pray: date) -> None:
    Story.create(
        chat_id=chat_id,
        date=date_pray,
        is_pray=is_pray,
    )


def update_report_pray(chat_id: int, is_pray: bool, date_pray: date) -> None:
    story = Story.get(chat_id=chat_id, date=date_pray)
    story.is_pray = is_pray
    story.save()


def get_reports_lost_pray_last_week_where_chat_id(chat_id: int) -> list[Story]:
    week_ago = date.today() - timedelta(days=7)
    story = Story.select().where(
        (Story.is_pray == 0) &
        (Story.date >= week_ago) &
        (Story.date < date.today()) &
        (Story.chat_id == chat_id)
    )
    return story


def get_reports_lost_pray_last_week() -> list[Story]:
    week_ago = date.today() - timedelta(days=7)
    story = Story.select().where(
        (Story.is_pray == 0) &
        (Story.date >= week_ago) &
        (Story.date < date.today())
    )
    return story


def get_reports_last_month_by_chat_id(chat_id: int) -> list[Story]:
    month_ago = date.today() - timedelta(days=30)
    story = Story.select().where(
        (Story.chat_id == chat_id) &
        (Story.date >= month_ago)
    )
    return story


def delete_history_by_id(chat_id: int) -> None:
    Story.delete().where(Story.chat_id == chat_id).execute()
