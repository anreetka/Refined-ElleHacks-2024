# Refined-ElleHacks-2024

Note: This is a refined project as the rendering was not working for the initial version that was submitted in the hackathon. The original version for our WinterWay project submission for ElleHacks 2024 can be found [here](https://github.com/anreetka/Elle-Hacks-2024). 

## Inspiration
- How many times have you stood standing at the TTC bus stop, in snow and without a shed? 
- Hands aching by the weight of groceries, making it even tougher for the elderly to travel, and the specially abled to take buses.

## Project Description
Winter Way is a web application designed to assist users in finding safe routes during inclement weather, particularly in extremely cold conditions when waiting at exposed bus stops can pose risks to health.

### What It Does
- Provides safe routes for users during extreme weather conditions.
- Integrates real-time data on shelter availability and bus schedules.
- Dynamically generates routes optimizing safety and comfort.

### How It Works
- Built backend using Flask, Python and REST API calls
- Developed frontend with JavaScript, HTML, CSS
- Utilizes independently developed algorithm for computing transit routes.
- Integration of geocoding, Google's Routes and Directions APIs.

## Challenges
- Inaugural collaboration for the team led to learning curve challenges.
- Rendering parsed data from the backend proved difficult.
- Timing issues and integration challenges arose due to rapid implementation.

## Accomplishments
- Half of the team participated in their first hackathon.
- Successful completion of the project through motivation and adaptability.
- Roles were naturally divided, and every aspect of development was taken seriously.

## Learning Outcomes
- Prioritization of frontend-backend communication for smoother integration.
- Successful completion despite last-minute pivots.

## Next Steps
- Enhancements to APIs for improved algorithm efficiency.
- Introduction of adaptive design and visual aesthetics enhancements.
- Testing across browsers and versions for consistency.
- Backend data manipulation for user-friendliness.

# Project Setup

Please make sure to follow each step to be able to set up the project for full functionality:

## Installation

```bash
pip install -r requirements.txt
```

Note: In order to run this project, you will need to create a .env file and use Google maps API key to fetch results.

## Google API Key 
Here's a list of services you will have enable to be able to render the final product:

- [Routes API](https://developers.google.com/maps/documentation/routes)
- [Directions API](https://developers.google.com/maps/documentation/directions)
- [Geolocation API](https://developers.google.com/maps/documentation/geolocation/overview)
- [Geocoding API](https://developers.google.com/maps/documentation/geocoding)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
