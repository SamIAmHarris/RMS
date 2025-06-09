from flask import Flask, jsonify, request, abort, Response
import json
from datetime import date
from typing import List, Dict

from data import (ASSESSMENT_RESPONSE, EXPLORE_RESPONSE, ACTIONS, CONSUME_PAGE_RESPONSE, REFRESH_TODAY_PAGE_RESPONSE,
                  INTRODUCTION_RESPONSE, RESULTS_RESPONSE, PFT_TEST_RESPONSE, TODAY_PAGE_RESPONSE, ACTIVITY_RESPONSE,
                  ACTIVATE_PAGE_RESPONSE, JOURNAL_RESPONSE)

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"message": "Mock API Server is running"})


@app.route('/api/assessment', methods=['GET'])
def get_assessment():
    return Response(json.dumps(ASSESSMENT_RESPONSE), mimetype='application/json')


@app.route('/api/consume_page', methods=['GET'])
def get_consume_page():
    return Response(json.dumps(CONSUME_PAGE_RESPONSE), mimetype='application/json')


@app.route('/api/explore', methods=['GET'])
def get_explore():
    return Response(json.dumps(EXPLORE_RESPONSE), mimetype='application/json')


@app.route('/api/today', methods=['GET'])
def get_today():
    return Response(json.dumps(TODAY_PAGE_RESPONSE), mimetype='application/json')


@app.route('/api/refresh_today', methods=['GET'])
def get_refresh_today():
    return Response(json.dumps(REFRESH_TODAY_PAGE_RESPONSE), mimetype='application/json')

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
        return jsonify(ACTIONS["results"])
    else:
        # Default to "next" for any other item_id
        return jsonify(ACTIONS["next"])


@app.route('/api/content/<string:content_id>', methods=['GET'])
def get_content(content_id):
    print(content_id)

    return Response(json.dumps(ASSESSMENT_RESPONSE), mimetype='application/json')

@app.route('/api/activate_page/<string:activate_page_id>', methods=['GET'])
def get_activate_page(activate_page_id):
    print(activate_page_id)

    return Response(json.dumps(ACTIVATE_PAGE_RESPONSE), mimetype='application/json')

@app.route('/api/activity/<string:activity_id>', methods=['GET'])
def get_activity(activity_id):
    print(activity_id)

    return Response(json.dumps(ACTIVITY_RESPONSE), mimetype='application/json')


@app.route('/api/journal/<string:journal_id>', methods=['GET'])
def get_journal(journal_id):
    print(journal_id)

    return Response(json.dumps(JOURNAL_RESPONSE), mimetype='application/json')


@app.route("/api/journal", methods=['POST'])
def submit_journal():
    return jsonify("{}")


@app.route('/api/dismiss_story_card/<string:content_id>', methods=['GET'])
def get_dismiss_story_card(content_id):
    print(content_id)

    return jsonify("{}")


@app.route("/api/content_actions", methods=['POST'])
def submit_content_action():
    return jsonify("{}")


@app.route("/api/pft_test", methods=['GET'])
def pft_mock_test():
    return jsonify(PFT_TEST_RESPONSE)


@app.route("/api/workouts", methods=['POST'])
def pft_mock_test_summary():
    logged_exercises = [
        {"slot_id": "1", "exercise_id": "1", "name": "Pushups", "score": 17, "logged_value": "50", "unit": "rep"},
        {"slot_id": "2", "exercise_id": "3", "name": "Situps", "score": 18, "logged_value": "45", "unit": "rep"},
        {"slot_id": "3", "exercise_id": "7", "name": "1.5 Mile Run", "score": 48, "logged_value": "12:30",
         "unit": "pace"}
    ]

    best_scores = {"1": 18, "2": 19, "3": 52}
    max_scores = {"1": 20, "2": 20, "3": 60}

    summary = generate_test_summary("PFT", logged_exercises, best_scores, max_scores)

    return json.dumps(summary, indent=2)


@app.route('/api/introduction', methods=['GET'])
def get_introduction():
    return jsonify(INTRODUCTION_RESPONSE)


@app.route('/api/results', methods=['GET'])
def get_results():
    return jsonify(RESULTS_RESPONSE)


def generate_test_summary(
        test_type: str,
        logged_exercises: List[Dict],
        best_scores_lookup: Dict[str, float],
        max_scores_lookup: Dict[str, float]
) -> Dict:
    composite_score = sum(ex["score"] for ex in logged_exercises)
    best_score = sum(best_scores_lookup.get(ex["exercise_id"], 0) for ex in logged_exercises)

    def get_status(score: float, max_score: float) -> str:
        percentage = (score / max_score) * 100 if max_score > 0 else 0
        if percentage >= 90:
            return "Excellent"
        elif percentage >= 75:
            return "Good"
        elif percentage >= 50:
            return "Fair"
        else:
            return "Needs Improvement"

    exercises_summary = []
    for ex in logged_exercises:
        slot_id = ex["slot_id"]
        ex_id = ex["exercise_id"]
        score = ex["score"]
        max_score = max_scores_lookup.get(ex_id, 0)
        best_score_ex = best_scores_lookup.get(ex_id, 0)

        exercises_summary.append({
            "slot_id": slot_id,
            "exercise_id": ex_id,
            "name": ex["name"],
            "score": score,
            "best_score": best_score_ex,
            "max_score": max_score,
            "logged_value": ex["logged_value"],
            "unit": ex["unit"],
            "status": get_status(score, max_score)
        })

    return {
        "test_date": str(date.today()),
        "test_type": test_type,
        "best_score": best_score,
        "composite_score": composite_score,
        "composite_status": get_status(composite_score, sum(max_scores_lookup.values())),
        "slots": exercises_summary
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
