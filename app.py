import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

import numpy as np
import pandas as pd
df = pd.read_excel('indicators.xlsx')
df=df.round(3)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


st.title("World Development Indicators")


countries=['Germany',
    'France',
    'United States',
    'United Kingdom',
    'Malaysia',
    'India',
    'China',
    'Japan',
    'Spain',
    'East Asia & Pacific',
    'Europe & Central Asia',
    'Latin America & Caribbean',
    'Sub-Saharan Africa']

seriesName=['GDP per capita (current US$)',
             'GDP growth (annual %)',
             'Imports of goods and services (current US$)',
             'Manufacturing, value added (% of GDP)',
             'Trade (% of GDP)',
             'Forest area (% of land area)',
             'Forest area (sq. km)',
             'Life expectancy at birth, total (years)',
             'Population growth (annual %)',
             'CO2 emissions (kg per 2010 US$ of GDP)',
             'Agriculture, forestry, and fishing, value added (% of GDP)'   ]
        

    

navigate_button = st.sidebar.radio("Select The Page to View", ('Display DataFrames','Compare Countries', 'Statistical Analysis')) 

if navigate_button=='Display DataFrames':
    st.header('Data Frame')
    select_event = st.selectbox('Select series to show the dataframe?',
                                        seriesName)

    dfa=df.loc[(df.SeriesName == select_event),[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]]
    dfa=dfa.T
    dfa.columns=countries
    dfa = dfa.reset_index()
    dfa=dfa.rename(columns={"index": "year"})
    dfa.set_index('year',inplace=True)
    st.write(dfa)

elif navigate_button=='Compare Countries':

   
    st.header('Compare Countries')

    option = st.multiselect('What countries do you want to compare?', countries, countries[0])
    select_event = st.selectbox('Select series to compare?',
                                        seriesName)

    
    


    dfa=df.loc[(df.SeriesName == select_event),[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]]
    dfa=dfa.T
    dfa.columns=countries
    dfa = dfa.reset_index()

   


    multi_lc = alt.Chart(dfa).transform_fold(
        option,
        ).mark_line().encode(
        x='index:Q',
        y=alt.Y('value:Q', title=''),
        color='key:N'
        
        
    ).properties(
        title=select_event,
        width=600,
        height=400
    ).interactive()
    if(len(option)==0):
            st.line_chart(dfa)
    else:
        st.write( multi_lc )


elif navigate_button=='Statistical Analysis':
    st.header("Statistical Analysis")
    


    select_event = st.selectbox('Select series to show stats?',
                                        seriesName)

    dfa=df.loc[(df.SeriesName == select_event),[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]]
    dfa=dfa.T
    dfa.columns=countries
    dfa = dfa.reset_index()
    countryName = st.selectbox('Choose country  to show stats?',
                                        countries)
    st.write( dfa.agg({countryName: ['min', 'max', 'mean', 'median']}) )




 
    

    

