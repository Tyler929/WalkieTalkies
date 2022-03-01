import random
from flask import jsonify, Blueprint

app_api = Blueprint('api', __name__,
                    url_prefix='/api',
                    template_folder='templates',
                    static_folder='static', static_url_path='static/api')

arts_data = []
art_list = [
    "Art used to be an olympic event",
    "Leonardo da Vinci Was a Procrastinator",
    "The Mona Lisa has her own mailbox in the Louvre because of all the love letters she receives",
    "Learning and practicing art leads to higher achievement in reading and maths",
    "Picasso owned a monkey, a dog, an owl, turtle, and cats",
    "Roman statues are made with detachable heads",
    "Painting Mona Lisa's lips took 12 years to complete",
    "The first pencil was invented in England in 1565",
    "Picasso learned how to draw first before walking",
    "Leonardo da Vinci was a vegetarian",
    "Leonardo da Vinci fought for animal rights during his time"
]


def _init_arts():
    item_id = 1
    for item in art_list:
        arts_data.append({"id": item_id, "art": item})
        item_id += 1


@app_api.route('/art')
def art():
    if len(arts_data) == 0:
        _init_arts()
    return jsonify(random.choice(arts_data))


if __name__ == "__main__":
    print(random.choice(art_list))