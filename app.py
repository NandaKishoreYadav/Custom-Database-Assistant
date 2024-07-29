import streamlit as st
from helper import init_database,get_response
from langchain_core.messages import AIMessage,HumanMessage

if 'start' not in st.session_state:
    st.session_state.start=False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
      AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database."),
    ]

st.set_page_config(page_title="Custom DataBase Assistant",page_icon='💻')
st.title("Custom DataBase Assistant")
with st.sidebar:
    st.subheader("Settings")
    st.write('Connect to your MySQL DataBase')
    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User", value="root", key="User")
    st.text_input("Password", type="password", value="root", key="Password")
    st.text_input("Database", value="atliq_tshirts", key="Database")

    if st.button("Connect"):
        with st.spinner("Connecting to database..."):
            db = init_database(
                st.session_state["User"],
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"]
            )
            st.session_state.db = db
            st.success("Connected to database!")
            st.session_state.start = True

if st.session_state.start == False :
    st.info("Please Connect with your SQL DataBase")
else:
    for message in st.session_state.chat_history:
        if isinstance(message,HumanMessage):
            with st.chat_message("Human"):
                st.markdown(message.content)
        elif isinstance(message,AIMessage):
            with st.chat_message("AI"):
                st.markdown(message.content)

    user_query = st.chat_input("Type a message...")
    if user_query is not None and user_query!='':
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        response = get_response(user_query, st.session_state.db, st.session_state.chat_history)

        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            st.markdown(response)

        st.session_state.chat_history.append(AIMessage(content=response))