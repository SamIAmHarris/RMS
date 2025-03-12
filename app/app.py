from flask import Flask, jsonify, request, abort, Response
import json
from data import ASSESSMENT_RESPONSE, ACTIONS, INTRODUCTION_RESPONSE, RESULTS_RESPONSE

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"message": "Mock API Server is running"})


@app.route('/api/assessment', methods=['GET'])
def get_assessment():
    return Response(json.dumps(ASSESSMENT_RESPONSE), mimetype='application/json')


@app.route('/api/action', methods=['GET'])
def get_action():
    # Get the required type parameter
    action_type = request.args.get('type')

    # If type parameter is missing, return 400 Bad Request
    if not action_type:
        abort(400, description="Missing required parameter: type")

    # Check if the action type exists
    if action_type not in ACTIONS:
        abort(404, description=f"Action type '{action_type}' not found")

    # Get the response based on the action type
    response = ACTIONS[action_type]

    # If it's a jump action and id parameter is provided, update the item_id
    if action_type == "jump" and request.args.get('id'):
        item_id = request.args.get('id')
        response = {"action": {"jump": {"item_id": item_id}}}

    return jsonify(response)


@app.route('/api/response', methods=['GET'])
def get_response():
    # Get the item_id parameter
    item_id = request.args.get('item_id')
    skip = request.args.get("skip", default="false").lower() == "true"

    if skip:
        return jsonify(ACTIONS["next"])

    # If item_id parameter is missing, return 400 Bad Request
    if not item_id:
        abort(400, description="Missing required parameter: item_id")

    # Return appropriate action based on item_id
    if item_id in ["1", "2", "1200"]:
        # For items 1 and 2, return "next" action
        return jsonify(ACTIONS["next"])
    elif item_id == "1001":
        # For item 1001, return "jump" action to item 1004
        return jsonify({"action": {"jump": {"item_id": "1004"}}})
    elif item_id == "1004":
        # For item 1004, return "results" action
        return jsonify(ACTIONS["mark_completed"])
    else:
        # Default to "next" for any other item_id
        return jsonify(ACTIONS["next"])


@app.route('/api/introduction', methods=['GET'])
def get_response():
    return jsonify(INTRODUCTION_RESPONSE)


@app.route('/api/results', methods=['GET'])
def get_response():
    return jsonify(RESULTS_RESPONSE)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
