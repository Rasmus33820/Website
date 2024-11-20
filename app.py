from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Mock product data
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1000, 'category': 'electronics'},
    {'id': 2, 'name': 'Headphones', 'price': 200, 'category': 'electronics'},
    {'id': 3, 'name': 'T-Shirt', 'price': 25, 'category': 'clothing'},
    {'id': 4, 'name': 'Jeans', 'price': 40, 'category': 'clothing'},
    {'id': 5, 'name': 'Coffee Mug', 'price': 15, 'category': 'home'},
    {'id': 6, 'name': 'Sofa', 'price': 500, 'category': 'home'}
]

# Home page route
@app.route('/')
def home():
    return render_template('index.html', products=products)

# Add item to cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((item for item in products if item['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('home'))

# View cart page
@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

# Checkout page (simple)
@app.route('/checkout')
def checkout():
    cart = session.get('cart', [])
    if not cart:
        return redirect(url_for('home'))
    return render_template('checkout.html', cart=cart)

# Filter products by category
@app.route('/filter/<category>')
def filter_products(category):
    filtered_products = [product for product in products if product['category'] == category]
    return render_template('index.html', products=filtered_products)

if __name__ == '__main__':
    app.run(debug=True)
