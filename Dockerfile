FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY ./coursenotify/ /app/coursenotify/
WORKDIR /app/coursenotify/

# run  >pip install -e "git+https://github.com/Larryun/coursenotify_v2#egg=cn_v2"
