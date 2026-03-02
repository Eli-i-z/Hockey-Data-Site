import streamlit as st
import statCalculator as calc
import plotly_express as px

if 'stage' not in st.session_state:
    st.session_state['stage'] = 0


positionGoalData = {'goals':[calc.getDefensiveGoals(),calc.getOffensiveGoals()],'position':['Defense','Offense']}
capitaGoalData = {'goals per capita':[calc.getDefensiveGoals()/calc.getDefensivePlayers(),calc.getOffensiveGoals()/calc.getOffensivePlayers()],'position':['Defense','Offense']}
capitaAssistData = {'assists per capita':[calc.getDeffensiveAssists()/calc.getDefensivePlayers(),calc.getOffensiveAssists()/calc.getOffensivePlayers()],'position':['Defense','Offense']}

original = px.pie(positionGoalData, values='goals', names='position', title='Offensive Goals vs Defensive Goals')
perCapita = px.pie(capitaGoalData, values='goals per capita', names='position', title='Offensive Goals vs Defensive Goals')
assists = px.pie(capitaAssistData, values='assists per capita', names='position', title='Offensive Assists vs Defensive Assists')

if st.session_state['stage'] == 0:
    st.text('Which position in hockey do you think scores more goals, offense or defense?')

if st.session_state['stage'] == 0:
    if st.button('click to find out'):
        st.session_state['stage'] = 1
        st.rerun()
if st.session_state['stage'] == 1:
        st.plotly_chart(original)
        st.text("okay.. so it's not even close. Offensive players score way more goals, however, it's still not fair. Lets even out the statistics so that it's based on a per capita")
if st.session_state['stage'] == 1:
    if st.button('see per capita'):
        st.session_state['stage'] = 2
        st.rerun()
if st.session_state['stage'] == 2:
    st.plotly_chart(perCapita)
    st.text("well that helped a little bit. Allthough it would make sense for offensive players to score more goals than defensive players. Offensive players on average score about 3x more goals than defensive players. Now lets look at assists.")
    if st.button('see assists'):
        st.session_state['stage'] = 3
        st.rerun()
if st.session_state['stage'] == 3:
    st.plotly_chart(assists)
    st.text("okay so assists are much closer than goals. These graphs clearly show that offensive players have an easier time gaining points in hockey than defensive players. This makes defensive players who have a lot of points be very imperessive. For example Evan Boucard is in the top ten players for points this season, as a defender. With the statistics shown earlier this becomes very impressive.")
