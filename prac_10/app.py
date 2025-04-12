from flask import Flask

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

@app.route('/convert')
@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        celsius_float = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        return f"<h3>{celsius_float}°C is {fahrenheit:.2f}°F</h3>"
    except ValueError:
        return "<p>Please enter a valid number for Celsius.</p>"

if __name__ == '__main__':
    app.run()