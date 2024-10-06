import streamlit
import streamlit as st

st.header('wassup' , divider="violet")
st.subheader('''
             Not sure how you've been doing recently but, i hope everything went well for you''')
import time
time.sleep(1)
st.write("Though im not sure what to do")
import time
time.sleep(3)
st.write('But still im sure everything will become normal someday')
import time
time.sleep(2)
st.write('Its just not you that is going through this state, everybody else takes turn too silly')
import time
time.sleep(2)
st.write('Do you think you know what you are doing right now?')
import time
time.sleep(1)
choice = st.radio("Choose One Darling", ["Yes,I Do", "No, I Dont"])
if choice == 'Yes,I Do':
    st.write('Then why not do it now right?')
else:
    st.write('Awww, i dont think ill be able to help much but here is some kitties picture for you')
    import time
    time.sleep(2)
    st.image("https://i.pinimg.com/564x/ea/5b/30/ea5b303fbb727e71f12f76e2038cfdf3.jpg", caption="like i said it is kitties :3")
    import time
    time.sleep(4)
    st.write('So? Is it cute?')
    time.sleep(1)
    choice = st.radio('Choose carefully peasant...', ['IT IS SO CUTEEEE', 'nah its not that cute/ im a dog person'])
if choice == 'IT IS SO CUTEEEE':
    st.write('Just like you cutie🌷')
else:
 st.write('how dare u nig-... ahem i mean peasant it is cute okay')
time.sleep(2)
st.write('anyway back to our main topic here')
time.sleep(2)
st.write('so im gonna ask you some questions alright?')
time.sleep(2)
choice = st.radio('Do you have a problem in life?', ['Yes', 'No'])
if choice == 'Yes':
    st.write('Hmmm')
else:
   st.write('I see....')
genre = st.radio('Can you do anything about it', ['Yes', 'No'])
if genre == 'Yes':
    st.write('Then Why Worry')
else:
   st.write('Then Why Worry')
time.sleep(2)
st.write('Anyway thank you for answering even though its quite short')
time.sleep(1)
st.write('Im thankful')
st.image("https://i.pinimg.com/564x/fc/97/34/fc973460640f23260b51dc8f037547a7.jpg", caption="Love U <3")
