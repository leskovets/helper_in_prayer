import logging

from datetime import datetime, timedelta

from db.models import Plan

db_plan_handler = logging.getLogger(name="db_handler")


def add_new_plan(chat_id: int, type_plan: str, day: int, start_time: datetime.time) -> None:
    plan = Plan.get_or_none(Plan.chat_id == chat_id, Plan.day == day, Plan.type_plan == type_plan)
    if plan is not None:
        plan.time = start_time
        plan.save()
    else:
        Plan.create(chat_id=chat_id,
                    type_plan=type_plan,
                    day=day,
                    time=start_time
                    )
    db_plan_handler.debug(f"{chat_id} было обновлён план")


def get_immediate_plans() -> list:
    start_time = datetime.now().time()
    end_time = timedelta(hours=start_time.hour, minutes=start_time.minute) + timedelta(hours=0, minutes=15)
    day = datetime.now().weekday()
    users = Plan.select().where(
        (Plan.day == day) &
        (Plan.time >= start_time) &
        (Plan.time <= end_time) &
        (Plan.total_alarm == 0)
    )
    users = [user for user in users]

    plan = Plan.update(total_alarm=1).where(
        (Plan.day == day) &
        (Plan.time >= start_time) &
        (Plan.time <= end_time) &
        (Plan.total_alarm == 0)
    )
    plan.execute()
    return users


def update_all_total_alarm_to_false() -> None:
    plan = Plan.update(total_alarm=False)
    plan.execute()


def delete_plan_by_id(id_plan: int) -> None:
    Plan.delete().where(Plan.id == id_plan)


def get_plan_by_id(id_plan: int) -> Plan:
    return Plan.get(Plan.id == id_plan)


def add_postponement_plan_by_chat_id(chat_id: int, day: int, start_time: datetime.time) -> None:
    Plan.create(chat_id=chat_id,
                type_plan="postponement",
                day=day,
                time=start_time
                )


