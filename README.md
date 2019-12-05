__<h1>Squirrel Tracker: Django-Based  Web Application for Tracking Central Park Squirrel Census Data</h1>__

<ul>
<li>Project Group 11, Section 1</li>
<li>UNIs: [jp3256, hc3130]</li>
<li>Raina Cho & Jenny Park</li>
<a href="https://jennyjihyuonpark-jp3256-tools.appspot.com/">https://jennyjihyuonpark-jp3256-tools.appspot.com/</a>
</ul>

<h2>Included Management Commands</h2>
<h3>1. import_squirrel_data </h3><ul>
<li>Command to import 2018 Central Park Squirrel Census data in CSV format</li>
<li>e.g. $ python manage.py import_squirrel_data /path/to/importfile.csv</li>
</ul>

<h3>2. export_squirrel_data</h3>
<ul>
<li>Command to export data in CSV format</li>
<li>e.g. $ python manage.py export_squirrel_data /path/to/exportfile.csv</li>
</ul>

<h2>Included Views</h2>
<ol>
<li>View with a map showing the location of squirrel sightings (located at: /map)</li>
<li>View listing all squirrel sightings with links to edit and add squirrel sightings (located at: /sightings)</li>
<li>View for updating a particular squirrel sighting (located at: /sightings/unique-squirrel-id)</li>
<li>View for creating a new sighting (located at: /sightings/add)</li>
<li>View for deleting a particular sighting (located at: /sightings/unique-squirrel-id)</li>
<li>View showing general statistics about the squirrel sightings (located at: /sightings/stats)</li>
</ol>

<h2>Supported Fields</h2>
<ul>
<li>Latitude</li>
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
<li>Runs from</li>
</ul>
