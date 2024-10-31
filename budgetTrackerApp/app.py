from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize database connection
def init_db():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY,
                        type TEXT,
                        amount REAL,
                        category TEXT
                      )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_income = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expenses = cursor.fetchone()[0] or 0
    conn.close()

    remaining_balance = total_income - total_expenses
    return render_template('index.html', transactions=transactions, total_income=total_income, total_expenses=total_expenses, remaining_balance=remaining_balance)

@app.route('/add', methods=['POST'])
def add():
    transaction_type = request.form['type']
    amount = float(request.form['amount'])
    category = request.form['category']

    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (type, amount, category) VALUES (?, ?, ?)",
                   (transaction_type, amount, category))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
