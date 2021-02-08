import logging
from argparse import ArgumentParser
from datetime import datetime

from cn_v2.manager import WatcherManager, CourseManager

term_code = {"DA": "202132", "FH": "202131"}

arg_parser = ArgumentParser(description="Course Notify Manager")

arg_parser.add_argument("--log_file",
                        help="Path to log file",
                        required=False)

arg_parser.add_argument("--config_file",
                        help="Path to configuration file",
                        required=True)

arg_parser.add_argument("--school",
                        choices=["DA", "FH"],
                        help="Which school to manage",
                        required=True)

arg_parser.add_argument("-c", "--update_course",
                        help="Update all course data",
                        action="store_true")

arg_parser.add_argument("-s", "--update_seats",
                        help="Update seats data only",
                        action="store_true")

arg_parser.add_argument("-n", "--send_notification",
                        help="Send notification email to watchers",
                        action="store_true")

arg_parser.add_argument("-v", "--verbose",
                        help="Verbose",
                        action="store_true")

args = arg_parser.parse_args()


def print_error(msg):
    print("[ERROR] " + msg)


def create_logger():
    logger = logging.getLogger("CourseNotify Logger")
    formatter = logging.Formatter("[%(levelname)s][%(asctime)s][%(name)s] - %(message)s")

    fh = logging.FileHandler(args.log_file)
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)

    logger.addHandler(fh)
    logger.setLevel(logging.INFO)
    return logger


course_manager = CourseManager(school=args.school, config_file=args.config_file, term_code=term_code)
watcher_manager = WatcherManager(school=args.school, config_file=args.config_file)


def update_course():
    course_manager.update_course_collection()


def update_seats():
    course_manager.update_course_collection()


def send_notification():
    watcher_manager.notify_all()


if args.update_course:
    update_course()
if args.update_seats:
    update_seats()
if args.send_notification:
    send_notification()
