from flask import Flask, request, jsonify
import recommender

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = "youwillneverguess"


@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    experiment_id=request.args.get('experiment_id')
    user_id=request.args.get('user_id')
    if not experiment_id:
        raise Exception("No exepriment id given")
    return jsonify(recommender.get_articles(experiment_id, user_id))



if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
