from flask import Flask, render_template
from flask import request, escape

app = Flask(__name__)

@app.route("/")
def index():
  # return render_template('index.html')
  celsius = str(escape(request.args.get("celsius", "")))
  if celsius:
    faren = to_farenheit_from(celsius)
  else:
    faren = ""
  return """
  <html>
  <head>
    <link rel="stylesheet" href='../static/style.css' />
  </head>
  <body>
  <form>
      <fieldset><legend>Celsius To Farenheit</legend><br/>
      <label for="celsius"><span>Input Celsius: </span><input type="text" name="celsius"></label>
      <label><span> </span><input type="submit" value="Convert" /></label>
    """ + """<br/><br/><label><span>Farenheit: </span></label>""" + faren + "</fieldset></form></body>"

@app.route("/<int:celsius>")
def to_farenheit_from(celsius):
  """Converts to farenheit"""
  try:
    faren = float(celsius) * (9/5) + 32
    faren = round(faren, 3)
    return str(faren)
  except ValueError:
    return "Invalid entry"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)