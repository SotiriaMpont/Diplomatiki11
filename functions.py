import mysql.connector

#Inser a Distributor to the Database


def InsertDistributor_toDatabase():
    
    #dinw timi apo ton terminal 
    value= input("Enter the name of the distributor:")
    
    #kanw connection tou python file mou me tin mydatabase
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )
     
    # ftiaxnw ton cursorako pou allilepidra me database
    cursor = mydatabase.cursor()
     
    #edw pairnei thn timi apo ton terminal kai tin bazei stin basi
    sql = "INSERT INTO Distributor (name_distributor) VALUES (%s)"
    val = (value,)
    
    # execute the SQL 
    cursor.execute(sql, val)
    
    #kanw panta ena commit 
    mydatabase.commit()

    # close the cursor and database connection
    cursor.close()
    mydatabase.close()

    print("Distributor added to the database!")

def delete_distributor_from_database():
    # Pairnw apo terminal 
    distributor_name = input("Enter the name of the distributor to delete: ")

    # sundesi me basi
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    # cursorakos
    cursor = mydatabase.cursor()

    # elegxw an uparxei ston pinaka Distributor
    sql = "SELECT * FROM Distributor WHERE name_distributor = %s"
    val = (distributor_name,)
    cursor.execute(sql, val)
    distributor = cursor.fetchone()

    # An den uparxei, ton enimerwnw apo terminal 
    if not distributor:
        print(f"Distributor {distributor_name} is not in the database!")
        cursor.close()
        mydatabase.close()
        return

    # SBHSEEEE AN YPARXEI 
    sql = "DELETE FROM Distributor WHERE name_distributor = %s"
    val = (distributor_name,)
    cursor.execute(sql, val)

    
    mydatabase.commit()
    cursor.close()
    mydatabase.close()

    print(f"Distributor {distributor_name} deleted from the database!")


                
#DOULEEEEEEEEEEEEYEI PANAGIA MOY !!!!!!!
def Dilwsi_Shift():
    # Get input from the user
    distributor_id = input("Enter the id of the distributor: ")
    date_shift = input("Enter the date (YYYY-MM-DD): ")
    hours_expected = float(input("Enter the hours that you will work: "))
    
    # Add a new parameter for ID_distributor_shift
    ID_distributor_shift = distributor_id

    active = 1
    hours_worked = 0
    Sinepeia = 0
    Total_aitimata_per_shift = 0
    
    # Connect to the MySQL database
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )
    
    cursor = mydatabase.cursor()
    
    sql = "INSERT INTO shift (date_shift, ID_distributor_shift, acceptance_rate, active, hours_expected, hours_worked, Sinepeia, Total_aitimata_per_shift) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (date_shift, ID_distributor_shift, 0, active, hours_expected, hours_worked, Sinepeia, Total_aitimata_per_shift)

    cursor.execute(sql, val)

    mydatabase.commit()

    print(cursor.rowcount, "shift added to the database!")
    print("Euxaristoume pou katoxirwses tis wres sou!")
    
    
def Kataxwrise_Aitima_database():
    #dinw timi apo ton terminal 
    value= input("dese to id tou dianomea poy thes na analabei to aitima :")
    
    #kanw connection tou python file mou me tin mydatabase
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )
     
    # ftiaxnw ton cursorako pou allilepidra me database
    cursor = mydatabase.cursor()
     
    #edw pairnei thn timi apo ton terminal kai tin bazei stin basi
    sql = "INSERT INTO Aitima (id_distr) VALUES (%s)"
    val = (value,)
    
    # execute the SQL 
    cursor.execute(sql, val)
    
    #kanw panta ena commit 
    mydatabase.commit()

    # close the cursor and database connection
    cursor.close()
    mydatabase.close()

    print("To aitima paraggelias anatethike ston distributor!")
    
    
#                DEN LEITOURGEI

def Rating_from_store():
    value1 = input("Enter the id of the distributor you want to evaluate: ")
    value2 = input("Enter the date of the delivery: ")
    value3 = input("Enter the id of the order: ")
    value4 = input("How would you rate the distributor from scale to 0-5 for that delivery? ")

    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    cursor = mydatabase.cursor()

    sql1 = "SELECT  id_distributor FROM Distributor WHERE  id_distributor=%s"
    val1 = (value1,)
    cursor.execute(sql1, val1)
    result1 = cursor.fetchall()
    
    print(result1)

    if len(result1) == 0:
        print("No distributor with this name found!")
        
        
    
    
    else:
        
        # Check if order exists
        sql2 = "SELECT id_aitimatos FROM Aitima WHERE id_aitimatos=%s"
        val2 = (value3,)
        cursor.execute(sql2, val2)
        result2 = cursor.fetchall()

        if len(result2) == 0:
            print("That specific distributor did not work on that day!")
        else:
            # Check if shift exists
            sql3 = "SELECT date_shift FROM Shift WHERE date_shift=%s"
            val3 = (value2,)
            cursor.execute(sql3, val3)
            result3 = cursor.fetchall()

            if len(result3) == 0:
                print("We cannot find the id of that specific order!")
            else:
                cursor = mydatabase.cursor()
                sql4 = "INSERT INTO RatingFromStore (id_di, dat_shift, id_aitim, Rating_store) VALUES (%s, %s, %s, %s)"
                val4 = (result1[0][0], value2, value3, value4)

                try:
                    cursor.execute(sql4, val4)
                    mydatabase.commit()
                    cursor.close()
                    mydatabase.close()
                    print("Thanks for your rating!")
                except mysql.connector.Error as error:
                    print("Failed to insert record into Rating_From_Store table {}".format(error))
                    
                    
def Rating_From_Costumer():
    
    value1 = input("Enter the id of the distributor you want to evaluate: ")
    value2 = input("Enter the date of the delivery: ")
    value3 = input("Enter the id of the order: ")
    value4 = input("How would you rate the distributor from scale to 0-5 for that delivery? ")

    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    cursor = mydatabase.cursor()

    sql1 = "SELECT  id_distributor FROM Distributor WHERE  id_distributor=%s"
    val1 = (value1,)
    cursor.execute(sql1, val1)
    result1 = cursor.fetchall()
    
    print(result1)

    if len(result1) == 0:
        print("No distributor with this name found!")
        
        
    
    
    else:
        
        # Check if order exists
        sql2 = "SELECT id_aitimatos FROM Aitima WHERE id_aitimatos=%s"
        val2 = (value3,)
        cursor.execute(sql2, val2)
        result2 = cursor.fetchall()

        if len(result2) == 0:
            print("That specific distributor did not work on that day!")
        else:
            # Check if shift exists
            sql3 = "SELECT date_shift FROM Shift WHERE date_shift=%s"
            val3 = (value2,)
            cursor.execute(sql3, val3)
            result3 = cursor.fetchall()

            if len(result3) == 0:
                print("We cannot find the id of that specific order!")
            else:
                cursor = mydatabase.cursor()
                sql4 = "INSERT INTO RatingFromCostumer (id_rating_costumer, dat_shif_costumer, id_aitimatos_costumer, Rating_costumer) VALUES (%s, %s, %s, %s)"
                val4 = (result1[0][0], value2, value3, value4)

                try:
                    cursor.execute(sql4, val4)
                    mydatabase.commit()
                    cursor.close()
                    mydatabase.close()
                    print("Thanks for your rating!")
                except mysql.connector.Error as error:
                    print("Failed to insert record into RatingFromCostumer table {}".format(error))
    