from flask import Flask, request, jsonify, send_file
from flask_cors import CORS, cross_origin
import datetime

from methods.goldenSearch import goldenSectionSearch
from services.plots import plot2D

now = datetime.datetime.now()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Rota para criar um novo item
@app.route('/', methods=['GET'])
@cross_origin()
def mainRoute():
    return jsonify({"msg": f"API Otimizae v1.0.0 {now.strftime('%Y-%m-%d %H:%M:%S')}"}), 200

@app.route('/goldenSearch', methods=['POST'])
@cross_origin()
def goldenSearchRoute():
    data = request.get_json()
    try:
        function, a, b, limit = data["function"], data["interval"][0], data["interval"][1], data["limit"]
        [x, fx, time] = goldenSectionSearch(function, a, b, limit)
        
        base64Image = plot2D(function, x, fx, a, b)

        return jsonify(
            {
                "x": x,
                "fx": fx,
                "time": time,
                "img": base64Image
            }
        ), 200
    except Exception as error:
        print(error)
        return jsonify({"error": "Erro interno do servidor"}), 500

    
if __name__ == '__main__':
    app.run(debug=True)