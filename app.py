from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import datetime

from methods.goldenSearch import goldenSectionSearch
from methods.bissectionSearch import bissectionSearch
from methods.newtonSearch import newtonSearch
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
    tableData = {
        'time': [],
        'd': [],
        'x1': [],
        'fx1': [],
        'x2': [],
        'fx2': [],
        'a': [],
        'b': [],
    } 

    try:
        function, a, b, limit = data["function"], data["interval"][0], data["interval"][1], data["limit"]
        [x, fx, time] = goldenSectionSearch(tableData, function, a, b, limit)
        
        base64Image = plot2D(function, x, fx, a, b)

        return jsonify(
            {
                "x": x,
                "fx": fx,
                "time": time,
                "img": base64Image,
                "data": tableData
            }
        ), 200
    except NameError as error:
        return jsonify({"error": error.args[0]}), 400
    except TimeoutError as error:
        return jsonify({"error": error.args[0]}), 408
    except Exception as error:
        print(error)
        return jsonify({"error": "Erro interno do servidor"}), 500

@app.route('/bissectionSearch', methods=['POST'])
@cross_origin()
def bissectionRoute():
    data = request.get_json()
    
    tableData = {
        'time': [],
        'lmbda': [],
        'flmbda': [],
        'a': [],
        'b': [],
    } 

    try:
        function, a, b, limit = data["function"], data["interval"][0], data["interval"][1], data["limit"]
        [x, fx, time] = bissectionSearch(tableData, function, a, b, limit)
        
        base64Image = plot2D(function, x, fx, a, b)

        return jsonify(
            {
                "x": x,
                "fx": fx,
                "time": time,
                "img": base64Image,
                "data": tableData
            }
        ), 200
    except NameError as error:
        return jsonify({"error": error.args[0]}), 400
    except TimeoutError as error:
        return jsonify({"error": error.args[0]}), 408
    except Exception as error:
        print(error)
        return jsonify({"error": "Erro interno do servidor"}), 500
    
@app.route('/newtonSearch', methods=['POST'])
@cross_origin()
def newtonRoute():
    data = request.get_json()
    
    tableData = {
        'time': [],
        'lmbda': [],
        'firstderiv': [],
        'secondderiv': [],
        'lmbdanext': [],
    }   

    try:
        function, initialValue, a, b, limit = data["function"], data["initialValue"], data["interval"][0], data["interval"][1], data["limit"]
        [x, fx, time] = newtonSearch(tableData, function, initialValue, limit)
        
        base64Image = plot2D(function, x, fx, a, b)

        return jsonify(
            {
                "x": x,
                "fx": fx,
                "time": time,
                "img": base64Image,
                "data": tableData
            }
        ), 200
    except NameError as error:
        return jsonify({"error": error.args[0]}), 400
    except TimeoutError as error:
        return jsonify({"error": error.args[0]}), 408
    except Exception as error:
        print(error)
        return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)