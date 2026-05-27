from flask import Flask, render_template

app = Flask(__name__)

productos = [
    {
        "nombre": "Polo Negro",
        "precio": 45,
        "imagen": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab"
    },
    {
        "nombre": "Casaca Jeans",
        "precio": 120,
        "imagen": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246"
    },
    {
        "nombre": "Zapatillas Urbanas",
        "precio": 180,
        "imagen": "https://images.unsplash.com/photo-1542291026-7eec264c27ff"
    },
    {
        "nombre": "Gorra Moderna",
        "precio": 35,
        "imagen": "https://images.unsplash.com/photo-1521369909029-2afed882baee"
    }
]

@app.route('/')
def inicio():
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
