## import libraries
import pandas as pd
import streamlit as st
import pickle
import numpy as np

model=pickle.load(open(r"titanic_v0.pkl",'rb'))     ## Load pickeled ml model

## Main Function
def main():
    """ main() contains all UI structure elements; getting and storing user data can be done within it"""
    st.title("Titanic Survival Prediction")                                                                              ## Title/main heading
    st.image(r"titanic_sinking.jpg", caption="Sinking of 'RMS Titanic' : 15 April 1912 in North Atlantic Ocean",use_column_width=True) ## image import
    st.write("""## Would you have survived From Titanic Disaster?""")                                                    ## Sub heading

    ## Side Bar Configurations
    st.sidebar.header("More Details:")
    st.sidebar.markdown("[For More facts about the Titanic here](https://www.telegraph.co.uk/travel/lists/titanic-fascinating-facts/#:~:text=1.,2.)")
    st.sidebar.markdown("[and here](https://titanicfacts.net/titanic-survivors/)")
    st.title("-----          Check Your Survival Chances          -----")

    ## Framing UI Structure
    age = st.slider("Enter Age :", 1, 75, 30)                                                                  # slider for user input(ranges from 1 to 75 & default 30)

    fare = st.slider("Fare (in 1912 $) :", 15, 500, 40)                                                        # slider for user input(ranges from 15 to 500 & default 40)

    SibSp = st.selectbox("How many Siblings or spouses are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8]) # Select box

    Parch = st.selectbox("How many Parents or children are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8]) # Select box

    sex = st.selectbox("Select Gender:", ["Male","Female"])                         # select box for gender[Male|Female]
    if (sex == "Male"):                                                             # selected gender changes to [Male:0 Female:1]
        Sex=0
    else:
        Sex=1

    Pclass= st.selectbox("Select Passenger-Class:",[1,2,3])                        # Select box for passenger-class

    boarded_location = st.selectbox("Boarded Location:", ["Southampton","Cherbourg","Queenstown"]) ## Select Box for Boarding Location
    Embarked_C,Embarked_Q,Embarked_S=0,0,0                     # initial values are 0
    # As we encoded these using one-hot-encode im ml model; so if 'Q' selected value is C=0,Q=1;S=0 , if 'S' selected value is C=0,Q=0;S=1 likewise
    if boarded_location == "Queenstown":
        Embarked_Q=1
    elif boarded_location == "Southampton":
        Embarked_S=1
    else:
        Embarked_C=1

    ## Getting & Framing Data: Collecting user-input into dictionary
    data={"Age":age,"Fare":fare,"SibSp":SibSp,"Parch":Parch,"Sex":Sex,"Pclass":Pclass,"Embarked_Q":Embarked_Q,"Embarked_S":Embarked_S,"Embarked_C":Embarked_C}

    df=pd.DataFrame(data,index=[0])      ## converting dictionary to Dataframe
    return df

data=main()                             ## calling Main()

## Prediction:
if st.button("Predict"):                                                                ## prediction button created,which returns predicted value from ml model(pickle file)
    result = model.predict(data)                                                        ## prediction of user-input
    proba=model.predict_proba(data)                                                     ## probabilty prediction of user-input
    #st.success('The output is {}'.format(result))

    if result[0] == 1:
        st.write("***congratulation !!!....*** **You probably would have made it!**")
        st.image(r"lifeboat.jfif")
        st.write("**Survival Probability Chances :** 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))
    else:
        st.write("***Better Luck Next time !!!!...*** **you're probably Ended up like 'Jack'**")
        st.image(r"Rip.jfif")
        st.write("**Survival Probability Chances :** 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))

## Working Button:
if st.button("Working"):                                                      # creating Working button, which gets some survival tips & info.
    st.write("""# How's prediction Working :- Insider Survival Facts and Tips: 
             - Only about `32%` of passengers survived In this Accident\n
             - Ticket price:
                    1st-class: $150-$435 ; 2nd-class: $60 ; 3rd-class: $15-$40\n
             - About Family Factor:
                If You Boarded with atleast one family member `51%` Survival rate
               """)
    st.image(r"gr.PNG")

## Author Info.
if st.button("Author"):
    st.write("## @ Anil")