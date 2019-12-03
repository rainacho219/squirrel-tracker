__<h1>Squirrel Tracker: Django-Based  Web Application for Tracking Central Park Squirrel Census Data</h1>__

__<ul><li>Group Name: Project Group 11</li>__  
__<li>Group Members: Raina Cho & Jenny Park</li>__  
__<li>Tools for Analytics Section 1</li>__
__<li>UNIs: [jp3256, hc3130]</li></ul>__  

<h3>Included Management Commands</h3>
<h4>import_squirrel_data.py </h4><ul>
<li>Command to import 2018 Central Park Squirrel Census data in CSV format</li>
<li>$ python manage.py import_squirrel_data /path/to/importfile.csv</li>
</ul>

<h4>export_squirrel_data</h4>
<ul><li>Command to export data in CSV format</li>
<li>$ python manage.py export_squirrel_data /path/to/exportfile.csv</li>
</ul>

<h3>Included Views</h3>
<ul><li>View with a map showing the location of squirrel sightings (located at: /map)</li>
<li>View listing all squirrel sightings with links to edit and add squirrel sightings (located at: /sightings)</li>
<li>View for updating a particular squirrel sighting (located at: /sightings/unique-squirrel-id)</li>
<li>View for creating a new sighting (located at: /sightings/add)</li>
<li>View for deleting a particular sighting (located at: /sightings/unique-squirrel-id)</li>
<li>View showing general statistics about the squirrel sightings (located at: /sightings/stats)</li></ul>

<h3>Supported Fields</h3>
<ul><li>Latitude</li>
<li>Longitude</li>
<li>Unique Squirrel ID</li>
<li>Shift</li>
<li>Date</li>
<li>Age</li>
<li>Primary Fur Color</li>
<li>Location</li>
<li>Specific Location</li>
<li>Running</li>
<li>Chasing</li>
<li>Climbing</li>
<li>Eating</li>
<li>Foraging</li>
<li>Other Activities</li>
<li>Kuks</li>
<li>Quaas</li>
<li>Moans</li>
<li>Tail flags</li>
<li>Tail twitches</li>
<li>Approaches</li>
<li>Indifferent</li>
<li>Runs from</li></ul>
