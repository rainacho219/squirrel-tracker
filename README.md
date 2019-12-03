__<h1>Squirrel Tracker: Django-Based  Web Application for Tracking Central Park Squirrel Census Data</h1>__

__<h2>Group Name: Project Group 11</h2>__  
__<h2>Group Members: Raina Cho & Jenny Park</h2>__  
__<h2>Tools for Analytics Section 1</h2>__
__<h2>UNIs: [jp3256, hc3130]</h2>__  

<h3>Included Management Commands</h3>
1. import_squirrel_data
	- Command to import 2018 Central Park Squirrel Census data in CSV format
	- $ python manage.py import_squirrel_data /path/to/importfile.csv
2. export_squirrel_data
	- Command to export data in CSV format
	- $ python manage.py export_squirrel_data /path/to/exportfile.csv

<h3>Included Views</h3>
1. View with a map showing the location of squirrel sightings (located at: /map)
2. View listing all squirrel sightings with links to edit and add squirrel sightings (located at: /sightings)
3. View for updating a particular squirrel sighting (located at: /sightings/unique-squirrel-id)
4. View for creating a new sighting (located at: /sightings/add)
5. View for deleting a particular sighting (located at: /sightings/unique-squirrel-id)
6. View showing general statistics about the squirrel sightings (located at: /sightings/stats)

<h3>Supported Fields</h3>
- Latitude
- Longitude
- Unique Squirrel ID
- Shift
- Date
- Age
- Primary Fur Color
- Location
- Specific Location
- Running
- Chasing
- Climbing
- Eating
- Foraging
- Other Activities
- Kuks
- Quaas
- Moans
- Tail flags
- Tail twitches
- Approaches
- Indifferent
- Runs from
