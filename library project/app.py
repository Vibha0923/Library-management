from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import datetime

app = Flask(__name__)

# DATABASE CONNECTION
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',     # Replace with your MySQL server address
        user='root', # Replace with your MySQL username
        password='2309', # Replace with your MySQL password
        database='library_database1' # Replace with your database name
    )
    return conn

# HOME PAGE
@app.route('/')
def index():
    return render_template('base.html')

# ADD BOOKS
@app.route('/add_books', methods=['GET', 'POST'])
def add_books():
    if request.method == 'POST':
        bk_id = request.form['bk_id']  # New field
        bk_name = request.form['bk_name']
        bk_author = request.form['bk_author']
        bk_details = request.form['bk_details']
        usr_name = request.form['usr_name']  # New field
        usr_class = request.form['usr_class']  # New field
        usr_num = request.form['usr_num']  # New field

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
    INSERT INTO user_details1 
    (bk_name, bk_author, bk_details, usr_name, usr_class, usr_num, usr_date) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", (bk_name, bk_author, bk_details, usr_name, usr_class, usr_num, None))


        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_books.html')


# SHOW BOOKS
@app.route('/show_books')
def show_books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Ensures the result is returned as a dictionary
    # Fetch specific columns like book details and user details
    cursor.execute("SELECT oid, bk_name, bk_author, bk_details, usr_name, usr_class, usr_num, usr_date FROM user_details1")
    books = cursor.fetchall()  # Fetch all the books with the correct columns
    cursor.close()
    conn.close()
    return render_template('show_books.html', books=books)  # Pass the books to the template



# ISSUE BOOK
@app.route('/issue_book', methods=['GET', 'POST'])
def issue_book():
    if request.method == 'POST':
        book_id = request.form['bk_id']
        usr_name = request.form['usr_name']
        usr_class = request.form['usr_class']
        usr_num = request.form['usr_num']
        date_nows = datetime.datetime.now()

        # Correct format for MySQL datetime
        usr_date = date_nows.strftime('%Y-%m-%d %H:%M:%S')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE user_details1 SET 
            usr_name = %s, usr_class = %s, usr_num = %s, usr_date = %s
            WHERE oid = %s
        """, (usr_name, usr_class, usr_num, usr_date, book_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('issue_book.html')


# REMOVE BOOK
@app.route('/remove_book', methods=['GET', 'POST'])
def remove_book():
    if request.method == 'POST':
        book_id = request.form['bk_id']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_details1 WHERE oid = %s", (book_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('remove_book.html')

if __name__ == '__main__':
    app.run(debug=True)
