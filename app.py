import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np








df = pd.read_excel('indicators.xlsx')
df=df.round(3)
pd.set_option('display.float_format', lambda x: '%.3f' % x)





html_string = "<h1>World Development Indicators</h1>"

st.markdown(html_string, unsafe_allow_html=True)





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
        

    

navigate_button = st.sidebar.radio("Select The Page to View", ('GDP World view','Compare Countries', 'Sun Burst','Statistical Analysis','Comparisons')) 

if navigate_button=='GDP World view':

   
    
    compare_GDP = st.radio("Select type to compare", ('GDP growth (annual %)','GDP per capita (current US$)')) 
    selected_series='GDP growth (annual %)'
    if compare_GDP=='GDP growth (annual %)':
        selected_series='GDP growth (annual %)'
    else:
        selected_series='GDP per capita (current US$)'
    df_gdp = pd.read_excel('gdp.xlsx')
    df_gdp=df_gdp.loc[df_gdp['Series Name'] == selected_series]




    year_select = st.select_slider('Select a Year',
    options=['YR2006','YR2007','YR2008','YR2009','YR2010','YR2011','YR2012','YR2013','YR2014','YR2015','YR2016','YR2017','YR2018','YR2019'])
    st.write('Selected Year : ', year_select)




   


   
    fig = go.Figure(data=go.Choropleth(
        locations = df_gdp['Country Code'],
        z = df_gdp[year_select],
        text = df_gdp['Country Name'],
        colorscale = 'Blues',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix = '$',
        colorbar_title = selected_series,
    ))
    fig.update_layout(
    title_text=selected_series,
    autosize=False,
    width=800,
    height=600,
    
    geo=dict(
        showframe=True,
        showcoastlines=True,
        projection_type='equirectangular'
    ))

    st.write(fig)

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


elif navigate_button=='Sun Burst':
    st.header("Sun Burst")
    df = pd.read_excel('indicators.xlsx')
    df=df.round(3)
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    edf = pd.melt(df,id_vars=['SeriesName','CountryName'], value_vars=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2018])
    countries = edf['CountryName'].unique()
    series = edf['SeriesName'].unique()
    year = edf['variable'].unique()
    select_event = st.selectbox('Select series to show the dataframe?',series)
    select_year = st.selectbox('Select year to show the dataframe?',year)
    edf2 = pd.melt(df,id_vars=['SeriesName','CountryName'], value_vars=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2018])
    edf2=edf2.loc[edf2.SeriesName == select_event]
    edf2=edf2.loc[edf2.variable == select_year]
    edf2.dropna()
    edf2["value"]=pd.to_numeric(edf2["value"])
    edf2["variable"]=pd.to_numeric(edf2["variable"])
    fig=px.sunburst(edf2, path=['variable','CountryName','SeriesName'], values='value', width=1000,height=800,hover_name="CountryName", hover_data={'value':True})
    st.plotly_chart(fig)

elif navigate_button=='Comparisons':

    compare_button = st.radio("Select type to compare", ('Tree Chart','Bar Charts','Scatter Plots')) 


    if compare_button=='Tree Chart':

        df = pd.read_excel('indicators.xlsx')
        df=df.round(3)
        pd.set_option('display.float_format', lambda x: '%.3f' % x)
        edf = pd.melt(df,id_vars=['SeriesName','CountryName'], value_vars=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
        countries = edf['CountryName'].unique()
        series = edf['SeriesName'].unique()
        year = edf['variable'].unique()

        st.header('Tree Chart')

        selectState = st.multiselect('Select Countries', countries)
        series_data = st.multiselect("Attributes: ", series)
        
        selectyear = st.selectbox("Select a year",  year)
        country_d = edf['CountryName'].isin(selectState) & edf['SeriesName'].isin(series_data) & edf.variable.isin([selectyear])
        tree_df = edf[country_d]


        if(len(series_data)>0):
            tree_graph = px.treemap(tree_df, path = ['SeriesName','CountryName','value'],values='value', color='CountryName')
            st.markdown("**Comparison for** " + str(selectyear))
            st.plotly_chart(tree_graph)
            
        else:
            st.write("Select Attributes and countries to display graph")

    elif compare_button=='Bar Charts':
        st.header('Bar Chart')
        edf = pd.melt(df,id_vars=['SeriesName','CountryName'], value_vars=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
        countries = edf['CountryName'].unique()
        series = edf['SeriesName'].unique()
        year = edf['variable'].unique()
        selBarCountry = st.multiselect('Select Countries: ', countries)
        selBarSeries = st.selectbox('Select Attributes: ', series)
        barComp = edf['CountryName'].isin(selBarCountry) & edf['SeriesName'].isin([selBarSeries])
        bar_df = edf[barComp]
        lineChart=alt.Chart(bar_df).mark_bar(opacity=0.7, width = 25.5).encode(
        x='variable',
            y=alt.Y('value', stack = None),
            color='CountryName',
        ).properties(
            width=800,
            height=300)
        if(len(selBarCountry)>0):

            st.markdown('      _ compare countries and attributes from 2005 to 2018_')
            st.write(lineChart)

        
        st.write("Dataset for barchart")
        st.write(bar_df)

    elif compare_button=='Scatter Plots':
        st.header('Scatter Plot')
        import plotly.express as px
        edf = pd.melt(df,id_vars=['SeriesName','CountryName'], value_vars=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
        countries = edf['CountryName'].unique()
        series = edf['SeriesName'].unique()
        year = edf['variable'].unique()

        scatterCountry = st.multiselect(' Select Countries: ', countries)
        scatterAttribute = st.selectbox('What do you want to see? ', series)

        if(len(scatterCountry)>0):
            scatterData = edf['CountryName'].isin(scatterCountry) & edf['SeriesName'].isin([scatterAttribute]) 
            scatterChart = edf[scatterData]

            fig = px.scatter(scatterChart, x="variable", y="value", color="CountryName",
                            hover_data=['value'])
            st.write(fig)
        
    


    




 
    

    

