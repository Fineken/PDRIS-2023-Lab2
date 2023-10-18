from flask import Flask, request, redirect, url_for, render_template_string
import requests

app = Flask(__name__)

# Простой HTML шаблон для ввода данных и выбора сервиса
template = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Service Requester</title>
  </head>
  <body>
    <div class="container">
      <h1 class="mt-5">Service Requester</h1>
      <form method="post" action="/send">
        <div class="mb-3">
          <label for="service" class="form-label">Choose Service</label>
          <select class="form-select" name="service" id="service">
            <option value="data_processor">Data Processor</option>
            <option value="logger">Logger</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="data" class="form-label">Data (JSON format)</label>
          <textarea class="form-control" name="data" id="data" rows="3" placeholder='{"key": "value"}'></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Send Request</button>
      </form>
    </div>
    <!-- Optional JavaScript; choose one of the two! -->
    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template_string(template)

@app.route('/send', methods=['POST'])
def send_request():
    service = request.form['service']
    data = request.form['data']

    # Парсинг данных JSON
    try:
        data = json.loads(data)
    except ValueError:
        return "Invalid JSON format", 400

    # Определение URL сервиса на основе выбора пользователя
    url = {
        'data_processor': 'http://data_processor:5001/process',
        'logger': 'http://logger:5002/log'
    }.get(service)

    if not url:
        return "Invalid service", 400

    # Отправка запроса к выбранному сервису
    response = requests.post(url, json=data)
    return response.text, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
