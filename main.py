from flask import Flask, flash, redirect, render_template, request, session, url_for

import products as db

app = Flask(__name__, template_folder="templates")  # явно вказуємо папку
app.secret_key = "your-secret-key"

# створюємо таблицю (не чіпаємо clear_db!)
db.create_table()


@app.route("/")
def index():
    products = db.get_all_products()
    return render_template("index.html", products=products)


@app.route("/new")
def new():
    new_items = db.get_new_products()
    return render_template("new.html", products=new_items)


# кошик
@app.route("/cart")
def view_cart():
    cart_items = []
    total_price = 0
    cart = session.get("cart", {})
    for product_id, quantity in cart.items():
        product = db.get_product(int(product_id))
        if product:
            cart_items.append(
                {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": quantity,
                    "total": product["price"] * quantity,
                    "image_url": product["image_url"],
                    "is_new": product["is_new"],
                }
            )
            total_price += product["price"] * quantity
    return render_template("cart.html", cart_items=cart_items, total_price=total_price)


@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = {}
    quantity = int(request.form.get("quantity", 1))
    product = db.get_product(product_id)
    if not product or quantity < 1:
        return render_template("error.html", error="Неможливо додати продукт"), 400
    session["cart"][str(product_id)] = session["cart"].get(str(product_id), 0) + quantity
    session.modified = True
    flash(f"Додано {product['name']} ({quantity} шт.) до кошика!", "success")
    return redirect(request.referrer or url_for("index"))


@app.route("/remove_from_cart/<int:product_id>")
def remove_from_cart(product_id):
    if "cart" in session:
        session["cart"].pop(str(product_id), None)
        session.modified = True
    flash("Продукт видалено з кошика!", "success")
    return redirect(url_for("view_cart"))


# маршрут для помилок
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error="Сторінку не знайдено"), 404


if __name__ == "__main__":
    app.run(debug=True)
