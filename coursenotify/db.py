from cn_v2.manager import CourseManager
from flask import current_app, g


def get_course_manager():
    if 'course_manager' not in g:
        g.course_manager = {"DA": CourseManager(current_app.config["MANAGER_CONFIG"], CourseManager.DA),
                            "FH": CourseManager(current_app.config["MANAGER_CONFIG"], CourseManager.FH)}
    return g.course_manager


def init_course_db():
    get_course_manager()["DA"].update_course_collection()
    get_course_manager()["FH"].update_course_collection()
