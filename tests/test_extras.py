from app import cache, scheduler


def test_cache_and_scheduler():
    assert cache.cache_task_1('x')
    assert scheduler.scheduler_task_1('y')

