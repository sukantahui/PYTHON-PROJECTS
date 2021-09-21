import streamlit as st


def create_text_file(data):
    f = open("python.txt","w")
    f.write(data)
    f.close()



st.title("Registration form")
first,last = st.columns(2)

first.text_input("First Name")
last.text_input("Last Name")

email,mob = st.columns([3,1])
email.text_input("Email ID")
mob.text_input("Mobile number")

user,pw,pw2 = st.columns(3)
user_name = user.text_input("User Name")
pw.text_input("Password",type="password")
pw2.text_input("Confirm Password",type="password")

ch,bl,sub = st.columns(3)
ch.checkbox("I agree")

submit = sub.button("Submit")

if submit:
    st.write(user_name)
    create_text_file(user_name)

