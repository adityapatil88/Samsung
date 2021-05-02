from config import app
from flask import request
from impl import main


@app.route('/GetOrderedRelation', methods=['POST'])
def get_ordered_relation():
    data = request.json
    if not(data['node_ids'] or data['relation']):
        return {"msg": "required parameter missing"}, 400
    return dict(j for i in main(data) for j in i.items())


