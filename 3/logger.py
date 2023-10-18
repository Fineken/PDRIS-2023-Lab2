from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    # Логирование данных (в реальном приложении, вы бы, возможно, записали данные в файл или систему логирования)
    print(data)
    return "Logged successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
