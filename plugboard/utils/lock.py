# encoding:utf-8
import functools
import inspect



def lock_func(lock_key):
    """
    :return:
    """
    def task_exec(func):
        @functools.wraps(func)
        def caller(*args, **kwargs):
            ret_value = None
            have_lock = False

            lock = redis_connect.lock(lock_key)
            try:
                have_lock = lock.acquire(blocking=True)
                if have_lock:
                    ret_value = func(*args, **kwargs)
            except Exception as e:
                raise e
            finally:
                if have_lock and redis_connect.get(lock_key):
                    lock.release()
                return ret_value

        return caller

    return task_exec


def single_task(lock_arg, lock_prefix="lock-", timeout=10):
    """
    :param lock_arg: set the lock key of the task parameter
    :param lock_prefix:
    :param timeout: set the lock key timeout
    Enforce only one celery task at a time.
    """

    def task_exec(func):
        @functools.wraps(func)
        def _caller(*args, **kwargs):

            ret_value = None
            have_lock = False

            call_args = inspect.getcallargs(func, **kwargs)
            lock_key = call_args.get(lock_arg)
            lock_key = lock_prefix + str(lock_key)

            lock = redis_connect.lock(lock_key, timeout=timeout)
            try:
                have_lock = lock.acquire(blocking=False)
                if have_lock:
                    ret_value = func(*args, **kwargs)
            except Exception as e:
                raise e
            finally:
                if have_lock and redis_connect.get(lock_key):
                    lock.release()
                return ret_value

        return _caller

    return task_exec
