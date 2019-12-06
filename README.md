# NYCity Watch 
#### A site about NYC public safety
See it here https://nycw.herokuapp.com  
  
Note: The site is still a work in progress.  

## Recent Updates
* New repository created to consolidate both github and heroku remotes
* Updated web scraping code to account for Pix11 site redesign
* Added AI chatbot component finally!  This is still a work in progress, the AI chat function only works when connected to the local server.  A Small step but progress nonetheless!    

Future updates will include:
* Updates to responsiveness
* Enhanced map buttons and navigation
* Updates to news scraping to include real time images
* Community forum section
* AI Chat - Dockerized chat component
* And more

## About Us
This project was developed as a class project for the May 2019 Data Science program at Rutgers University. The group consisted of three members listed below.

Ankit Rana    
Charlie Blasi  
Anonymous

## The Project
Our goal for this project was to look at various factors of public safety within New York City. We wanted to gather as much data as we could find from publicly available sources including Datasets, API's, and Websites.

With data sources in hand we were able to create and deploy a functioning web application. Below are the tools we used to perform both the server-side and front-end operations.

* Python/Flask: The code to scrape news and social media information from various news outlets was written using Python. We then used Flask deploy the application to the web.
* MongoDB: MongoDB was used as the database to run CRUD operations on the scraped data.
* Leaflet: The Leaflet JavaScript library was used to display our data as overlays on an interactive map provided by Mapbox.
* Plotly: The Plotly library was used to create the interactive graphs used to display EMS Response Times.

## For more details check out the documentation section of the site [here](https://nycw.herokuapp.com/documentation).
