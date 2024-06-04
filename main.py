import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

df = pd.read_csv('/Users/sheenkocher/PycharmProjects/AttemptAtDashboard/ticketDataset.csv')
print(df)
df.dropna()
print(df.columns)


df.rename(columns={'Ticket Status': 'Ticket_Status', 'Customer Gender': 'Customer_Gender', 'Ticket Priority' : 'Ticket_Priority', 'Ticket Type' : 'Ticket_Type'}, inplace=True)


#slide bar
st.sidebar.header("Please Filter Here : ")

Status = st.sidebar.multiselect(
   "SELECT STATUS : ",
    options= df['Ticket_Status'].unique(),
    default= df['Ticket_Status'].unique()

)

Gender = st.sidebar.multiselect(
   "SELECT CUSTOMER TYPE : ",
    options= df['Customer_Gender'].unique(),
    default= df['Customer_Gender'].unique()

)

Priority = st.sidebar.multiselect(
   "SELECT Priority : ",
    options= df['Ticket_Priority'].unique(),
    default= df['Ticket_Priority'].unique()

)
TicketType = st.sidebar.multiselect(
   "SELECT Ticket type: ",
    options= df['Ticket_Type'].unique(),
    default= df['Ticket_Type'].unique()

)



df_selection = df.query(
    "Ticket_Status == @Status & Customer_Gender == @Gender &  Ticket_Priority == @Priority & Ticket_Type == @TicketType"
)


#-----MAIN PAGE-------
st.title(":bar_chart: SYSTEM TICKETS DASHBOARD ")
st.markdown("##")

#TOP KPI's

total_records_in_system = df['Ticket ID'].max()
average_age = round(df_selection['Customer Age'].mean(),1)
records_selected_currently = df_selection.shape[0]

left_column,middle_column,right_column = st.columns(3)
with left_column :
    st.subheader("TOTAL RECORDS : ")
    st.subheader(f"{total_records_in_system}")
with middle_column :
    st.subheader("AVERAGE CUSTOMER AGE : ")
    st.subheader(f"{average_age}")
with right_column :
    st.subheader("RECORDS SELECTED CURRENTLY : ")
    st.subheader(f"{records_selected_currently}")
st.markdown("---")

#plotting


# Create the Count Plot with Horizontal Orientation
fig = px.bar(df_selection, y='Ticket_Priority', title='Ticket Priority Count Plot', orientation='h')

# Customize the appearance and layout
fig.update_traces(marker=dict(color='orange'),  # Change the color of the bars
                  opacity=0.8,  # Adjust the opacity of the bars
                  hovertemplate="%{y}: %{x}",  # Define the tooltip format
                  )
fig.update_layout(title_font=dict(size=24),  # Set the title font size
                  yaxis_title="Ticket Priority",  # Set the y-axis title
                  xaxis_title="Count",  # Set the x-axis title
                  title_x=0.5,  # Center the title
                  )

# Display the Count Plot with Horizontal Orientation
st.plotly_chart(fig)



# Create the Histogram
fig = px.histogram(df_selection, x='Ticket_Status', title='Ticket Status Histogram')

# Customize the appearance and layout
fig.update_traces(marker=dict(color='royalblue'),  # Change the color of the bars
                  opacity=0.8,  # Adjust the opacity of the bars
                  hovertemplate="%{x}: %{y}",  # Define the tooltip format
                  )
fig.update_layout(title_font=dict(size=24),  # Set the title font size
                  xaxis_title="Ticket Status",  # Set the x-axis title
                  yaxis_title="Count",  # Set the y-axis title
                  title_x=0.5,  # Center the title
                  )
st.plotly_chart(fig)

#creating pie chart

# Define the Pie Chart Data
pie_chart_data = df_selection['Customer_Gender'].value_counts()

# Create the Pie Chart
fig = px.pie(pie_chart_data, names=pie_chart_data.index, values=pie_chart_data.values)

# Set the Pie Chart Title
fig.update_layout(title_text='Gender Distribution')

# Display the Pie Chart
st.plotly_chart(fig)


# Create the Scatter Plot
fig = px.scatter(df_selection, x='Ticket_Type', y='Customer Age', color='Ticket_Priority',
                 title='Scatter Plot for Ticket Type')

# Customize the appearance and layout
fig.update_traces(marker=dict(size=12, opacity=0.8),  # Set marker size and opacity
                  selector=dict(mode='markers'),  # Set marker mode to 'markers'
                  hovertemplate="%{x}: %{y} years, Priority: %{marker.color}",  # Define the tooltip format
                  )
fig.update_layout(title_font=dict(size=24),  # Set the title font size
                  xaxis_title="Ticket Type",  # Set the x-axis title
                  yaxis_title="Customer Age",  # Set the y-axis title
                  title_x=0.5,  # Center the title
                  legend_title="Ticket Priority",  # Set the legend title
                  legend_traceorder='reversed',  # Reverse the order of legend items
                  )

# Display the Scatter Plot
st.plotly_chart(fig)














