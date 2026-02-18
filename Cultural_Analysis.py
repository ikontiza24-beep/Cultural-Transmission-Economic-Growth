# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 17:35:42 2026

@author: dkont
"""



#ASSIGNMENT 1
import pandas as pd

# QUESTION A
file_path = r"C:\Users\dkont\Downloads\Trends_VS_1981_2022_stata_v4_0.dta"
my_vars = ['A042', 'A040', 'A029'] # Obedience, Religion, Independence
cols_to_load = ['COW_ALPHA', 'S002VS'] + my_vars

print("Loading raw numeric data for inspection... (Please wait)")
df_num = pd.read_stata(file_path, columns=cols_to_load, convert_categoricals=False)

print("Loading categorical data for inspection... (Please wait)")
df_cat = pd.read_stata(file_path, columns=cols_to_load, convert_categoricals=True)


#(NULL CHECKS)
print("\n--- NULL VALUES COUNT (RAW NUMBERS) ---")
print(df_num.isnull().sum())

print("\n--- NULL VALUES COUNT (CATEGORICAL STRINGS) ---")
print(df_cat.isnull().sum())



#DATA CLEANING & FILTERING
print("\nCleaning data using raw numbers...")
df = df_num.copy()

# Drop rows where the country code or wave is completely missing
df = df.dropna(subset=['COW_ALPHA', 'S002VS'])

# Filter out negative values ("Don't Know", "No Answer", etc.) 
# Note the indentation here! This is what caused your SyntaxError.
for var in my_vars:
    df = df[df[var] >= 0]


#CREATING THE TIME PERIODS
def assign_period(wave):
    if wave in [1, 2, 3, 4]:
        return '1981-2004'
    elif wave in [5, 6, 7]:
        return '2005-2022'
    else:
        return 'Unknown'

df['Period'] = df['S002VS'].apply(assign_period)

#Duplicate data to create the overall 1981-2022 average
df_overall = df.copy()
df_overall['Period'] = '1981-2022'
df_combined = pd.concat([df, df_overall], ignore_index=True)

# Remove any 'Unknown' periods just in case
df_combined = df_combined[df_combined['Period'] != 'Unknown']


#CALCULATE THE AVERAGES
final_data = df_combined.groupby(['COW_ALPHA', 'Period'])[my_vars].mean().reset_index()

final_data = final_data.rename(columns={
    'A042': 'Obedience',
    'A040': 'Religious_Faith',
    'A029': 'Independence'
})

print("\n--- STEP A COMPLETED: FIRST 10 ROWS OF FINAL DATA ---")
print(final_data.head(10))







#QUESTION B
import plotly.express as px
import os


#Save maps in pc
save_directory = r"C:\Users\dkont\Downloads\WVS_Maps"

#create WVS_Maps
if not os.path.exists(save_directory):
    os.makedirs(save_directory)


#9 STATIC MAPS
# 3 time periods and-3 variables to loop through
periods = ['1981-2004', '2005-2022', '1981-2022']
map_variables = ['Obedience', 'Religious_Faith', 'Independence']

print(f"\nGenerating 9 maps and saving them to: {save_directory}")

#Go through each time period
for period in periods:
    
    #Keep only the rows for the current period in the loop
    df_period = final_data[final_data['Period'] == period]
    
    #Go through each of the 3 traits
    for variable in map_variables:
        
        
        fig = px.choropleth(
            df_period, 
            locations="COW_ALPHA",        # The column with the 3-letter country codes
            color=variable,               # color intensity
            hover_name="COW_ALPHA",       # Shows country code when hover your mouse
            color_continuous_scale="Viridis", 
            title=f"Percentage valuing {variable} in children ({period})"
        )
        
        # beaytify map
        fig.update_geos(showcountries=True, projection={"type": "natural earth"})
        
        # Create filenames
        filename = f"Map_{variable}_{period}.html"
        full_path = os.path.join(save_directory, filename)
        
        # Save the map as HTML file
        fig.write_html(full_path)
        
    
    
    
    
    
    
    
#QUESTION C

#interactice maps with slider
print("\nGenerating 3 interactive slider maps... (Please wait)")

# Sort chronologically so the slider moves in the right order
final_data = final_data.sort_values(by='Period')

for variable in map_variables:
    
    #Lock the color scale
    min_val = final_data[variable].min()
    max_val = final_data[variable].max()
    
    #Build the animated map
    fig = px.choropleth(
        final_data, 
        locations="COW_ALPHA",
        color=variable,
        hover_name="COW_ALPHA",
        animation_frame="Period",       
        color_continuous_scale="Viridis", 
        range_color=[min_val, max_val], 
        title=f"Evolution of '{variable}' as an Important Child Quality"
    )
    
    #Improve map projection
    fig.update_geos(showcountries=True, projection={"type": "natural earth"})
    
    # Adjust layout
    fig.update_layout(
        margin={"r":0,"t":40,"l":0,"b":0},
        coloraxis_colorbar_title_text="Percentage"
    )
    
    
    
    #set the frame to stay on screen for 2 seconds,and the transition to take 0.5 seconds.
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 2000
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
    # ---------------------------------------------
    
   
    filename = f"Interactive_Slider_{variable}.html"
    full_path = os.path.join(save_directory, filename)
    fig.write_html(full_path)
    
    




#QUESTION D

#Sort the data chronologically
final_data = final_data.sort_values(by='Period')

#interactive map
fig = px.choropleth(
    final_data, 
    locations="COW_ALPHA",
    color='Religious_Faith',
    hover_name="COW_ALPHA",
    hover_data=['Obedience', 'Independence'], 
    animation_frame="Period",       
    color_continuous_scale="Viridis", 
    range_color=[0, 1], 
    title="Master Map: Cultural Traits Evolution (Hover over countries for all data)"
)

#adjust map shape and the legend title
fig.update_geos(showcountries=True, projection={"type": "natural earth"})
fig.update_layout(
    margin={"r":0,"t":50,"l":0,"b":0},
    coloraxis_colorbar_title_text="Percentage"  # <-- THIS FIXES YOUR LEGEND!
)

#animation speed
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 2000
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500

#dropdown buttons
continent_buttons = [
    {"label": "🌍 World View", "method": "relayout", "args": [{"geo.scope": "world"}]},
    {"label": "🇪🇺 Europe", "method": "relayout", "args": [{"geo.scope": "europe"}]},
    {"label": "🌏 Asia", "method": "relayout", "args": [{"geo.scope": "asia"}]},
    {"label": "🌍 Africa", "method": "relayout", "args": [{"geo.scope": "africa"}]},
    {"label": "🌎 North America", "method": "relayout", "args": [{"geo.scope": "north america"}]},
    {"label": "🌎 South America", "method": "relayout", "args": [{"geo.scope": "south america"}]}
]

#add dropdown to the maps control panel
fig.update_layout(
    updatemenus=[
        fig.layout.updatemenus[0], 
        {
            "buttons": continent_buttons,
            "direction": "down",
            "showactive": True,
            "x": 0.05,
            "y": 1.15
        }
    ]
)

#HTML
filename = "Master_Map_Step_D.html"
full_path = os.path.join(save_directory, filename)
fig.write_html(full_path)








#QUESTION E
my_countries = ['USA','NOR','CHN']

#filtering the original dataset to include my countries only
df_line = df[df['COW_ALPHA'].isin(my_countries)].copy()

#dictionary to make the wave numbers year labels 
wave_dict = {
    1: '1981-1984',
    2: '1989-1993',
    3: '1994-1998',
    4: '1999-2004',
    5: '2005-2009',
    6: '2010-2014',
    7: '2017-2022'
}

#a new year column using our translation dictionary
df_line['Year'] = df_line['S002VS'].map(wave_dict)

#Calculate the percentages grouped by Country and Wave
line_data = df_line.groupby(['COW_ALPHA', 'Year', 'S002VS'])[my_vars].mean().reset_index()

#sort by the wave number so the timeline flows correctly
line_data = line_data.sort_values(by=['S002VS'])

variable_names = ['Obedience', 'Religious_Faith', 'Independence']

for var_code, var_name in zip(my_vars, variable_names):
    
    #build the line chart
    fig = px.line(
        line_data, 
        x='Year', 
        y=var_code, 
        color='COW_ALPHA', 
        markers=True,  
        title=f"Time Series Comparison: {var_name}",
        labels={var_code: 'Percentage (Show Column %)', 'COW_ALPHA': 'Country', 'Year': 'Survey Wave'}
    )
    
    #Force Plotly to treat the X-axis as a strict category timeline, otherwise the years wont be in correct order
    fig.update_layout(
        xaxis=dict(
            type='category', 
            categoryorder='array',
            categoryarray=[
                '1981-1984', '1989-1993', '1994-1998', 
                '1999-2004', '2005-2009', '2010-2014', '2017-2022'
            ]
        ),
        yaxis=dict(tickformat=".0%", range=[0, 1]),
        plot_bgcolor='white', 
        yaxis_gridcolor='lightgray' 
    )
    
    #HTML
    filename = f"LineChart_{var_name}.html"
    full_path = os.path.join(save_directory, filename)
    fig.write_html(full_path)
    
    





#question 3b


#exploratory

file_path = r"C:\Users\dkont\Downloads\Behavioral_assignment_1\QJE.dta"
gps_data = pd.read_stata(file_path)

print(gps_data.columns.tolist())


print(gps_data.head(5).to_string(index=False))


#mean per country
wvs_subset = final_data.groupby('COW_ALPHA')[['Obedience', 'Religious_Faith', 'Independence']].mean().reset_index()

#inner merge
merged_data = pd.merge(wvs_subset, gps_data, left_on='COW_ALPHA', right_on='ISO3', how='inner')
merged_data = merged_data.drop_duplicates(subset=['COW_ALPHA'])

#columns needed for the understanding of the correlation
wvs_vars = ['Obedience','Religious_Faith','Independence']
gps_vars = ['patienceQJE','risktaking','trustQJE','altruism','posrecip','negrecip']
all_vars = wvs_vars + gps_vars

print(merged_data[['COW_ALPHA'] + all_vars].head(10).to_string(index=False))


#corr matrix
corr_matrix = merged_data[all_vars].corr()

pd.set_option('display.max_columns', None)  # Δείξε όλες τις στήλες
pd.set_option('display.width', 1000)

print(corr_matrix.round(3))

#Heatmap
fig = px.imshow(
    corr_matrix, 
    text_auto=".2f", 
    aspect="auto",
    color_continuous_scale='RdBu_r', 
    zmin=-1, zmax=1,
    title="Correlation Matrix: WVS Variables vs. GPS Preferences (Falk et al. 2018)"
)

fig.update_layout(margin=dict(t=50, l=150, r=50, b=50))

save_directory = r"C:\Users\dkont\Downloads\Behavioral_assignment_1\WVS_Maps"

#Heatmap HTML 
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

heatmap_filename = "Correlation_Matrix_WVS_GPS.html"
heatmap_path = os.path.join(save_directory, heatmap_filename)
fig.write_html(heatmap_path)

print(f"\nΟ Θερμικός Χάρτης Συσχετίσεων αποθηκεύτηκε επιτυχώς στο:\n{heatmap_path}")
print("--- Η ΕΚΤΕΛΕΣΗ ΤΟΥ ΚΩΔΙΚΑ ΟΛΟΚΛΗΡΩΘΗΚΕ! ---")

