import streamlit as st
import time as t
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Assuming you have the data stored in a pandas DataFrame called 'df'
# If not, load the data here
df = pd.read_csv(r'C:\Users\Guduri Prasanna\downloads\doctor.csv')
df['age'] = df['age'].apply(lambda x: int(x * 100))

def main():
    st.set_page_config(page_title='Doctor Visit App', page_icon='download.jpg', layout="wide", initial_sidebar_state="expanded")

    # Creating the sidebar for Doctor Visit Data Analysis and Visualization
    st.sidebar.markdown('''# :center[Doctor Visit Data Analysis and Visualization]''')
    opt = st.sidebar.selectbox('Choose an option:', options=('Distribution of visits', 'Income affects visits', 'Health Insurance Distribution', 'Correlation matrix', 'Illness Distribution',
     'Reduced Charges Distribution','Health Distribution','chronic illness'))
    
    if opt == 'Distribution of visits':
        st.sidebar.info("You selected 'Distribution of visits'.")
        plot_visits_analysis()
    elif opt == 'Income affects visits':
        st.sidebar.info("You selected 'Income vs. visits'.")
        plot_income_vs_visits()
    elif opt == 'Health Insurance Distribution':
        st.sidebar.info("You selected 'Private Health Insurance Distribution'.")
        plot_health_insurance_analysis()
    elif opt == 'Correlation matrix':
        st.sidebar.info("You selected 'Correlation matrix'.")
        plot_correlation_matrix()
    elif opt == 'Illness Distribution':
        st.sidebar.info("You selected 'Illness Distribution'.")
        plot_illness_analysis()
    elif opt == 'Reduced Charges Distribution':
        st.sidebar.info("You selected 'Reduced Charges Distribution'.")
        plot_reduced_charges_analysis()
    elif opt == 'Health Distribution':
        st.sidebar.info("You selected 'Health Distribution'.")
        plot_health_distribution()
    elif opt == 'chronic illness':
        st.sidebar.info("You selected 'chronic illness'.")
        analyze_nchronic_and_lchronic()



def plot_visits_analysis():
    with st.spinner('Loading'):
        t.sleep(0.3)
    st.title("Doctor Visits")
    st.info('''Doctor Visits''',icon='📌')
    st.snow()
    # Histogram of 'visits' attribute
    fig_visits_distribution = px.histogram(df, x='visits', nbins=20, color_discrete_sequence=['skyblue'], title='Distribution of Doctor Visits')
    st.plotly_chart(fig_visits_distribution)

    # Countplot of 'gender' attribute
    fig_visits_by_gender = px.bar(df, x='gender', color='gender',
                                  color_discrete_map={'female': 'lightblue', 'male': 'lightpink'},
                                  title='Number of Visits by Genders',
                                  labels={'gender': 'Gender', 'visits': 'Number of Visits'})


    # Display the bar plot in the app
    st.plotly_chart(fig_visits_by_gender)
    avg_visits_by_age = df.groupby('age')['visits'].mean().reset_index()
    fig_avg_visits_by_age = px.bar(avg_visits_by_age, x='age', y='visits', color='age', 
                                   labels={'age': 'Age', 'visits': 'Average Number of Doctor Visits'},
                                   title='Average Doctor Visits')
    fig_avg_visits_by_age.update_layout(xaxis_tickvals=list(range(0, 101, 5))) 
    st.plotly_chart(fig_avg_visits_by_age)
    st.success('Success!')
    

def plot_income_vs_visits():
    with st.spinner('Loading'):
        t.sleep(0.3)
    st.title("Income Affects Visits")
    st.info('''Income Affects Visits''',icon='📌')
    st.snow()
    # Visualization: Scatter plot of 'income' vs. 'visits'
    fig = px.scatter(df, x='income', y='visits', color_discrete_sequence=['salmon'], title='Income vs. Visits')
    fig.update_layout(xaxis_title='Income', yaxis_title='Number of Visits')
    st.plotly_chart(fig)
    st.success('Success!')

