# README #

* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### What is this repository for? ###

* FlexEngage ReactJS UI Challange!

### How do I get set up? ###
Make sure to have python3.5+ installed on your machine

Run run-local.sh to start metrics service. The service will start up locally on
port 5000.

Once running API Docs can be found at http://localhost:5000/docs

### GOAL 

Write a ReactJS metrics application that utilizes the API found in this repository.

The application should behave and look in the following ways:

* 2 views, a dashboard and metric details view
* The dashboard page should contain a list of boxes with the metric names written on each box. At the top of the page, a button should exist, titled Create Metric, that when clicked reveals a modal that allows users to create a new metric.
* Each box should contain a delete button allowing the user to delete the metric.
* Each box should contain an open button that when clicked, routes the user the metrics details view that displays a table with 2 columns, one for the value field of a metric recordset object and the other for the timestamp field of a metric recordset object.
* From this view the user should be able to click on an add value button located above the table allowing the user to add a value to the metric recordset via a modal.
* From the recordset view a button should exist to take the user back to the dashboard.
* Make sure all timestamps are formatted as 04/12/2021 08:00:12

### Definitions ###

* A Metric is a simple object with an id, name, and timestamp. To create one, just a name needs to be provided as the 
API will auto generate an id and timestamp representing when the metric was created.
  
* A MetricValue is a value that can be assigned to a metric at any given point. Representing a measurement taken at a 
particular point in time.
  
* A MetricRecordset is a list of MetricValues that belong to a metric. 


### Who do I talk to? ###
* Brian Ocasio