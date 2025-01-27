from  streamlit import *
from streamlit_extras import *
from streamlit_lottie import *
from streamlit_option_menu import *
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import base64
import lottie
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.keyboard_url import keyboard_to_url
import json as js
import gif as gf
import base64
import pydeck as pdk
import pymongo as py

# Streamlit Part
st.set_page_config(
    page_title="Airbnb Data Analysis",
    page_icon="🏡",  # Optional: Add an emoji or favicon
    layout="wide",   # Set layout to wide
    initial_sidebar_state="expanded"  # Optional: Keep the sidebar expanded
)

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://wallpaperaccess.com/full/11093096.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-color: rgba(0, 0, 0, 0.5); /* Black transparent overlay */
  background-blend-mode: overlay; /* Blend the image with the overlay */
}
[data-testid="stHeader"]{
  background-color: rgba(0,0,0,0);
}
/* Sidebar Background */
[data-testid="stSidebar"] {
  background-image: url("https://images.pexels.com/photos/29559655/pexels-photo-29559655/free-photo-of-cozy-minimalist-bedroom-with-woven-lamp.jpeg?auto=compress&cs=tinysrgb&w=800");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-color: rgba(0,0,0,0); /* Optional: Transparent overlay */
}
/* Style for the tabs container to appear inside a glowing box */
div.stTabs {
    display: cover;
    justify-content: space-between;
    margin-bottom: 20px;
}

/* Individual tab styling */
div.stTabs > div {
    background-color: rgba(0, 0, 0, 0.3); /* Slight dark background for the box */
    border: 3px solid #FF6347; /* Glowing border with red color */
    border-radius: 15px; /* Rounded corners */
    padding: 15px 30px;
    box-shadow: 0 0 15px 5px rgba(255, 99, 71, 0.8); /* Glowing effect */
    transition: all 0.3s ease-in-out;
    font-weight: bold;
}

/* Hover effect for the tabs */
div.stTabs > div:hover {
    box-shadow: 0 0 25px 10px rgba(255, 99, 71, 1); /* Stronger glow on hover */
}

/* Optional: Change the text color of the tab titles */
.stTab {
    color: #FFFFFF;
    font-size: 18px;
}

/* Adjusting tab content styles if necessary */
.stTabContent {
    padding: 20px;
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.8);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

#st.set_page_config(layout = "wide",page_title="Airbnb Data Analysis",page_icon=":house_with_garden:")

#st.markdown(
 #                   "<h1 style='font-family: Georgia, sans-serif; font-size: 36px; color: purple;'>AIRBNB DATA ANALYSIS</h1>", 
  #                  unsafe_allow_html=True
   #             )
#st.title("AIRBNB DATA ANALYSIS")
#st.write("")

def datafr():
    df= pd.read_csv("D:/Air_BnB/Air_BnB.csv")
    return df

df= datafr()

with st.sidebar:
    select = option_menu("Main Menu",["Home", "About", "Data Exploration", "Power-Bi dashboard","Features","Profile","Feedback"],
                         icons=["mic-fill","house","list-task","phone-flip","person","lightbulb-fill",'envelope-paper-heart-fill'],
                         menu_icon="cast",default_index=0)
    




if select == "Home":
    #image1= Image.open(r"D:\Air_BnB\OIP.jpg")
    #st.image(image1)
    st.markdown("<h1 style='font-size: 50px;'><span style='color: cyan;'>AIRBNB</span> <span style='color: white;'</span> <span style='color: white;'>Data Analysis And Visualization</span></h1>",unsafe_allow_html=True)
    st.markdown("<h3 style='font-family: comic sans ms, sans-serif; font-size: 30px; color: yellow;'>About Airbnb</h3>", unsafe_allow_html=True)
    #st.header("About Airbnb")
    st.write("")
    st.markdown('''<h3 style='font-family: comic sans ms, sans-serif; font-size: 18px; color: white;'>
                Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.
                </h3>''',
                 unsafe_allow_html=True
    )
    st.write("")

    st.markdown('''<h3 style='font-family: comic sans ms, sans-serif; font-size: 18px; color: white;'>
                Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.
                </h3>''',
                 unsafe_allow_html=True
                 )
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<h3 style='font-family: comic sans ms, sans-serif; font-size: 30px; color: yellow;'>Background of Airbnb</h3>", unsafe_allow_html=True)
    #st.header("Background of Airbnb")
    st.write("")
    st.markdown('''<h3 style='font-family: comic sans ms, sans-serif; font-size: 18px; color: white;'>
                Airbnb was born in 2007 when two Hosts welcomed three guests to their San Francisco home,
                 and has since grown to over 4 million Hosts who have welcomed over 1.5 billion guest arrivals 
                in almost every country across the globe.</h3>''',
                 unsafe_allow_html=True)