def plot_health_insurance_analysis():
    with st.spinner('Loading'):
        t.sleep(0.3)
    st.title("Health Insurance")
    st.info('''Health Insurance''',icon='📌')
    st.snow()
    # Calculate the percentage of people getting government insurance
    health_insurance_percentage = df['freepoor'].value_counts(normalize=True) * 100
    health_insurance_percentage.index = ['Government Insurance', 'Private Health Insurance']
    government_insurance_percentage = df['freepoor'].value_counts(normalize=True) * 100

    # Create a bar plot for the percentage of people getting government insurance
    fig_percentage = px.bar(x=government_insurance_percentage.index, y=government_insurance_percentage.values,
                            color=government_insurance_percentage.index,
                            color_discrete_sequence=px.colors.sequential.Viridis,
                            labels={'x': 'Government Insurance', 'y': 'Percentage'},
                            title='Percentage of People with Government Insurance')

    # Set the y-axis range to 0-100
    fig_percentage.update_yaxes(range=[0, 100])

    # Calculate the percentage of patients with private health insurance
    private_health_insurance_percentage = df['private'].value_counts(normalize=True) * 100

    # Create a bar plot for private health insurance distribution
    fig_distribution = px.bar(x=private_health_insurance_percentage.index, y=private_health_insurance_percentage.values,
                              color=private_health_insurance_percentage.index,
                              color_discrete_sequence=px.colors.sequential.Viridis,
                              labels={'x': 'Private Health Insurance', 'y': 'Percentage'},
                              title='Percentage of Patients with Private Health Insurance')
     

    # Create a bar plot for health insurance distribution
    fig_health_insurance = px.bar(x=health_insurance_percentage.index, y=health_insurance_percentage.values,
                                  color=health_insurance_percentage.index,
                                  color_discrete_sequence=px.colors.sequential.Viridis,
                                  labels={'x': 'Health Insurance', 'y': 'Percentage'},
                                  title='Percentage of Patients with Health Insurance')

    # Set the y-axis range to 0-100
    fig_health_insurance.update_yaxes(range=[0, 100])


    # Set the y-axis range to 0-100
    fig_distribution.update_yaxes(range=[0, 100])

    # Display both plots in the app
    st.plotly_chart(fig_health_insurance)
    st.plotly_chart(fig_percentage)
    st.plotly_chart(fig_distribution)
    st.success('Success!')

def plot_correlation_matrix():
    with st.spinner('Loading'):
        t.sleep(0.3)
    st.title("Corelation")
    st.info('''Corelation''',icon='📌')
    st.snow()
    # Calculate the correlation matrix for numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns
    correlation_matrix = df[numeric_columns].corr()

    # Create a heatmap to visualize the correlations
    fig = px.imshow(correlation_matrix, color_continuous_scale='viridis', zmin=-1, zmax=1)
    fig.update_xaxes(title='Attributes')
    fig.update_yaxes(title='Attributes')
    fig.update_layout(title='Correlation Matrix', title_x=0.5)
    st.plotly_chart(fig)
    st.success('Success!')

def plot_illness_analysis():
    with st.spinner('Loading'):
        t.sleep(0.3)
    st.title("Illness")
    st.info('''Illness caused''',icon='📌')
    st.snow()
    # Calculate the percentage of patients with and without illness
    illness_percentage = df['illness'].value_counts(normalize=True) * 100

    # Bar plot for illness distribution
    fig_illness_distribution = px.bar(illness_percentage, x=illness_percentage.index, y=illness_percentage.values,
                                      color=illness_percentage.index, color_discrete_sequence=['#ffcccb', '#00ced1'])
    fig_illness_distribution.update_layout(xaxis_title='Illness', yaxis_title='Percentage', title='Proportion of Patients with and Without Illness')

    # Calculate the average number of visits for patients with and without illness
    avg_visits_by_illness = df.groupby('illness')['visits'].mean().reset_index()

    # Bar plot for average number of visits comparison
    fig_avg_visits_by_illness = px.bar(avg_visits_by_illness, x='illness', y='visits', color='illness',
                                       color_discrete_sequence=['#ffcccb', '#00ced1'])
    fig_avg_visits_by_illness.update_layout(xaxis_title='Illness', yaxis_title='Average Number of Visits', title='Average Number of Visits by Illness')

    # Display both plots in the app
    st.plotly_chart(fig_illness_distribution)
    st.plotly_chart(fig_avg_visits_by_illness)
    st.success('Success!')


