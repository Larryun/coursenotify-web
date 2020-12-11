from cn_v2.exception import *
from email_validator import validate_email, EmailNotValidError
from flask import Blueprint, request, jsonify, current_app
from flask_cors import cross_origin

from coursenotify.manager import get_watcher_manager, get_course_manager

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/add", methods=["POST"])
@cross_origin()
def add():
    result = {"status": "failed"}
    try:
        data = request.get_json()
        watcher_manager = get_watcher_manager(data["school"])
        validate_email(data["email"], check_deliverability=False)
        if watcher_manager:
            if not isinstance(data["crn"], list):
                result["status"] = "failed"
                result["crn"] = "expected list"
            else:
                for crn in data["crn"]:
                    watcher_manager.add_watchee(data["email"], str(crn))
                result["status"] = "ok"
                # TODO add send confirmation email when done
        else:
            current_app.logger.error("<%s> school %s not valid" % (data["email"], data["school"]))
            result["school"] = "not valid"
    except CRNNotFound:
        current_app.logger.error("<%s> CRN %s not found" % (data["email"], data["crn"]))
        result["crn"] = "not valid"
    except EmailNotValidError:
        current_app.logger.error("<%s> email not valid" % (data["email"]))
        result["email"] = "not valid"
    except Exception as e:
        current_app.logger.error(str(e))
        result["server_error"] = 1
    return jsonify(result)


def find_course_by_crn_prefix(school, crn):
    course_m = get_course_manager(school)
    projection = {"_id": 0, "title": 1, "name": 1, "crn": 1, "status": 1, }
    courses = course_m.course_cc.find({"crn": {"$regex": "^" + str(crn)}}, projection)
    return courses


@api.route("/query", methods=["POST"])
@cross_origin()
def query_course():
    result = {"status": "failed"}
    try:
        data = request.get_json()
        if len(str(data["crn"])) < 3:
            result["status"] = "failed"
            result["course"] = "crn length to short"
        else:
            courses = find_course_by_crn_prefix(data["school"], data["crn"])
            result["course"] = list(courses)
            result["status"] = "ok"
    except CRNNotFound as e:
        result["course"] = "not found"
        current_app.logger.error(str(e))
    except Exception as e:
        print(str(e))
        result["server_error"] = 1

    return jsonify(result)


@api.route("/remove", methods=["POST"])
@cross_origin()
def remove_watch():
    result = {"status": "failed"}
    status_code = 404
    try:
        data = request.get_json()
        watcher_m = get_watcher_manager(data["school"])
        watcher_m.remove_watchee_by_remove_key(data["remove_key"])
        result["status"] = "succeed"
        status_code = 200
    except RemoveKeyNotFound as e:
        current_app.logger.error(str(e))
        result["msg"] = "remove key not found"
    except RemoveKeyUsed as e:
        current_app.logger.error(str(e))
        result["msg"] = "removed key is used"
    except KeyError as e:
        current_app.logger.error("KeyError " + str(e))
        result["key_error"] = 1
        status_code = 400
    except Exception as e:
        current_app.logger.error(str(e))
        result["server_error"] = 1
        status_code = 500
    return jsonify(result), status_code
