from datetime import datetime, timedelta

from db.models import Plan


def add_new_plan(chat_id: int, type_plan: str, day: int, start_time: datetime.time) -> None:
    plan = Plan.get_or_none(Plan.chat_id == chat_id, Plan.day == day, Plan.type_plan == type_plan)
    if plan is not None:
        plan.time = start_time
        plan.save()
        return

    Plan.create(chat_id=chat_id,
                type_plan=type_plan,
                day=day,
                time=start_time
                )


def get_immediate_plans(type_plan: str) -> list:
    start_time = datetime.now().time()
    end_time = timedelta(hours=start_time.hour, minutes=start_time.minute) + timedelta(hours=0, minutes=15)
    day = datetime.now().weekday()
    users = Plan.select().where(
        (Plan.day == day) &
        (Plan.time >= start_time) &
        (Plan.time <= end_time) &
        (Plan.total_alarm == 0) &
        (Plan.type_plan == type_plan)
    )
    users = [user for user in users]
    plan = Plan.update(total_alarm=1).where(
        (Plan.day == day) &
        (Plan.time >= start_time) &
        (Plan.time <= end_time) &
        (Plan.total_alarm == 0) &
        (Plan.type_plan == type_plan)
    )
    plan.execute()
    return users


def update_all_total_alarm_to_false() -> None:
    plan = Plan.update(total_alarm=False)
    plan.execute()
