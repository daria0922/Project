from flask import Flask, flash, redirect, render_template, request, session, url_for

import products as db  # твій products.py

app = Flask(__name__)
app.secret_key = "your-secret-key"  # заміни на безпечний ключ для сесій

# ✅ створюємо таблицю, якщо її ще немає (не чіпаємо clear_db!)
db.create_table()


@app.route("/")
def index():
    try:
        products = db.get_all_products()
        return render_template("index.html", products=products)
    except Exception as e:
        return render_template("error.html", error=str(e)), 500


@app.route("/new")
def new():
    try:
        new_items = db.get_new_products()
        return render_template("new.html", products=new_items)
    except Exception as e:
        return render_template("error.html", error=str(e)), 500


@app.route("/cart")
def view_cart():
    try:
        cart_items = []
        total_price = 0
        cart = session.get("cart", {})
        for product_id, quantity in cart.items():
            product = db.get_product(int(product_id))
            if product:
                item_total = product["price"] * quantity
                cart_items.append(
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                        "quantity": quantity,
                        "total": item_total,
                        "image_url": product["image_url"],
                        "is_new": product["is_new"],
                    }
                )
                total_price += item_total
        return render_template("cart.html", cart_items=cart_items, total_price=total_price)
    except Exception as e:
        return render_template("error.html", error=str(e)), 500


@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id: int):
    try:
        if "cart" not in session:
            session["cart"] = {}
        quantity = int(request.form.get("quantity", 1))
        if quantity < 1:
            raise ValueError("Кількість має бути більше 0")
        product = db.get_product(product_id)
        if not product:
            raise ValueError("Продукт не знайдено")
        if product["stock"] < quantity:
            raise ValueError(f"Недостатньо товару на складі (доступно: {product['stock']})")
        session["cart"][str(product_id)] = session["cart"].get(str(product_id), 0) + quantity
        session.modified = True
        flash(f"Додано {product['name']} ({quantity} шт.) до кошика!", "success")
        return redirect(url_for("index"))
    except Exception as e:
        return render_template("error.html", error=str(e)), 400


@app.route("/update_cart/<int:product_id>", methods=["POST"])
def update_cart(product_id: int):
    try:
        quantity = int(request.form.get("quantity", 0))
        product = db.get_product(product_id)
        if not product:
            raise ValueError("Продукт не знайдено")
        if quantity < 0:
            raise ValueError("Кількість не може бути від’ємною")
        if quantity > product["stock"]:
            raise ValueError(f"Недостатньо товару на складі (доступно: {product['stock']})")
        if quantity == 0:
            session["cart"].pop(str(product_id), None)
        else:
            session["cart"][str(product_id)] = quantity
        session.modified = True
        flash("Кошик оновлено!", "success")
        return redirect(url_for("view_cart"))
    except Exception as e:
        return render_template("error.html", error=str(e)), 400


@app.route("/remove_from_cart/<int:product_id>")
def remove_from_cart(product_id: int):
    try:
        if "cart" in session:
            session["cart"].pop(str(product_id), None)
            session.modified = True
        flash("Продукт видалено з кошика!", "success")
        return redirect(url_for("view_cart"))
    except Exception as e:
        return render_template("error.html", error=str(e)), 400


# ✅ тимчасовий маршрут для перевірки, що товари у базі
# @app.route("/debug")
# def debug_db():
#   products = db.get_all_products()
#   return "<br>".join([f"{p['id']}: {p['name']} - {p['price']} грн" for p in products])

if __name__ == "__main__":
    app.run(debug=True)
