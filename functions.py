import mysql.connector
import datetime

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


                
def Dilwsi_Shift():
    # sundesi me basi
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    # cursorakos
    cursor = mydatabase.cursor()
    
    #input to id tou dianomea 
    distributor_id = input("Enter the id of the distributor you want to declare a shift : ")
    
    #yparxei autos o dianomeas stin basi?
    
    sql = "SELECT id_distributor FROM Distributor WHERE id_distributor = %s"
    val = (distributor_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        print(f"The distributor with id '{distributor_id}' does not exist in the database")
    else:    
        # input imerominia
        Hmerominia = input("Enter the date (YYYY-MM-DD): ")
        date_obj = datetime.datetime.strptime(Hmerominia, '%Y-%m-%d')

        # elegxos an i hmerominia einai valid! px den thelw na balw to 1821 ws mera bardias.
        try:
            Hmerominia = datetime.datetime.strptime(Hmerominia, '%Y-%m-%d')
            if Hmerominia.year < datetime.datetime.now().year: #mono gia to etos 2021 kai panw ton afinw 
                print("Invalid year entered.")
            elif Hmerominia.month < 1 or Hmerominia.month > 12: #profanws ama baleis mina 13 d
                print("Invalid month entered.")
            elif Hmerominia.day < 1 or Hmerominia.day > 31: # 38 tou mina 
                print("Invalid day entered.")
            else:
                print("Date entered is valid.")
        except ValueError:
            print("Invalid date format entered.")
                
        #an isxioun ola ta parapanw zita kai wra enar3is/li3is  bardias apo terminal 
        # zhtaw wra enarxis
       # zhtaw wra enarxis
        wra_enarxis_shift = input("Enter the time that the shift starts (HH:MM:SS): ")
        try:
            time_obj = datetime.datetime.strptime(wra_enarxis_shift, '%H:%M:%S')
            print("Time entered is valid.")
        except ValueError:
            print("Invalid time format entered.")
                
        # zhtaw wra li3is shift 
        wra_lixis_shift = input("Enter the time that the shift ends (HH:MM:SS): ")
        try:
            time_obj = datetime.datetime.strptime(wra_lixis_shift, '%H:%M:%S')
            print("Time entered is valid.")
        except ValueError:
            print("Invalid time format entered.")
                    
        # elegxos profanws na mhn einai h wra li3is mikroteri apo thn enarxis
        start_time_obj = datetime.datetime.strptime(wra_enarxis_shift, '%H:%M:%S')
        end_time_obj = datetime.datetime.strptime(wra_lixis_shift, '%H:%M:%S')

        if start_time_obj >= end_time_obj:
            print("Error: Start time of shift must be before end time.")
        else:
            print("Shift times are valid.")
        
        #poses wres doulepse. 
        duration = end_time_obj - start_time_obj
        print(f"Shift duration is {duration}")
        
        
        #afou einai swsta, pame na ta kanoume insert stin database

        sql = "INSERT INTO Shift (date_shift, ID_distributor_shift, time_starts, time_ends, hours_expected) VALUES (%s, %s, %s, %s, %s)"
        val = (Hmerominia, result[0], wra_enarxis_shift, wra_lixis_shift, duration)

        # Execute 
        cursor.execute(sql, val)
        mydatabase.commit()

        # Gia na eimai sigouri oti egine h eggrafi stin basi
        print(cursor.rowcount, "record inserted.") 
    
def Kataxwrise_Aitima_database():
   
    # dinw timi apo ton terminal 
    value = input("Give me the id of the distributor you want to get  the request :")
    date = input("Give the date of the request (yyyy-mm-dd) :")

    # kanw connection tou python file mou me tin mydatabase
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    # ftiaxnw ton cursorako pou allilepidra me database
    cursor = mydatabase.cursor()
    
    #tsekarw an o dianomeas me auto to id uparxei sthn basi 
    
    sql = "SELECT id_distributor FROM Distributor WHERE id_distributor = %s"
    val = (value,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        print(f"The distributor with id '{value}' does not exist in the database")
    else:   
        #  # input imerominia
       

        # elegxos an i hmerominia einai valid! px den thelw na balw to 1821 ws mera bardias.
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            if date.year < datetime.datetime.now().year: #mono gia to etos 2021 kai panw ton afinw 
                print("Invalid year entered.")
            elif date.month < 1 or date.month > 12: #profanws ama baleis mina 13 d
                print("Invalid month entered.")
            elif date.day < 1 or date.day > 31: # 38 tou mina 
                print("Invalid day entered.")
            else:
                print("Date entered is valid.")
        except ValueError:
            print("Invalid date format entered.")
            
            
        #elegxos an h hmeromhnia aitimatos tairiazei me thn hmeromhnia pou exei shift o man. alliwa ti nohma exei? 
        #mhn ton afinei na kanei anathesi ama den exei bardia o dianomeas!!!!
        sql = "SELECT * FROM Shift WHERE ID_distributor_shift = %s AND date_shift = %s"
        val = (value, date)
        cursor.execute(sql, val)
        shift_result = cursor.fetchone()

        if shift_result is None:
            print(f"The distributor with id '{value}' does not have a shift on {date}! Den egine h anathesi tou aitimatos!")
        else:
            # AN OLA BAINOUN KALWS, PAME LIGO GIA TO INSERTTTTT 
            # edw pairnei thn timi apo ton terminal kai tin bazei stin basi
            sql = "INSERT INTO Aitima (id_distr, accepted, declined, date_aitimatos) VALUES (%s, 0, 0, %s)"
            val = (value, date)

            print(cursor.rowcount, "Egine anathesi ston dianomea!")   
            # execute the SQL 
            cursor.execute(sql, val)
            mydatabase.commit()
        
        

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
    value4 = input("How would you rate the distributor from scale 0-5 for the speed of the delivery? ")
    value5= input("How would you rate the distributor from scale 0-5 for the accuracy of the delivery? ")
    value6=input("How would you rate the distributor from scale 0-5 for general user experience? Was this distributor polite? ")
   

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
                sql4 = "INSERT INTO RatingFromCostumer (id_rating_costumer, dat_shif_costumer, id_aitimatos_costumer, criterion1,criterion2,criterion3) VALUES (%s, %s, %s, %s,%s,%s)"
                val4 = (result1[0][0], value2, value3, value4,value5,value6)

                try:
                    cursor.execute(sql4, val4)
                    mydatabase.commit()
                    cursor.close()
                    mydatabase.close()
                    print("Thanks for your rating!")
                except mysql.connector.Error as error:
                    print("Failed to insert record into RatingFromCostumer table {}".format(error))                   

  def Find_Sinepeia_Distributor():
    import mysql.connector

    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    value1 = input("Give the id of the distributor: ")
    value2 = input("Give me the date of the shift of the distributor with this id (YYYY-MM-DD): ")
    value3 = int(input("How many hours did the distributor work at that specific shift? "))

    cursor = mydatabase.cursor()

    sql1 = "SELECT id_distributor FROM Distributor WHERE id_distributor=%s"
    val1 = (value1,)
    cursor.execute(sql1, val1)
    result1 = cursor.fetchall()

    if len(result1) == 0:
        print("No distributor with this id found!")
    else:
        cursor = mydatabase.cursor()

        sql2 = "SELECT date_shift FROM Shift WHERE ID_distributor_shift=%s AND date_shift=%s"
        val2 = (value1, value2)
        cursor.execute(sql2, val2)
        result2 = cursor.fetchall()

        if len(result2) == 0:
            print("Distributor with that id did not work on that day!")
        else:
            cursor = mydatabase.cursor()

            sql3 = "UPDATE Shift SET hours_worked=%s WHERE ID_distributor_shift=%s AND date_shift=%s"
            val3 = (value3, value1, value2)
            cursor.execute(sql3, val3)
            mydatabase.commit()

            h_expected_query = "SELECT hours_expected FROM Shift WHERE ID_distributor_shift=%s AND date_shift=%s"
            h_expected_params = (value1, value2)
            cursor.execute(h_expected_query, h_expected_params)
            h_expected = cursor.fetchone()[0]

            if value3 == h_expected:
                sql4 = "UPDATE Shift SET sinepeia=1 WHERE ID_distributor_shift=%s AND date_shift=%s"
                val4 = (value1, value2)
                cursor.execute(sql4, val4)
                mydatabase.commit()
                print("O distributor den einai sinepis!")
            else:
                sql5 = "UPDATE Shift SET sinepeia=0 WHERE ID_distributor_shift=%s AND date_shift=%s"
                val5 = (value1, value2)
                cursor.execute(sql5, val5)
                mydatabase.commit()
                print("O distributor den einai sinepis!")

            cursor.close()
            mydatabase.close()



# briskw me basi thn mera ton distributor pou exei to kalutero rating apo katastima kai tous kanw ranking!
def Find_Best_Distributors_of_the_day_Rating_Store():
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    # pairnw imeromhnia terminal 
    hmeromhnia = input("Enter the date (YYYY-MM-DD): ")

    
    cursor = mydatabase.cursor()
    sql = "SELECT date_shift FROM Shift WHERE date_shift = %s"
    val = (hmeromhnia,)
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if len(result) == 0: # elegxos. Den uparxei shift me auth thn hmerominia 
        print("Den vrethike bardia me auth thn hmerominia!")
    else:
        # Gia kathe dianomea pou eixe bardia auth thn hmeromhnia bres to meso oro apo to rating tou gia na breis ton kalitero 
        sql1 = "SELECT id_di, AVG(Rating_store) FROM RatingFromStore JOIN Distributor ON RatingFromStore.id_di = Distributor.id_distributor JOIN Shift ON RatingFromStore.dat_shift = Shift.date_shift WHERE Shift.date_shift = %s GROUP BY id_di"
        val1 = (hmeromhnia,)
        cursor.execute(sql1, val1)
        results = cursor.fetchall()

        # kanw tous distributors ranking basi tou mesou orou tous kai tous apothikeuw stin basi
        ranked_results = sorted(results, key=lambda x: x[1], reverse=True)[:10]
        for i, result in enumerate(ranked_results):
            distributor_id = result[0]
            avg_rating = result[1]
            print(f"{i+1}. Distributor {distributor_id} has an average rating of {avg_rating:.2f}")
            update_sql = "UPDATE RatingFromStore SET ranking = %s WHERE dat_shift = %s AND id_di = %s"
            update_val = (i+1, hmeromhnia, distributor_id)
            cursor.execute(update_sql, update_val)

        mydatabase.commit()
        print("Ranking based on the average of the rating the got from store that day!")

    cursor.close()
    mydatabase.close()



def Find_Best_Distributors_of_the_day_Rating_Costumer():
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    # pairnw imeromhnia terminal 
    hmeromhnia = input("Enter the date (YYYY-MM-DD): ")

    
    cursor = mydatabase.cursor()
    sql = "SELECT date_shift FROM Shift WHERE date_shift = %s"
    val = (hmeromhnia,)
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if len(result) == 0: # elegxos. Den uparxei shift me auth thn hmerominia 
        print("Den vrethike bardia me auth thn hmerominia!")
    else:
        # Gia kathe dianomea pou eixe bardia auth thn hmeromhnia bres to meso oro apo to rating tou gia na breis ton kalitero 
        
        sql1 = "SELECT id_rating_costumer, AVG(Rating_costumer) FROM RatingFromCostumer JOIN Distributor ON RatingFromCostumer.id_rating_costumer = Distributor.id_distributor JOIN Shift ON RatingFromCostumer. dat_shif_costumer = Shift.date_shift WHERE Shift.date_shift = %s GROUP BY id_rating_costumer"
        val1 = (hmeromhnia,)
        cursor.execute(sql1, val1)
        results = cursor.fetchall()
        # kanw tous distributors ranking basi tou mesou orou tous kai tous apothikeuw stin basi
        ranked_results = sorted(results, key=lambda x: x[1], reverse=True)[:10]
        for i, result in enumerate(ranked_results):
            distributor_id = result[0]
            avg_rating = result[1]
            print(f"{i+1}. Distributor {distributor_id} has an average rating of {avg_rating:.2f}")
            update_sql = "UPDATE RatingFromCostumer SET ranking_costumer = %s WHERE  dat_shif_costumer = %s AND id_rating_costumer = %s"
            update_val = (i+1, hmeromhnia, distributor_id)
            cursor.execute(update_sql, update_val)

        mydatabase.commit()
        print("Ranking based on the average of the rating the got from costumers that day!")

    cursor.close()
    mydatabase.close()
    
    
def Apodoxi_Aitimatos_Distributor(): 
    
    
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    cursor = mydatabase.cursor()
    
    #pairnw apo terminal id distributor kai aitimatos 
    id1 = input("Dwse mou to id tou distributor: ")
    id_aitimatos1 = input("Dwse to id tis paraggelias pou exei anatethei ston distributor: ")
    date_input = input("Dwse tin imerominia tis paraggelias (YYYY-MM-DD): ")
    time_input = input("Dwse tin ora tis paraggelias (HH:MM:SS): ")

    # check if date is valid
    try:
        date_input = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    # check if time is valid
    try:
        time_input = datetime.datetime.strptime(time_input, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return

    # check if shift exists for the given date and distributor
    sql_shift = "SELECT time_starts, time_ends FROM Shift WHERE date_shift = %s AND ID_distributor_shift = %s"
    val_shift = (date_input, id1)
    cursor.execute(sql_shift, val_shift)
    shift_result = cursor.fetchone()

    if shift_result is None:
        print("Invalid distributor or order ID or date.")
        return

    shift_start = datetime.datetime.strptime(str(shift_result[0]), "%H:%M:%S")
    shift_end = datetime.datetime.strptime(str(shift_result[1]), "%H:%M:%S")

    if time_input < shift_start or time_input > shift_end:
        print("The order was not placed during the distributor's shift.")
        return
    
    sql_aitima = "SELECT id_distr, id_aitimatos FROM Aitima WHERE id_distr = %s AND id_aitimatos = %s"
    val_aitima = (id1, id_aitimatos1)
    
    cursor.execute(sql_aitima, val_aitima)
    aitima_result = cursor.fetchone()
    
    if aitima_result is None:
        print("Invalid distributor or order ID.")
        return
    else:
        value = input("Enter 1 if the distributor will accept the order, else type 0: ")
        
        #elegxos an dinw apo terminal swstes times 
        if value not in ["0", "1"]:
            print("Please enter 0 for decline or 1 for acceptance!")
            return
        
        accepted = "1" if value == "1" else "0"
        declined = "1" if value == "0" else "0"
        
        sql_update = "UPDATE Aitima SET accepted = %s, declined = %s, time_aitimatos = %s WHERE id_distr = %s AND id_aitimatos = %s"
        val_update = (accepted, declined, time_input, id1, id_aitimatos1)
        
        cursor.execute(sql_update, val_update)
        mydatabase.commit()
        
        print("Order status updated.")
            
    
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    #terminal hmeromhnia kai id distributor 
    hmeromhnia = input("Enter the date (YYYY-MM-DD): ")
    id1 = input("Enter the id of the distributor: ")

    cursor = mydatabase.cursor()

    # metraw accepted and declined requests
    sql = "SELECT COUNT(*) FROM Aitima WHERE id_distr = %s AND accepted = 1 AND EXISTS (SELECT * FROM Shift WHERE Shift.ID_distributor_shift = %s AND Shift.date_shift = %s)"
    val = (id1, id1, hmeromhnia)
    cursor.execute(sql, val)
    accepted_count = cursor.fetchone()[0]

    sql = "SELECT COUNT(*) FROM Aitima WHERE id_distr = %s AND accepted = 0 AND EXISTS (SELECT * FROM Shift WHERE Shift.ID_distributor_shift = %s AND Shift.date_shift = %s)"
    val = (id1, id1, hmeromhnia)
    cursor.execute(sql, val)
    declined_count = cursor.fetchone()[0]

    # briskw acceptance rate 
    if declined_count == 0:
        acceptance_rate = 1
    else:
        acceptance_rate = accepted_count / (declined_count + accepted_count)

    # bazw to acceptance rate sto table Shift afou prwta to ypologisa
    sql = "UPDATE Shift SET acceptance_rate = %s WHERE date_shift = %s AND ID_distributor_shift = %s"
    val = (acceptance_rate, hmeromhnia, id1)
    cursor.execute(sql, val)

    mydatabase.commit()
    print(cursor.rowcount, "Eggrapsa sthn bash!!!!!")


def Find_Acceptance_rate_perShift():
    
    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    #terminal hmeromhnia kai id distributor 
    hmeromhnia = input("Enter the date (YYYY-MM-DD): ")
    id1 = input("Enter the id of the distributor: ")

    cursor = mydatabase.cursor()

    # metraw accepted and declined requests
    sql = "SELECT COUNT(*) FROM Aitima WHERE id_distr = %s AND accepted = 1 AND hmeromhnia_aitimatos=%sAND EXISTS (SELECT * FROM Shift WHERE Shift.ID_distributor_shift = %s AND Shift.date_shift = %s)"
    val = (id1, hmeromhnia, id1, hmeromhnia)
    cursor.execute(sql, val)
    accepted_count = cursor.fetchone()[0]

    sql = "SELECT COUNT(*) FROM Aitima WHERE id_distr = %s AND accepted = 0 AND hmeromhnia_aitimatos=%s AND EXISTS (SELECT * FROM Shift WHERE Shift.ID_distributor_shift = %s AND Shift.date_shift = %s)"
    val = (id1, hmeromhnia, id1, hmeromhnia)
    cursor.execute(sql, val)
    declined_count = cursor.fetchone()[0]

    # briskw acceptance rate 
    if declined_count == 0:
        acceptance_rate = 1
    else:
        acceptance_rate = accepted_count / (declined_count + accepted_count)

    # bazw to acceptance rate sto table Shift afou prwta to ypologisa
    sql = "UPDATE Shift SET acceptance_rate = %s WHERE date_shift = %s AND ID_distributor_shift = %s"
    val = (acceptance_rate, hmeromhnia, id1)
    cursor.execute(sql, val)

    mydatabase.commit()
    print("Accepted: ",cursor.rowcount, "Eggrapsa sto acceptance_rate tou shift to ",acceptance_rate)
    

    
 def Best_Distributor_Acceptance_Rate():
    
 

    mydatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="mydatabase"
    )

    cursor = mydatabase.cursor()

    # Terminal hmeromhnia
    hmeromhnia = input("Enter the date (YYYY-MM-DD): ")

    # Update SELECT statement to calculate ranking
    sql = "SELECT ID_distributor_shift, acceptance_rate, ROW_NUMBER() OVER (ORDER BY acceptance_rate DESC) AS ranking FROM Shift WHERE date_shift = %s LIMIT 10"
    val = (hmeromhnia,)
    cursor.execute(sql, val)

    # Fetch results and insert into BestDistributors table
    rows = cursor.fetchall()
    for row in rows:
        distributor_id = row[0]
        acceptance_rate = row[1]
        ranking = row[2]

        # Insert values into BestDistributors table
        sql = "INSERT INTO BestDistributors (hmera_best, Id_best_distributor, Ranking_best_AccepRate) VALUES (%s, %s, %s)"
        val = (hmeromhnia, distributor_id, ranking)
        cursor.execute(sql, val)
        mydatabase.commit()

    # Print results to console
    print(f"Top 10 distributors with the highest acceptance rates on {hmeromhnia}:\n")
    print("('Distributor ID', 'Acceptance Rate', 'Ranking_Accep_Rate')")
    for row in rows:
        print((row[0], row[1], row[2]))

    # Close the database connection
    mydatabase.close()   
    
