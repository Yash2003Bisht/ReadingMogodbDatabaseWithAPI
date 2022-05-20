from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

def create_dict():
    python_dict = []
    db = MongoClient("mongodb://localhost:27017").dashboard
    for data in db.visualizationdashboard.find():
        python_dict.append(
            {
                "_id": f"{data['_id']}",
                "end_year": data["end_year"],
                "intensity": data["intensity"],
                "sector": data["sector"],
                "topic": data["topic"],
                "insight": data["insight"],
                "url": data["url"],
                "region": data["region"],
                "start_year": data["start_year"],
                "impact": data["impact"],
                "added": data["added"],
                "published": data["published"],
                "country": data["country"],
                "relevance": data["relevance"],
                "pestle": data["pestle"],
                "source": data["source"],
                "title": data["title"],
                "likelihood": data["likelihood"]
            
            }
        )
    return python_dict

@app.route(f"/mongodb-api/userapi=<string:api>")
def dataBase(api):
    return jsonify(create_dict())

if __name__ == "__main__":
    app.run(debug=True, port="5555")