if select == "Data Exploration":
    #tab1, tab2, tab3, tab4, tab5 = st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***",
                                #            "***LOCATION BASED***", "***GEOSPATIAL VISUALIZATION***",
                                 #           "***TOP CHARTS***"])
    st.markdown("<style>div.block-container{padding-top:3rem;}</style>", unsafe_allow_html=True)

    explore = option_menu(
                            menu_title="",
                            options=['PRICE ANALYSIS', 'AVAILABILITY ANALYSIS','LOCATION BASED',"GEOSPATIAL VISUALIZATION","TOP CHARTS"],
                            icons=['cash','check-circle','geo-alt','map','trophy'],
                            menu_icon='',
                            default_index=0,
                            orientation='horizontal')

    if explore == "PRICE ANALYSIS":
        st.markdown("<h1 style='font-size: 50px;'><span style='color: cyan;'>PRICE</span> <span style='color: white;'>DIFFERENTIATION</span></h1>",unsafe_allow_html=True)
        #st.title("PRICE Differentiation")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                <h1 style="font-family: 'Comic Sans MS', sans-serif; font-size: 20px; color: yellow;">
                    Select The Country
                </h1>
            """, unsafe_allow_html=True)
            country = st.selectbox("",sorted(df["country"].unique()))
            df_1 = df[df["country"]==country]
            df_1.reset_index(drop=True,inplace=True)

            st.markdown("""
                <h1 style="font-family: 'Comic Sans MS', sans-serif; font-size: 20px; color: yellow;">
                    Select The Room Type
                </h1>
            """, unsafe_allow_html=True)
            room_typ = st.selectbox("",df_1["room_type"].unique())
            df_2 = df_1[df_1["room_type"]==room_typ]
            df_2.reset_index(drop=True,inplace=True)

            df_bar = pd.DataFrame(df_2.groupby("property_type")[["price", "review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace=True)

            fig_bar = px.bar(df_bar, x = 'property_type', y = 'price', 
                             title= 'Price for Property Types',
                             hover_data=['number_of_reviews','review_scores'], color_discrete_sequence=px.colors.sequential.Redor_r,
                             width=600, height=500)
            fig_bar.update_layout(
                title={
                    'text': 'Price for Property Types',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.3,  # Center-align the title
                }
            )
            st.plotly_chart(fig_bar)

        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                    "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select The Property Type</h4>", 
                    unsafe_allow_html=True
                )
            property_typ = st.selectbox("",df_2["property_type"].unique())

            df_4 = df_2[df_2["property_type"]==property_typ]
            df_4.reset_index(drop=True,inplace=True)

            df_pie = pd.DataFrame(df_4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace=True)

            fig_pie = px.pie(df_pie, values = "price", names = "host_response_time",
                             hover_data=['bedrooms'], title='Price for Host Response Time',
                             color_discrete_sequence=px.colors.sequential.Plasma_r, width=600, height=500)
            fig_pie.update_layout(
                title={
                    'text': 'Price for Host Response Time',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.3,  # Center-align the title
                }
            )
            st.plotly_chart(fig_pie)

        col1,col2 = st.columns(2)
        with col1:
            st.markdown(
                    "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select The Host Response Time</h4>", 
                    unsafe_allow_html=True
                )
            hostresponsetime = st.selectbox("",df_4["host_response_time"].unique())

            df_5 = df_4[df_4["host_response_time"]==hostresponsetime]

            df_do_bar = pd.DataFrame(df_5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace=True)

            fig_do_bar = px.bar(df_do_bar, x = 'bed_type', y = ['minimum_nights','maximum_nights'],
                                title= 'Minimum Nights And Maximum Nights For Bed Types',
                                hover_data=['price'], color_discrete_sequence=px.colors.sequential.Agsunset_r,
                                width=600, height=500)
            fig_do_bar.update_layout(
                title={
                    'text': 'Minimum Nights And Maximum Nights For Bed Types',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.05,  # Center-align the title
                }
            )
            st.plotly_chart(fig_do_bar)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2 = pd.DataFrame(df_5.groupby("bed_type")[["price","bedrooms","beds","accommodates"]].sum())
            df_do_bar_2.reset_index(inplace=True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x = 'bed_type', y = ['bedrooms','beds','accommodates'],
                                  title="BEDROOMS, BEDS, ACCOMMODATES", hover_data=['price'],
                                  barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=600, height=500)
            fig_do_bar_2.update_layout(
                title={
                    'text': 'Bedrooms, Beds, Accommodates',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.2,  # Center-align the title
                }
            )
            st.plotly_chart(fig_do_bar_2)
        
        col_1, col_2 = st.columns(2)
        with col_1:
        
            # Scatter Plot 1: Price vs. Number of Bedrooms

            fig1 = px.scatter(
                df,
                x="bedrooms",
                y="price",
                hover_data=["price", "bedrooms"],
                title="Price vs. Number of Bedrooms",
                labels={"bedrooms": "Number of Bedrooms", "price": "Price"},
            )
            fig1.update_layout(
                title={
                    'text': 'Price vs. Number of Bedrooms',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.3,  # Center-align the title
                }
            )
            st.plotly_chart(fig1)

        with col_2:


            # Scatter Plot 2: Price vs. Number of Reviews

            fig2 = px.scatter(
                df,
                x="number_of_reviews",
                y="price",
                hover_data=["price", "number_of_reviews"],
                title="Price vs. Number of Reviews",
                labels={"number_of_reviews": "Number of Reviews", "price": "Price"},
            )
            fig2.update_layout(
                title={
                    'text': 'Price vs. Number of Reviews',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.3,  # Center-align the title
                }
            )
            st.plotly_chart(fig2)


    if explore == "AVAILABILITY ANALYSIS":

        def datafr():
            df_a= pd.read_csv("D:/Air_BnB/Air_BnB.csv")
            return df_a
        df_a = datafr()
        st.markdown("<h1 style='font-size: 40px;'><span style='color: cyan;'>AVAILABILITY</span> <span style='color: white;'>ANALYSIS</span></h1>",unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                    "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select A Country</h4>", 
                    unsafe_allow_html=True
                )
            country_a = st.selectbox("",sorted(df_a["country"].unique()))
            
            df_a_1 = df_a[df_a["country"]==country_a]
            df_a_1.reset_index(drop=True,inplace=True)
            
            st.markdown(
                    "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select A Property Type</h4>", 
                    unsafe_allow_html=True
                )
            property_typ_a = st.selectbox("",sorted(df_a_1["property_type"].unique()))

            df_a_2 = df_a_1[df_a_1["property_type"]==property_typ_a]
            df_a_2.reset_index(drop=True,inplace=True)

            df_a_sunburst_30 = px.sunburst(df_a_2, path = ["room_type","bed_type","is_location_exact"], values= "availability_30",
                                           width=600, height=500, color_discrete_sequence=px.colors.sequential.PuBu_r, title="Availability for 30 Days")
            df_a_sunburst_30.update_layout(
                title={
                    'text': 'Availability for 30 Days',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.25,  # Center-align the title
                }
            )
            st.plotly_chart(df_a_sunburst_30)


        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_a_sunburst_60 = px.sunburst(df_a_2, path = ["room_type","bed_type","is_location_exact"], values= "availability_60",
                                             width=600, height=500, color_discrete_sequence=px.colors.sequential.Purp, title="Availability for 60 Days")
            df_a_sunburst_60.update_layout(
                title={
                    'text': 'Availability for 60 Days',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.3,  # Center-align the title
                }
            )
            st.plotly_chart(df_a_sunburst_60)

        col1,col2 = st.columns(2)
        with col1:

            df_a_sunburst_90 = px.sunburst(df_a_2, path = ["room_type","bed_type","is_location_exact"], values= "availability_90",
                                           width=600, height=500, color_discrete_sequence=px.colors.sequential.Pinkyl, title="Availability for 90 Days")
            df_a_sunburst_90.update_layout(
                title={
                    'text': 'Availability for 90 Days',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.3,  # Center-align the title
                }
            )
            st.plotly_chart(df_a_sunburst_90)

        with col2:

            df_a_sunburst_365 = px.sunburst(df_a_2, path = ["room_type","bed_type","is_location_exact"], values= "availability_365",
                                            width=600, height=500, color_discrete_sequence=px.colors.sequential.Pinkyl_r, title="Availability for 365 Days")
            df_a_sunburst_365.update_layout(
                title={
                    'text': 'Availability for 365 Days',
                    'font': {
                        'family': 'comic sans ms, sans-serif',
                        'size': 15,
                        'color': '#4CAF50'
                    },
                    'x': 0.3,  # Center-align the title
                }
            )
            st.plotly_chart(df_a_sunburst_365)

        st.markdown(
                "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select A Room Type</h4>", 
                unsafe_allow_html=True
            )

        room_typ_a = st.selectbox("",df_a_2["room_type"].unique())

        df_3_a = df_a_2[df_a_2["room_type"]==room_typ_a]
        df_3_a.reset_index(drop=True,inplace=True)

        df_multi_bar_a = pd.DataFrame(df_3_a.groupby("host_response_time")[["availability_30",
                                                                            "availability_60",
                                                                            "availability_90",
                                                                            "availability_365",
                                                                            "price"]].sum())
        df_multi_bar_a.reset_index(inplace=True)

        fig_df_multi_bar_a = px.bar(df_multi_bar_a, x = "host_response_time", y = ["availability_30","availability_60",
                                                                                   "availability_90","availability_365"],
                                                                                   title="AVAILABILITY FOR HOST RESPONSE TIME",
                                                                                   hover_data=['price'], barmode='group',
                                                                                   color_discrete_sequence=px.colors.sequential.Aggrnyl,
                                                                                   width=1000)
        fig_df_multi_bar_a.update_layout(
            title={
                'text': 'AVAILABILITY FOR HOST RESPONSE TIME',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 15,
                    'color': '#4CAF50'
                },
                'x': 0.3,  # Center-align the title
            }
        )
        st.plotly_chart(fig_df_multi_bar_a)

    if explore == "LOCATION BASED":

        #st.title("LOCATION BASED ANALYSIS")
        #st.write("")

        def datafr():
            df= pd.read_csv("D:/Air_BnB/Air_BnB.csv")
            return df
        df_loc = datafr()
        st.markdown( "<h1 style='font-size: 50px;'><span style='color: cyan;'>LOCATION</span> <span style='color: white;'>Dataset</span></h1>",unsafe_allow_html=True)
        st.markdown(
            "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select the Country</h4>",
            unsafe_allow_html=True
        )
        country_loc = st.selectbox("",sorted(df_loc["country"].unique()))

        df_1_loc = df_loc[df_loc["country"]==country_loc]
        df_1_loc.reset_index(drop=True,inplace=True)
        
        st.markdown(
            "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select A Property Type</h4>", 
            unsafe_allow_html=True
        )
        property_typ_loc = st.selectbox("",sorted(df_1_loc["property_type"].unique()))

        df_2_loc = df_1_loc[df_1_loc["property_type"]==property_typ_loc]
        df_2_loc.reset_index(drop=True,inplace=True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df_2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df_2_loc['price'].min())+' '+str("(30% of the value)"):

                df_val_30 = df_2_loc[df_2_loc["price"] <= differ_max_min*0.30 + df_2_loc['price'].min()]
                df_val_30.reset_index(drop=True,inplace=True)
                return df_val_30
            
            elif sel_val == str(differ_max_min*0.30 + df_2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df_2_loc['price'].min())+' '+str("(30% to 60% of the value)"):

                df_val_60 = df_2_loc[df_2_loc["price"] >= differ_max_min*0.30 + df_2_loc['price'].min()]
                df_val_60_1 = df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df_2_loc['price'].min()]
                df_val_60_1.reset_index(drop=True,inplace=True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df_2_loc['price'].min())+' '+str('to')+' '+str(df_2_loc['price'].max())+' '+str("(60% to 100% of the value)"):

                df_val_100 = df_2_loc[df_2_loc["price"] >= differ_max_min*0.60 + df_2_loc['price'].min()]
                df_val_100.reset_index(drop=True,inplace=True)
                return df_val_100
            
        differ_max_min = df_2_loc['price'].max() - df_2_loc['price'].min()

        st.markdown(
            "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select The Price Range</h4>",
            unsafe_allow_html=True
        )
        val_sel = st.radio("",[str(df_2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df_2_loc['price'].min())+' '+str("(30% of the value)"),
                                                     str(differ_max_min*0.30 + df_2_loc['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df_2_loc['price'].min())+' '+str("(30% to 60% of the value)"),
                                                        str(differ_max_min*0.60 + df_2_loc['price'].min())+' '+str('to')+' '+str(df_2_loc['price'].max())+' '+str("(60% to 100% of the value)")])
        # Determine color based on selected option
        if "30% of the value" in val_sel:
            color = "#90ee90"
        elif "30% to 60% of the value" in val_sel:
            color = "orange"
        else:
            color = "#FF6666"

        # Display the selected value with the corresponding color
        st.markdown(f'<p style="color: {color}; font-size: 18px;font-weight:bold;">You selected: {val_sel}</p>', unsafe_allow_html=True)

        
        df_val_sel = select_the_df(val_sel)
        st.dataframe(df_val_sel)

        # checking the correlation

        df_val_sel_corr = df_val_sel.drop(columns = ["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()
        
        #st.dataframe(df_val_sel_corr)

        df_val_sel_groupby = pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_groupby.reset_index(inplace=True)

        fig_1 = px.bar(df_val_sel_groupby, x = "accommodates", y = ["cleaning_fee","bedrooms","beds"],
                       title="ACCOMMODATES", hover_data=['extra_people'],barmode='group',color_discrete_sequence=px.colors.sequential.Bluered_r,
                       width=1000)
        fig_1.update_layout(
            title={
                'text': 'Accommodates',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 20,
                    'color': '#4CAF50'
                },
                'x': 0.43,  # Center-align the title
            }
        )
        st.plotly_chart(fig_1)

        st.markdown(
            "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select the Room Type</h4>",
            unsafe_allow_html=True
        )
        room_typ_loc = st.selectbox("",df_val_sel["room_type"].unique())

        df_val_sel_r_typ = df_val_sel[df_val_sel["room_type"]==room_typ_loc]
        

        fig_2 = px.bar(df_val_sel_r_typ, x =["street","host_location","host_neighbourhood"] , y = "market",
                       title= "MARKET", hover_data=["name", "host_name", "market"], color_discrete_sequence=px.colors.sequential.YlOrBr,
                       width=1000, height=1100, barmode='group')
        fig_2.update_layout(
            title={
                'text': 'Market',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 20,
                    'color': '#4CAF50'
                },
                'x': 0.45,  # Center-align the title
            }
        )
        st.plotly_chart(fig_2)

        fig_3 = px.bar(df_val_sel_r_typ, x ="government_area" , y = ["host_is_superhost","host_neighbourhood","cancellation_policy"],
                       title= "GOVERNMENT AREA", hover_data=["guests_included", "location_type"], color_discrete_sequence=px.colors.sequential.Mint,
                       barmode="group", width=1300, height=700)
        fig_3.update_layout(
            title={
                'text': 'Government Area',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 20,
                    'color': '#4CAF50'
                },
                'x': 0.44,  # Center-align the title
            }
        )
        st.plotly_chart(fig_3)


        # Select only numeric columns
        numeric_df = df.select_dtypes(include=['number'])

        # Calculate the correlation matrix
        correlation_matrix = numeric_df.corr()

        # Create a Plotly heatmap
        fig_corr = px.imshow(correlation_matrix, 
                        color_continuous_scale='RdBu_r', 
                        title="Correlation Matrix Heatmap", 
                        labels={'color': 'Correlation Coefficient'},
                        width=1300,
                        height=700)
        fig_corr.update_layout(
            title={
                'text': 'Correlation Matrix Heatmap',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 20,
                    'color': '#4CAF50'
                },
                'x': 0.4,  # Center-align the title
            }
        )
        # Show the heatmap in Streamlit
        st.plotly_chart(fig_corr)

    if explore == "GEOSPATIAL VISUALIZATION":
        df = pd.read_csv("D:/Air_BnB/Air_BnB.csv")
        st.markdown( "<h1 style='font-size: 90px;'><span style='color: cyan;'>GEOSPATIAL</span> <span style='color: white;'>Dataset</span></h1>",unsafe_allow_html=True)
        #st.title("GEOSPATIAL VISUALIZATION")
        #st.write("")

        # Function to determine color based on price range
        def get_color(price):
            if price <= 279:
                return [0, 255, 0]  # Green for low price
            elif 279 <= price <= 1000:
                return [255, 255, 0]  # Yellow for medium price
            elif 1000 <= price <= 2000:
                return [255, 165, 0]  # Orange for high price
            elif 2000 <= price <= 3000:
                return[255, 0, 0]       #Red for very high price
            else :
                return [128, 0, 128]  # Purple for very very high price

        # Add a color column to the DataFrame
        df["color"] = df["price"].apply(get_color)

        # Pydeck ScatterplotLayer
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position=["longitude", "latitude"],
            get_fill_color="color",
            get_radius="price * 1000",
            pickable=True,
            radius_min_pixels=5,
            radius_max_pixels=20,
        )

        # Tooltip (hover data)
        tooltip = {
            "html": """
            <b>Name:</b> {name}<br>
            <b>Price:</b> ${price}<br>
            <b>Room Type:</b> {room_type}<br>
            <b>Host Neighborhood:</b> {host_neighbourhood}<br>
            <b>Street:</b> {street}<br>
            <b>Country Code:</b> {country_code}<br>
            <b>Suburb:</b> {suburb}<br>
            <b>Country:</b>{country}
            """,
            "style": {"backgroundColor": "steelblue", "color": "white"}
        }

        # View State
        view_state = pdk.ViewState(
            latitude=df["latitude"].mean(),
            longitude=df["longitude"].mean(),
            zoom=2,
            pitch=0
        )

        # Deck
        r_1 = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            map_style="mapbox://styles/mapbox/light-v9",
            tooltip=tooltip
        )

        # Display in Streamlit
        st.pydeck_chart(r_1, use_container_width=False, height=700,width=1000)


        # geo visual by roomtype

  # Unique Country Selection-------------------------------------
        # Dropdown to select a country
        #selected_country = st.selectbox("Select a Room Type", df["room_type"].unique())

        # Filter the DataFrame by the selected country
        #df_country = df[df["country"] == selected_country]

        #fig_5 = px.scatter_map(df_country, lat="latitude", lon="longitude", color="price", size="accommodates",
        #                        color_continuous_scale="rainbow", hover_data=["price","room_type","property_type","street","country_code","suburb"],
      #                          range_color=(0, 49000), zoom=10)
       # fig_5.update_layout(width = 1150, height = 800, title=f"Geospatial Visualization of Airbnb Listings in {selected_country}",
       #                     mapbox_style="carto-positron")
       # st.plotly_chart(fig_5)

    if explore == "TOP CHARTS":
        df_1 = pd.read_csv("D:/Air_BnB/Air_BnB.csv")
        st.markdown("<style>div.block-container{padding-top:3rem;}</style>", unsafe_allow_html=True)

                # Metrics 

        col1,col2,col3,col4,col5 = st.columns([10,10,10,10,10])

        col1.metric(label="Total Host Count", value=f'{len(df.host_name.unique())}',delta=int(len(df.host_name.unique())/100))
        col2.metric(label="Total Room Types", value=f'{len(df.room_type.unique())}',delta=int(len(df.room_type.unique())))
        col3.metric(label="Total Listings Available", value=f'{len(df.name.unique())}',delta=int(len(df.name.unique())/10))
        col4.metric(label="Total Amount Earned", value=f'{df.price.sum()}',delta=int(df.price.sum()/100))
        col5.metric(label="Total Host Neighbourhood", value=f'{len(df.host_neighbourhood.unique())}',delta=int(len(df.host_neighbourhood.unique())/10))

        col1.write("")
        col1.write("")
        col1.write("")
        col1.write("")
        col1.write("")

        st.markdown(
            "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select The Country</h4>",
            unsafe_allow_html=True
        )
        country_t = st.selectbox("",df["country"].unique(), key="unique_c_t")

        df_1_t = df[df["country"]==country_t]

        st.markdown(
            "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select The Property Type</h4>",
            unsafe_allow_html=True
        )
        property_typ_t = st.selectbox("",df_1["property_type"].unique(), key="unique_p_t")

        df_2_t = df_1_t[df_1_t["property_type"]==property_typ_t]
        df_2_t.reset_index(drop=True,inplace=True)

        df_2_t_sorted = df_2_t.sort_values(by="price", ascending=True)
        df_2_t_sorted.reset_index(drop=True,inplace=True)

        df_price = pd.DataFrame(df_2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace=True)
        df_price.columns = ["host_neighbourhood","price_sum","price_mean"]

        col_1, col2 = st.columns(2)
        with col_1:
            fig_price = px.bar(df_price, x = "price_sum", y ="host_neighbourhood", orientation="h",
                               title="PRICE BASED ON HOST NEIGHBORHOOD",hover_data=["price_mean"],width=600, height=600)
            fig_price.update_layout(
            title={
                'text': 'Price Based On Host Neighbourhood',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 15,
                    'color': '#4CAF50'
                },
                'x': 0.3,  # Center-align the title
            }
        )
            
            st.plotly_chart(fig_price)

        with col2:
            fig_price_2 = px.bar(df_price, x = "price_mean", y ="host_neighbourhood", orientation="h",
                                 title="MEAN PRICE BASED ON HOST NEIGHBORHOOD",hover_data=["price_sum"],width=600, height=600)
            fig_price_2.update_layout(
            title={
                'text': 'Mean Based On Host Neighbourhood',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 15,
                    'color': '#4CAF50'
                },
                'x': 0.29,  # Center-align the title
            }
        )
            st.plotly_chart(fig_price_2)
        
        col_1, col_2 = st.columns(2)
        with col_1:

            df_price_1 = pd.DataFrame(df_2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace=True)

            df_price_1.columns = ["host_location","price_sum","price_mean"]

            fig_price_3 = px.bar(df_price_1, x= "price_sum", y = "host_location", orientation="h",
                                 title="SUM PRICE BASED ON HOST LOCATION",hover_data=["price_mean"],width=600, height=600,
                                 color_discrete_sequence=px.colors.sequential.Oryel_r)
            fig_price_3.update_layout(
            title={
                'text': 'Sum Of Price Based On Host Location',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 15,
                    'color': '#4CAF50'
                },
                'x': 0.27,  # Center-align the title
            }
        )
            st.plotly_chart(fig_price_3)

        with col_2:
            fig_price_4 = px.bar(df_price_1, x= "price_mean", y = "host_location", orientation="h",
                                 title="MEAN PRICE BASED ON HOST LOCATION",hover_data=["price_sum"],width=600, height=600,
                                 color_discrete_sequence=px.colors.sequential.Peach_r)
            fig_price_4.update_layout(
            title={
                'text': 'Mean Price Based On Host Location',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 15,
                    'color': '#4CAF50'
                },
                'x': 0.3,  # Center-align the title
            }
        )
            st.plotly_chart(fig_price_4)
        st.markdown(
            "<h4 style='font-family: comic sans ms; font-size: 20px; color: yellow;'>Select The Room Type</h4>",
            unsafe_allow_html=True
        )
        room_typ_t = st.selectbox("",df_2_t_sorted["room_type"].unique(), key="unique_r_t")
        df_3_t = df_2_t_sorted[df_2_t_sorted["room_type"]==room_typ_t]

        df_3_t_sorted_price = df_3_t.sort_values(by="price", ascending=True)
        df_3_t_sorted_price.reset_index(drop=True,inplace=True)

        df_3_top_50_price = df_3_t_sorted_price.head(100)

        fig_top_50_price_1 = px.bar(df_3_top_50_price, x = "name", y = "price", color = "price",
                                    color_continuous_scale="rainbow", range_color=(0, df_3_top_50_price.price.max()),
                                    title= "MINIMUM NIGHTS, MAXIMUM NIGHTS AND ACCOMMODATES",
                                    hover_data=["minimum_nights","maximum_nights","accommodates"],width=1200, height=800)
        fig_top_50_price_1.update_layout(
            title={
                'text': 'Minimum Nights, Maximum Nights And Accommodates',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 15,
                    'color': '#4CAF50'
                },
                'x': 0.3,  # Center-align the title
            }
        )
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2 = px.bar(df_3_top_50_price, x = "name", y = "price", color = "price", color_continuous_scale="greens",
                                    title= "BEDROOMS, BEDS , ACCOMMODATES AND BED TYPE", range_color=(0, df_3_top_50_price.price.max()),
                                    hover_data=["bedrooms","beds","accommodates","bed_type"],width=1200, height=800)
        fig_top_50_price_2.update_layout(
            title={
                'text': 'Bedrooms, Beds, Accommodates And Bed Type',
                'font': {
                    'family': 'comic sans ms, sans-serif',
                    'size': 15,
                    'color': '#4CAF50'
                },
                'x': 0.38,  # Center-align the title
            }
        )
        st.plotly_chart(fig_top_50_price_2)

if select == "Feedback":
    kishore_1 = py.MongoClient("mongodb+srv://Kishore:mongodb123@cluster-kishore.kznavjg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Kishore")
    db = kishore_1["Feedback_airbnb"]
    collection = db["comment"]

    st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)
    col1, col2, col3, = st.columns([3, 8, 3])

    with col2:
        selected_1 = option_menu(
            menu_title="OPINION BOX",
            options=['Choose Option', 'Your Feedback', "Explore User Thoughts"],
            icons=['arrow-down-circle-fill', 'envelope-plus-fill', 'people-fill'],
            default_index=0)
    col2.write("")
    col2.write("")
    col2.write("")
    col2.write("")

    if selected_1 == 'Choose Option':
        kishore_1 = py.MongoClient("mongodb+srv://Kishore:mongodb123@cluster-kishore.kznavjg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Kishore")
        db = kishore_1["Feedback_airbnb"]
        collection = db["Reaction_emoji"]
        # Animation
        def lottie(filepath):
            with open(filepath, 'r') as file:
                return js.load(file)
        # Layout for emoji options
        st.write("Choose your mood:")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

        # Emoji animations
        emoji_files = {
            "Angry": "D:/Air_BnB/angry_emoji.json",
            "Smile": "D:/Air_BnB/smile_emoji.json",
            "Calm": "D:/Air_BnB/calm_emoji.json",
            "Love": "D:/Air_BnB/love_emoji.json",
        }

        # Render Lottie animations in columns
        selected_emoji = None
        with col1:
            if st.button("Angry"):
                selected_emoji = "Angry"
            file = lottie("D:/Air_BnB/angry_emoji.json")
            st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=200,
                    width=200,
                    key=None
                )
        with col2:
            if st.button("Smile"):
                selected_emoji = "Smile"
            file = lottie("D:/Air_BnB/smile_emoji.json")
            st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=200,
                    width=200,
                    key=None
                )
        with col3:
            if st.button("Calm"):
                selected_emoji = "Calm"
            file = lottie("D:/Air_BnB/calm_emoji.json")
            st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=200,
                    width=200,
                    key=None
                )
        with col4:
            if st.button("Love"):
                selected_emoji = "Love"
            file = lottie("D:/Air_BnB/love_emoji.json")
            st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=200,
                    width=200,
                    key=None
                )

        # Save selection to MongoDB
        if selected_emoji:
            collection.insert_one({"emoji": selected_emoji})
            st.success(f"Your selection ({selected_emoji}) has been saved!")
            
    elif selected_1 == 'Your Feedback':

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            col1, col2, col3 = st.columns([10, 30, 5])
            col2.markdown(
                "<h1 style='font-size: 90px;'><span style='color:white;'>Your</span> <span style='color:cyan;'>Feedback</span> <span style='color: white;'>Here </span> </h1>",
                unsafe_allow_html=True)
            # animation

            st.write("")

            st.write("")

            st.write("")
            col1, col2, col3 = st.columns([10, 15, 5])
            with col2:
                file = lottie("D:/Air_BnB/star_before_fb.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=600,
                    key=None
                )
            col1, col2, col3, = st.columns([3, 8, 3])

            with col2:
                col2.markdown(
                    "<h1 style='font-size: 30px;'><span style='color:white;'>Enter</span> <span style='color:cyan;'>Comment</span> <span style='color: white;'>Here ⬇️</span> </h1>",
                    unsafe_allow_html=True)
                Comment = st.text_input('   ')
                st.write(Comment)
                if st.button('Save Comment'):
                    collection.insert_one({'comment of user': Comment})
                    st.write("")
                    st.write("")
                    col1, col2, col3, = st.columns([5, 8, 5])
                    st.success('Your Valuable Comment Saved Thankyou!', icon="✅")
                    col1, col2, col3 = st.columns([10, 30, 10])
                    with col2:
                        file = lottie("D:/Air_BnB/star.json")
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            # renderer='svg',
                            height=100,
                            width=500,
                            key=None
                        )
            col1, col2, col3, = st.columns([3, 8, 3])
            with col2:
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )
            
    elif selected_1 == 'Explore User Thoughts':

        def lottie(filepath):
            with open(filepath, 'r') as file:
                return js.load(file)

        col1, col2, col3 = st.columns([10, 30, 5])

        with col2:

            file = lottie("D:/Air_BnB/down_arrow.json")
            st_lottie(
                file,
                speed=2,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=300,
                width=800,
                key=None
            )
        col2.markdown(
                    "<h1 style='font-size: 70px;'><span style='color:white;'>Explore</span> <span style='color:cyan;'>User Thoughts </span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
        col2.write("")
        col2.write("")
        with col2:

            file = lottie("D:/Air_BnB/thoughts.json")
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=500,
                width=800,
                key=None
            )
        st.write("")
        st.write("")
        st.write("")
        col1, col2, col3, = st.columns([3.6, 10, 3])
        with col2:
            # if st.button("Click Me!"):
            res = [i['comment of user'] for i in collection.find()]
            st.write("")
            with st.spinner('Wait for it...'):
                time.sleep(5)

            colored_header(
                label="Comments By Users ⬇",
                description="",
                color_name="blue-green-70", )
            for i in res:
                print(st.code(i))

            col1, col2, col3 = st.columns([1, 10, 1])
            col2.write("")
            col2.write('')
            col2.markdown(
                "<h1 style='font-size: 35px;'><span style='color:cyan;'>Press</span> <span style='color:white;'>'G'</span> <span style='color:cyan;'>On Keyboard To Explore More Project</span> </h1>",
                unsafe_allow_html=True)
            with col2:
                keyboard_to_url(key="G", url="https://github.com/KishoreKumar-J-22")
            def lottie(filepath):
                        with open(filepath, 'r') as file:  # 'G' On Keyboard To Explore More Project
                            return js.load(file)

            with col2:
                file = lottie("D:/Air_BnB/click2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    height=100,
                    width=700,
                    key=None
                )

            colored_header(
                label="",
                description="",
                color_name="blue-green-70", )



if select == "About":
    st.markdown("<h1 style='font-size: 50px;'><span style='color: cyan;'>ABOUT</span> <span style='color: white;'</span> <span style='color: white;'>THIS PROJECT</span></h1>",unsafe_allow_html=True)


    st.subheader(":orange[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')
    
    st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')
    
    st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')
    
    st.subheader(":orange[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
    
    st.subheader(":orange[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')

# Features

if select == "Features":
    st.markdown(
                    "<h1 style='font-family: comic sans ms, sans-serif;text-align: center; font-size: 30px; color: purple;'>Features</h1>", 
                    unsafe_allow_html=True
                )
#st.title("AIRBNB DATA ANALYSIS")
    #st.write("")
    st.title("")
    col1,col2,col3 = st.columns([12.5,10,10])

    col2.write("")
    col2.write("")
    col2.write("")

    col2.markdown( "<h1 style='font-size: 50px;'><span style='color: cyan;'>Load</span> <span style='color: white;'</span> <span style='color: white;'>Dataset</span></h1>",unsafe_allow_html=True)


    
    col2.write("")
    col1,col2,col3 = st.columns([10,10,9])

    col2.write("")
    uploaded_file = col2.file_uploader("   ", type=["csv", "txt", "jpg", "png", "pdf"])

    if uploaded_file is not None:
            # Save the uploaded file
            with open('uploaded_data.csv', "wb") as f:
                f.write(uploaded_file.read())
            df_100 = pd.read_csv('uploaded_data.csv')

    
    col2.write("")
    col2.write("")
    col2.write("")
    # col2.write("")
    # col2.write("")
    col1,col2,col3 = st.columns([12,10,10])
    col2.write("")
    col2.write("")
    col2.write("")
    col2.write("")

    col2.markdown( "<h1 style='font-size: 50px;'><span style='color: cyan;'>Know </span> <span style='color: white;'>The</span> <span style='color: cyan;'>Features</span></h1>",unsafe_allow_html=True)



    
    col2.write("")
    col2.write("")
    col1,col2,col3 = st.columns([18,10,10])

    # Continous and categorical values
    df['_id'] = df['_id'].apply(lambda x : str(x))
    df['host_id'] = df['host_id'].apply(lambda x : str(x))
    continous_features = df.select_dtypes(include=['int64','float64']).columns
    cat_deatures = df.select_dtypes(include=['object']).columns 

    if col2.button('Know features'):
                
        col1,col2,col3,col4 = st.columns([2,10,10,2])

        col2.write("")
        col2.write("")
        col2.write("")
        
        with col2 :
            st.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'>Continous</span><span style='color: White;'> Features</span> </h1>",unsafe_allow_html=True)
            colored_header(
            label="",
            description="",
            color_name="blue-green-70", )

                
            for i in continous_features:
                    st.markdown( f"<h1 style='font-size: 25px;'><span style='color: white;'> {i} </span> </h1>",unsafe_allow_html=True)
        col3.write("")
        col3.write("")
        col3.write("")
        with col3 :
            st.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'>Categorical </span><span style='color: White;'> Features</span> </h1>",unsafe_allow_html=True)
            colored_header(
            label="",
            description="",
            color_name="blue-green-70", )

                
            for i in cat_deatures:
                    st.markdown( f"<h1 style='font-size: 25px;'><span style='color: white;'> {i} </span> </h1>",unsafe_allow_html=True)




                       
    col1,col2,col3 = st.columns([7,10,5])
    col2.write("")
    col2.write("")
    col2.write("")
    col2.write("")
    col2.write("")
    col2.write("")
    col2.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'> Summary </span><span style='color: white;'> Statistics </span> </h1>",unsafe_allow_html=True)
    col2.write("")
    col2.write("")
    col2.write("")
    col2.write("")
    col2.write("")
    col2.write("")
    col1,col2,col3 = st.columns([9,10,5])
    col2.markdown( f"<h1 style='font-size: 40px;'><span style='color: cyan;'> Select </span><span style='color: white;'> Feature Type </span> </h1>",unsafe_allow_html=True)

    col1,col2,col3 = st.columns([9,10,5])
    select = col2.selectbox('',['Continous Features','Categorical Features'])
    # col2.write("")
    # col2.write("")
    col2.write("")
    col2.write("")

    if select == 'Continous Features':
        col2.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'> Continous </span><span style='color: white;'> Features </span> </h1>",unsafe_allow_html=True)

        col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Select </span><span style='color: white;'> Feature </span> </h1>",unsafe_allow_html=True)

        option = col2.selectbox('',continous_features)
        if col2.button('Show'):

            x = df[option].describe()

            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Selected Feature : </span><span style='color: white;'> {option}</span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Count : </span><span style='color: white;'>{x[0]} </span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Mean : </span><span style='color: white;'> {x[1]} </span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Std :  </span><span style='color: white;'> {x[2]}</span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Min  : </span><span style='color: white;'>  {x[3]}</span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> 25 % : </span><span style='color: white;'> {x[4]}</span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> 50 % : </span><span style='color: white;'>  {x[5]}</span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> 75 % : </span><span style='color: white;'>  {x[6]}</span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Max  : </span><span style='color: white;'>  {x[7]}</span> </h1>",unsafe_allow_html=True)
            col1,col2,col3 = st.columns([7,10,5])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'> Feature </span><span style='color: white;'>  Distribution </span> </h1>",unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.markdown( f"<h1 style='font-size: 40px;'><span style='color: cyan;'> {option} </span><span style='color: white;'> Feature  Distribution </span> </h1>",unsafe_allow_html=True)

            
            fig = px.histogram(df[f'{option}'], nbins=20)
            fig.update_layout(
                plot_bgcolor='#0E1117',
                paper_bgcolor='#0E1117',
                xaxis_title_font=dict(color='#0DF0D4'),
                yaxis_title_font=dict(color='#0DF0D4')
            )
            fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                hoverlabel_font_color="#0DF0D4")
            fig.update_xaxes(title_text="Availability Types")

            fig.update_yaxes(title_text="Days  Count")

            fig.update_traces(marker_color='#1BD4BD')
            
            st.plotly_chart(fig, theme=None, use_container_width=True)




    elif select == 'Categorical Features':
        col2.markdown( f"<h1 style='font-size: 60px;'><span style='color: cyan;'> Categorical  </span><span style='color: white;'> Features </span> </h1>",unsafe_allow_html=True)

        col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Select </span><span style='color: white;'> Feature </span> </h1>",unsafe_allow_html=True)

        option = col2.selectbox('',cat_deatures)

        if col2.button('Show'):

            x = df[option].describe()

            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Selected Feature : </span><span style='color: white;'> {option}</span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Count : </span><span style='color: white;'>{x[0]} </span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Unique : </span><span style='color: white;'> {x[1]} </span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top :  </span><span style='color: white;'> {x[2]}</span> </h1>",unsafe_allow_html=True)
            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Feq  : </span><span style='color: white;'>  {x[3]}</span> </h1>",unsafe_allow_html=True)
# PowerBI dashboard
if select == 'Power-Bi dashboard':
                st.markdown("<style>div.block-container{padding-top:0rem;}</style>", unsafe_allow_html=True)

                col1,col2,col3 = st.columns([5,10,5])
                col2.write("")
                col2.write("")
                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([1, 10, 1])
                with col2:
                    file = lottie("D:/Air_BnB/d1.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        height=900,
                        width=1700,
                        key=None
                    )
                col1,col2,col3 = st.columns([7,10,5])
                col2.markdown( "<h1 style='font-size: 40px;'><span style='color: white;'>Press </span> <span style='color: cyan;'>'P'</span> <span style='color: white;'>To See PowerBI Dashboard</span></h1>",unsafe_allow_html=True)
                keyboard_to_url(key="P", url="https://app.powerbi.com/groups/me/reports/0d94fe89-7784-41b1-8c17-ef5cb6185bd6/7bd9f31de8e6f15293f4?experience=power-bi")

elif select == "Profile":
        
    st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.markdown(
            "<h1 style='font-size: 79px;text-align: center;'><span style='color:white;'>Hi!</span> <span style='color: white;'>I'm </span><span style='color: cyan;'> Kishore Kumar</span> </h1>",
            unsafe_allow_html=True)
    #st.image("D:/Air_BnB/profile-pic.png",width=300)

    # Convert image to base64
    image_path = "D:/Air_BnB/profile-pic.png"
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()

    # Center image with HTML
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{encoded_image}" width="300">
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("""
    <style>
    /* Custom font style for links */
    a {
        font-family: "Arial", sans-serif;  /* Change to desired font */
        font-size: 18px;                  /* Adjust font size */
        font-weight: bold;                /* Make the font bold */
        color: #0073e6;                   /* Link color */
        text-decoration: none;            /* Remove underline */
    }
    a:hover {
        color: #005bb5;                   /* Hover color for links */
    }
    </style>
    """, unsafe_allow_html=True)
    Links_of_mine = option_menu(
                        menu_title = "Connect Me",
                        options = ["Instagram","Email","LinkedIn","Git_Hub"],
                        icons = ["instagram","envelope","linkedin","github"],
                        menu_icon = "cast",
                        default_index = 0
                        )


        # Display the corresponding link based on selection
    if Links_of_mine == "Instagram":
        st.markdown('<a href="https://www.instagram.com/kishore_kumar_22/" target="_blank"><i class="fab fa-instagram"></i> Instagram</a>', unsafe_allow_html=True)
    elif Links_of_mine == "Email":
        st.markdown('<a href="mailto:kishorericardo026@gmail.com" target="_blank"><i class="fas fa-envelope"></i> Email</a>', unsafe_allow_html=True)
    elif Links_of_mine == "LinkedIn":
        st.markdown('<a href="https://www.linkedin.com/in/kishorekumar2002" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>', unsafe_allow_html=True)
    elif Links_of_mine == "Git_Hub":
        st.markdown('<a href="https://github.com/KishoreKumar-J-22" target="_blank"><i class="fab fa-github"></i> GitHub</a>', unsafe_allow_html=True)


