from typing import Union, Type

from cn_v2.manager import CourseManager, WatcherManager
from flask import current_app, g


def get_manager(school, which: Union[Type[CourseManager], Type[WatcherManager]]) -> Union[
    CourseManager, WatcherManager]:
    if which == CourseManager:
        n = "course_manager"
    elif which == WatcherManager:
        n = "watcher_manager"
    else:
        raise RuntimeError("Expected subclass of BaseManager, got %s" % which)
    if n not in g:
        g.n = {school: which(current_app.config["MANAGER_CONFIG"], school)}
    if school not in g.n:
        g.n[school] = which(current_app.config["MANAGER_CONFIG"], school)

    return g.n[school]


def get_course_manager(school) -> CourseManager:
    return get_manager(school, CourseManager)


def get_watcher_manager(school) -> WatcherManager:
    return get_manager(school, WatcherManager)


def check_db_connection():
    return get_course_manager("DA").check_mongo_connection() and get_watcher_manager("DA").check_mongo_connection()


def init_course_db():
    get_course_manager("DA").update_course_collection()
    get_course_manager("FH").update_course_collection()
