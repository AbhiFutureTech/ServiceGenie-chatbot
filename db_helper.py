import mysql.connector


mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pandeyji_eatery"
)

def get_order_status(order_id: int):
    # Create a cursor object
    mycursor = mydb.cursor()

    # Write the SQL query
    query = ("SELECT status FROM order tracking WHERE order_id = %s")

    # Execute the query
    mycursor.execute('SELECT * FROM pandeyji_eatery.food_items')

    #Fetch the result
    result = mycursor.fetchone()

    #close the cursor and connection
    cursor.close()
    cnx.close()

    if result is not None:
        return result[0]
    else:
         return None