def plot_reduced_charges_analysis():
    with st.spinner('Loading'):
        t.sleep(0.3)
    st.title("Reduced Charges")
    st.info('''Reduced Charges''',icon='📌')
    st.snow()
    df['gender'] = df['gender'].map({'male': 0, 'female': 1})
    # Calculate the percentage of patients receiving reduced medical charges
    reduced_percentage = df['reduced'].value_counts(normalize=True) * 100

    # Bar plot for reduced charges distribution
    fig_reduced_distribution = px.bar(reduced_percentage, x=reduced_percentage.index, y=reduced_percentage.values,
                                      color=reduced_percentage.index, color_discrete_sequence=['#ffcccb', '#00ced1'])
    fig_reduced_distribution.update_layout(xaxis_title='Reduced Charges', yaxis_title='Percentage',
                                           title='Percentage of Patients Receiving Reduced Medical Charges')

    # Group by 'reduced' and calculate the demographics (e.g., gender, income) of patients
    reduced_demographics = df.groupby('reduced')[['gender', 'income']].mean().reset_index()

    # Bar plot for demographics of patients receiving reduced charges
    fig_reduced_demographics = px.bar(reduced_demographics, x='reduced', y='income', color='reduced',
                                      color_discrete_sequence=['#ffcccb', '#00ced1'],
                                      labels={'reduced': 'Reduced Charges', 'income': 'Average Income'},
                                      title='Demographics of Patients Receiving Reduced Medical Charges')
    fig_reduced_demographics.update_layout(yaxis_tickprefix="$")

    # Calculate the average number of visits for patients with and without reduced charges
    avg_visits_by_reduced = df.groupby('reduced')['visits'].mean().reset_index()

    # Bar plot for average number of visits comparison
    fig_impact_of_reduced_charges = px.bar(avg_visits_by_reduced, x='reduced', y='visits', color='reduced',
                                           color_discrete_sequence=['#ffcccb', '#00ced1'],
                                           labels={'reduced': 'Reduced Charges', 'visits': 'Average Number of Visits'},
                                           title='Impact of Reduced Medical Charges on Doctor Visits')

    # Display all three plots in the app
    st.plotly_chart(fig_reduced_distribution)
    st.plotly_chart(fig_reduced_demographics)
    st.plotly_chart(fig_impact_of_reduced_charges)
    st.success('Success!')


def plot_health_distribution():
    with st.spinner('Loading'):
        t.sleep(0.3)
    st.title("Health Distribution")
    st.info('''Health Distribution''',icon='📌')
    st.snow()
    st.subheader('Health Distribution')
    health_distribution = df['health'].value_counts().reset_index()
    health_distribution.columns = ['health', 'count']
    fig_health_distribution = px.bar(health_distribution, x='health', y='count', color='health',
                                     labels={'health': 'Health', 'count': 'Number of Records'},
                                     title='Distribution of Health')
    st.plotly_chart(fig_health_distribution)

    # Visualization: Average Visits by Health
    st.subheader('Average Visits by Health')
    avg_visits_by_health = df.groupby('health')['visits'].mean().reset_index()
    fig_avg_visits_by_health = px.bar(avg_visits_by_health, x='health', y='visits', color='health',
                                      labels={'health': 'Health', 'visits': 'Average Number of Doctor Visits'},
                                      title='Average Doctor Visits by Health')
    st.plotly_chart(fig_avg_visits_by_health)

    # Visualization: Health Relationships
    st.subheader('Health Relationships')
    fig_health_relationships = px.scatter(df, x='age', y='visits', color='health',
                                          labels={'age': 'Age', 'visits': 'Number of Visits', 'health': 'Health'},
                                          title='Health Relationships')
    st.plotly_chart(fig_health_relationships)
    st.success('Success!')


def analyze_nchronic_and_lchronic():
    with st.spinner('Loading'):
        t.sleep(0.3)
    st.title("Nchronic Affects")
    st.info('''People affected by nchronic''',icon='📌')
    st.snow()
    # Step 1: Check unique values
    print("Unique values in 'nchronic':", df['nchronic'].unique())
    print("Unique values in 'lchronic':", df['lchronic'].unique())

    # Step 2: Distribution of 'nchronic' and 'lchronic'
    fig_nchronic = px.histogram(df, x='nchronic', color_discrete_sequence=['skyblue'],
                                title='Distribution of Nchronic')
    fig_lchronic = px.histogram(df, x='lchronic', color_discrete_sequence=['salmon'],
                                title='Distribution of Lchronic')
    st.plotly_chart(fig_nchronic)
    st.plotly_chart(fig_lchronic)

    # Step 3: Compare average number of visits for different values of 'nchronic' and 'lchronic'
    avg_visits_by_nchronic = df.groupby('nchronic')['visits'].mean().reset_index()
    avg_visits_by_lchronic = df.groupby('lchronic')['visits'].mean().reset_index()

    fig_avg_visits_nchronic = px.bar(avg_visits_by_nchronic, x='nchronic', y='visits', color_discrete_sequence=['lightgreen'],
                                     title='Average Number of Visits by Nchronic')
    fig_avg_visits_lchronic = px.bar(avg_visits_by_lchronic, x='lchronic', y='visits', color_discrete_sequence=['lightcoral'],
                                     title='Average Number of Visits by Lchronic')

    fig_avg_visits_nchronic.update_layout(xaxis_title='Nchronic', yaxis_title='Average Number of Visits')
    fig_avg_visits_lchronic.update_layout(xaxis_title='Lchronic', yaxis_title='Average Number of Visits')

    st.plotly_chart(fig_avg_visits_nchronic)
    st.plotly_chart(fig_avg_visits_lchronic)
    st.success('Success!')



if __name__ == '__main__':
    main()
