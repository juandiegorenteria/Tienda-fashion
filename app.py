from flask import Flask, render_template, redirect, session, request
import os

app = Flask(__name__)

app.secret_key = "tienda123"


productos_lista = [

{"id":1,"nombre":"Camiseta Bélgica","precio":120,"imagen":"camiseta1.webp"},
{"id":2,"nombre":"Camiseta Brasil","precio":130,"imagen":"camiseta2.webp"},
{"id":3,"nombre":"Camiseta Croacia","precio":130,"imagen":"camiseta3.webp"},
{"id":4,"nombre":"Camiseta España","precio":130,"imagen":"camiseta4.webp"},
{"id":5,"nombre":"Camiseta Francia","precio":130,"imagen":"camiseta5.webp"},
{"id":6,"nombre":"Camiseta Inglaterra","precio":130,"imagen":"camiseta6.jpeg"},
{"id":7,"nombre":"Camiseta Uruguay","precio":130,"imagen":"camiseta7.webp"},
{"id":8,"nombre":"Camiseta Argentina","precio":130,"imagen":"camiseta8.avif"},

{"id":9,"nombre":"Short Deportivo","precio":140,"imagen":"sh1.webp"},
{"id":10,"nombre":"Short Deportivo","precio":130,"imagen":"sh2.webp"},
{"id":11,"nombre":"Short Deportivo","precio":130,"imagen":"sh3.webp"},
{"id":12,"nombre":"Short Deportivo","precio":130,"imagen":"sh4.webp"},
{"id":13,"nombre":"Short Deportivo","precio":130,"imagen":"sh5.webp"},
{"id":14,"nombre":"Short Deportivo","precio":130,"imagen":"sh6.webp"},
{"id":15,"nombre":"Short Deportivo","precio":130,"imagen":"sh7.webp"},
{"id":16,"nombre":"Short Deportivo","precio":150,"imagen":"sh8.webp"},

{"id":17,"nombre":"Polo Camisero","precio":90,"imagen":"polo1.webp"},
{"id":18,"nombre":"Polo Camisero","precio":85,"imagen":"polo2.webp"},
{"id":19,"nombre":"Polo Camisero","precio":85,"imagen":"polo3.webp"},
{"id":20,"nombre":"Polo Camisero","precio":85,"imagen":"polo4.webp"},
{"id":21,"nombre":"Polo Camisero","precio":85,"imagen":"polo5.webp"},
{"id":22,"nombre":"Polo Camisero","precio":90,"imagen":"polo6.webp"},
{"id":23,"nombre":"Polo Camisero","precio":95,"imagen":"polo7.webp"},
{"id":24,"nombre":"Polo Camisero","precio":100,"imagen":"polo8.webp"}

]


@app.route('/')
def inicio():

    cantidad = len(
        session.get(
            "carrito",
            []
        )
    )

    return render_template(
        "index.html",
        cantidad=cantidad
    )


@app.route('/productos')
def productos():

    cantidad = len(
        session.get(
            "carrito",
            []
        )
    )

    return render_template(
        "productos.html",
        productos=productos_lista,
        cantidad=cantidad
    )


@app.route('/agregar/<int:id>')
def agregar(id):

    carrito = session.get(
        "carrito",
        []
    )

    carrito.append(id)

    session["carrito"] = carrito

    return redirect("/carrito")


@app.route('/carrito')
def carrito():

    ids = session.get(
        "carrito",
        []
    )

    prendas=[]

    total=0

    for id in ids:

        for p in productos_lista:

            if p["id"]==id:

                prendas.append(
                    p
                )

                total+=p["precio"]

    cantidad=len(ids)

    return render_template(
        "carrito.html",
        carrito=prendas,
        total=total,
        cantidad=cantidad
    )


@app.route('/eliminar/<int:id>')
def eliminar(id):

    carrito=session.get(
        "carrito",
        []
    )

    if id in carrito:

        carrito.remove(
            id
        )

    session["carrito"]=carrito

    return redirect(
        "/carrito"
    )


@app.route('/vaciar')
def vaciar():

    session["carrito"]=[]

    return redirect(
        "/carrito"
    )


@app.route(
'/login',
methods=[
"GET",
"POST"
]
)
def login():

    cantidad=len(
        session.get(
            "carrito",
            []
        )
    )

    if request.method=="POST":

        correo=request.form[
            "correo"
        ]

        session[
            "usuario"
        ]=correo

        return redirect(
            "/"
        )

    return render_template(
        "login.html",
        cantidad=cantidad
    )


if __name__=="__main__":

    print(
        os.getcwd()
    )

    app.run(
        host="0.0.0.0",
        port=10000,
        debug=True
    )