# import mysql database module
import pymysql as mq

# database connection
mysql_conn = mq.connect(host="localhost",port=8088,user="root",password="",database="employeeDB")

# open cursor
cursor = mysql_conn.cursor()

while True:
    ch = int(input(
        '''
        Which operation you want to perform? 
        1 add employee
        2 display all employee
        3 display employee by id
        4 delete employee by id
        5 update employee by id
        6 Exit
        '''
    ))

    if ch == 1:
        e_name = input("Enter employee name:-")
        e_email = input("Enter employee email:-")
        e_phone = input("Enter employee phone:-")
        e_designation = input("Enter employee designation:-")
        e_salary = input("Enter employee salary:-")
        try:
            # add employee
            add = "INSERT INTO employee(e_name,e_email,e_phone,e_designation,e_salary) VALUES(%s, %s, %s, %s, %s)"

            data = (e_name,e_email,e_phone,e_designation,e_salary)

            # execute insert query
            cursor.execute(add,data)

            # commit(save) changes
            mysql_conn.commit()

            print("Employee added successfully")

        except Exception as e:
            print("Error in adding employee")
            print(e)


    elif ch == 2:
        try:
            # display all employee
            displayall = "SELECT * FROM employee"

            # execute select query
            cursor.execute(displayall)

            # fetchall
            records = cursor.fetchall()

            print("__________________________________________________________________________________________________________________________")
            print("{:<15}| {:<15}| {:<20}| {:<20}| {:<25}| {:<20}".format("Employee ID","Employee Name","Employee Email","Employee Phone","Employee Designation","Employee Salary"))
            print("__________________________________________________________________________________________________________________________")
            for i in records:
                print("{:<15}| {:<15}| {:<20}| {:<20}| {:<25}| {:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
            print("__________________________________________________________________________________________________________________________")
        except Exception as e:
            print("Error in displaying employee")
            print(e)   
    
    elif ch == 3:
        try:
            e_id = input("Enter employee id you want to display:-")
            
            # display single record
            displayone = "SELECT * FROM employee WHERE e_id="+e_id

            # execute select query
            cursor.execute(displayone)

            # fetchall
            record = cursor.fetchone()

            print("__________________________________________________________________________________________________________________________")
            print("{:<15}| {:<15}| {:<20}| {:<20}| {:<25}| {:<20}".format("Employee ID","Employee Name","Employee Email","Employee Phone","Employee Designation","Employee Salary"))
            print("__________________________________________________________________________________________________________________________")
            print("{:<15}| {:<15}| {:<20}| {:<20}| {:<25}| {:<20}".format(record[0],record[1],record[2],record[3],record[4],record[5]))

        except Exception as e:
            print("Error in displaying employee")
            print(e) 
    
    elif ch == 4:
        try:
            delete_id = input("Enter employee id you want to delete:-")
            
            # delete record
            delete = "DELETE FROM employee WHERE e_id=%s"
        
            # execute delete query
            cursor.execute(delete,delete_id)

            # commit(save) changes
            mysql_conn.commit()

            print("Employee deleted successfully")
        
        except Exception as e:
            print("Error in deleting employee")
            print(e)

    elif ch == 5:
        while True:
            updatech = int(input(
                '''
                Which field you want to update?
                1 Name
                2 Email
                3 Phone
                4 Designation
                5 Salary
                6 Don't want to update
                '''
            ))

            if updatech == 1:
                try:
                    update_id = input("Enter employee id you want to update name:-")
                    update_ename = input("Enter employee name:-")

                    # update employee name
                    updateEname = "UPDATE employee SET e_name=%s WHERE e_id=%s"
                    en = (update_ename,update_id)

                    # execute update name query
                    cursor.execute(updateEname,en)

                    # commit(save) changes
                    mysql_conn.commit()

                    print("Employee name updated successfully")

                except Exception as e:
                    print("Error in updating employee name")
                    print(e) 

            elif updatech == 2:
                try:
                    update_id = input("Enter employee id you want to update email:-")
                    update_eemail = input("Enter employee email:-")

                    # update employee email
                    updateEemail = "UPDATE employee SET e_email=%s WHERE e_id=%s"
                    ee = (update_eemail,update_id)

                    # execute update email query
                    cursor.execute(updateEemail,ee)

                    # commit(save) changes
                    mysql_conn.commit()

                    print("Employee email updated successfully")

                except Exception as e:
                    print("Error in updating employee email")
                    print(e) 

            elif updatech == 3:
                try:
                    update_id = input("Enter employee id you want to update phone:-")
                    update_ephone = input("Enter employee phone:-")

                    # update employee phone
                    updateEphone = "UPDATE employee SET e_phone=%s WHERE e_id=%s"
                    ep = (update_ephone,update_id)

                    # execute update phone query
                    cursor.execute(updateEphone,ep)

                    # commit(save) changes
                    mysql_conn.commit()

                    print("Employee phone updated successfully")

                except Exception as e:
                    print("Error in updating employee phone")
                    print(e) 

            elif updatech == 4:
                try:
                    update_id = input("Enter employee id you want to update designation:-")
                    update_edesignation = input("Enter employee designation:-")

                    # update employee designation
                    updateEdesignation = "UPDATE employee SET e_designation=%s WHERE e_id=%s"
                    ed = (update_edesignation,update_id)

                    # execute update designation query
                    cursor.execute(updateEdesignation,ed)

                    # commit(save) changes
                    mysql_conn.commit()

                    print("Employee designation updated successfully")

                except Exception as e:
                    print("Error in updating employee designation")
                    print(e) 

            elif updatech == 5:
                try:
                    update_id = input("Enter employee id you want to update salary:-")
                    update_esalary = input("Enter employee salary:-")

                    # update employee salary
                    updateEsalary = "UPDATE employee SET e_salary=%s WHERE e_id=%s"
                    es = (update_esalary,update_id)

                    # execute update salary query
                    cursor.execute(updateEsalary,es)

                    # commit(save) changes
                    mysql_conn.commit()

                    print("Employee salary updated successfully")

                except Exception as e:
                    print("Error in updating employee salary")
                    print(e) 

            elif updatech == 6:
                break
    
            else:
                print("Enter a valid choice")

    
    elif ch == 6:
        break
    
    else:
        print("Enter a valid choice")