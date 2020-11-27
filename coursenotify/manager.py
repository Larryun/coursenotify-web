from cn_v2.manager import CourseManager, WatcherManager
from flask import current_app, g


def get_course_manager(school):
    if school not in ["DA", "FH"]:
        return None
    if 'course_manager' not in g:
        g.course_manager = {school: CourseManager(current_app.config["MANAGER_CONFIG"], school)}
    if school not in g.course_manager:
        g.course_manager[school] = CourseManager(current_app.config["MANAGER_CONFIG"], school)

    return g.course_manager[school]


def get_watcher_manager(school):
    if school not in ["DA", "FH"]:
        return None
    if 'watcher_manager' not in g:
        g.watcher_manager = {school: WatcherManager(current_app.config["MANAGER_CONFIG"], school)}
    if school not in g.watcher_manager:
        g.watcher_manager[school] = WatcherManager(current_app.config["MANAGER_CONFIG"], school)

    return g.watcher_manager[school]


def init_course_db():
    get_course_manager("DA").update_course_collection()
    get_course_manager("FH").update_course_collection()
