from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from main.util.rerank import rank_all

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="task_rank_all",
    ignore_result=True
)

def task_rank_all():
    rank_all()
    logger.info("running cron job")