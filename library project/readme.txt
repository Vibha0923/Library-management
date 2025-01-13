# Library management System

This README file explains the functionality and structure of the "Add Book" feature in the Library Management System. This module is designed to allow users to add book details and corresponding user information into the system using a web interface built with Flask and styled with Bootstrap.

---

## Features

- A form to input book details:
  - Book Name
  - Author
  - Book Details
  - User Information (Name, Class, Number)
- Validation for required fields.
- User-friendly and modern interface using Bootstrap.
- Responsive design, ensuring compatibility across devices.

---

## Languages Used

- **Python** (Flask framework for backend development)
- **HTML** (Structure of the web pages)
- **CSS** (Styling the web pages, including Bootstrap integration)
- **SQL** (Database queries and integration with MySQL)

---

## File Structure

### `add_books.html`

The HTML template for the "Add Book" feature.

### Flask Route (`add_books`)

The `add_books` function in Flask handles the functionality for this page.

- **Route**: `/add_books`
- **Methods**: `GET`, `POST`
- **Functionality**:
  - `GET`: Renders the `add_books.html` form.
  - `POST`: Inserts the submitted data into the MySQL database and redirects the user to the homepage.

---

## Database Integration

### Table Structure (`user_details1`)

The following fields are stored in the `user_details1` table:

| Field Name   | Type                  | Description                                |
| ------------ | --------------------- | ------------------------------------------ |
| `oid`        | INT (AUTO\_INCREMENT) | Primary Key (Unique identifier for books). |
| `bk_name`    | VARCHAR               | Name of the book.                          |
| `bk_author`  | VARCHAR               | Author of the book.                        |
| `bk_details` | TEXT                  | Details of the book.                       |
| `usr_name`   | VARCHAR               | Name of the user.                          |
| `usr_class`  | VARCHAR               | User's class or grade.                     |
| `usr_num`    | VARCHAR               | User's contact number.                     |
| `usr_date`   | DATETIME              | Date of book issue (optional).             |

### SQL Query

The `add_books` route uses the following SQL query to insert data:

```sql
INSERT INTO user_details1 
(bk_name, bk_author, bk_details, usr_name, usr_class, usr_num, usr_date) 
VALUES (%s, %s, %s, %s, %s, %s, %s);
```

---

## Form Fields

The form collects the following data:

1. **Book Name** - A text input field to specify the name of the book.
2. **Author** - A text input field to specify the author's name.
3. **Book Details** - A textarea to input a brief description of the book.
4. **User Name** - A text input for the user's name.
5. **User Class** - A text input for the user's class or grade.
6. **User Number** - A text input for the user's contact number.

---

## Styling

This page is styled using [Bootstrap 5](https://getbootstrap.com/):

- **CSS:**

  - Clean layout with a light background.
  - Rounded corners and shadow for the form container.
  - Bold labels and easy-to-read font sizes.

- **JavaScript:**

  - Included Bootstrap's JavaScript bundle for potential interactive features.

---

## Instructions to Use

1. Clone the project repository.
2. Ensure you have Flask and MySQL set up in your environment.
3. Configure the database connection in the Flask app.
4. Navigate to the `/add_books` route in your browser.
5. Fill in the required form fields and click "Add Book".

---

##
