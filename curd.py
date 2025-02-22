import mysql.connector
import streamlit as st

#Establish a connection to  Mysql Server

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="crud_new1"
)

mycursor=mydb.cursor()
print("Connection Established")

# Create Streamlit App

def main():
    st.title("CURD Operation with mysql")

    #Display option for curd Operation

    option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))

    # Perform Selected CRUD Operations
    if option=="Create":
        st.subheader("Create a Record")
        name=st.text_input("Enter a name")
        email=st.text_input("Enter a email")
        if st.button("Create"):
            sql="insert into users(name,email) values(%s,%s) "
            val=(name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully")

    elif option=="Read":
        st.subheader("Read  Records")
        mycursor.execute("select * from users")
        result=mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option=="Delete":
        st.subheader("Delete a Record")
        id=st.number_input("Enter ID",min_value=1)
        if st.button("Delete"):
            sql="delete from users where id=%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Deleted Sucessfilly")

    elif option=="Update":
        st.subheader("Update a Record")
        id=st.number_input("Enter ID",min_value=1)
        name=st.text_input("Enter a New Name")
        email=st.text_input("Enter a new Email")
        if st.button("Update"):
            sql="update users set name=%s,email=%swhere id=%s"
            val=(name,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Recor Updated Sucessfully")









if __name__=="__main__"    :
    main()