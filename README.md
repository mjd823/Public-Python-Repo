# Public-Python-Repo
Machine Learning Program for students 
Personalized and Collaborative Learning Program for Children
This program provides personalized and collaborative learning resources and activities for children. It uses machine learning algorithms to find resources and projects that are most similar to the children's interests and skills, and generates activity suggestions based on the available resources.

Requirements
Python 3.6 or higher
NumPy
scikit-learn


Installation
To install the required libraries, run the following command:
pip install numpy scikit-learn


Usage
The program consists of the following functions:

personalized_learning(child, database)
This function retrieves resources related to a child's interests and skills, and finds the ones that are most similar to the child's interests and skills using the KMeans algorithm.

Parameters
child: A dictionary containing the following keys:
interests: A list of the child's interests.
skills: A list of the child's skills.
database: A database object that provides access to the resources.
Returns
A list of resources that are most similar to the child's interests and skills.

collaborative_learning(children, database)
This function retrieves resources and family projects suitable for collaborative learning, and finds the ones that are most similar to the children's interests and skills using the NearestNeighbors algorithm.

Parameters
children: A list of dictionaries, each containing the following keys:
interests: A list of the child's interests.
skills: A list of the child's skills.
database: A database object that provides access to the resources.
Returns
A tuple containing:

A list of resources that are most similar to the children's interests and skills.
A list of family projects that are suitable for collaborative learning.
filter_by_age(children, resources)
This function filters the resources to only include ones that are suitable for the children's ages.

Parameters
children: A list of dictionaries, each containing the following keys:
age: The child's age.
resources: A list of dictionaries, each containing the following keys:
age_range: A tuple containing the minimum and maximum ages for which the resource is suitable.
Returns
A list of resources that are suitable for the children's ages.

generate_activity_suggestions(children, resources)
This function generates a list of activities based on the children's interests and the resources available.

Parameters
children: A list of dictionaries, each containing the following keys:
interests: A list of the child's interests.
resources: A list of dictionaries, each containing the following keys:
interests: A list of the resource's relevant interests.
activities: A list of activities related to the resource.
Returns
A list of activities based on the children's interests and the available resources.

filter_by_interest(children, resources)
This function filters the resources to only include ones that are relevant to the children's interests.





PERSONALIZED LEARNING PAGE
This HTML page includes a form that allows users to enter their interests and skills, and a button to submit the form. It also includes a div element with the ID results that will be used to display the results of the personalized_learning function.

then use JavaScript to send an HTTP request to Python script when the form is submitted, and update the results element with the returned data:

This code listens for the submit event on the form element, and prevents the default form submission behavior. It then gets the values of the interests and skills inputs and constructs a JavaScript object with these values. It uses the fetch function to send an HTTP POST request to the Python script with the data as the request body, and sets the Content-Type header to application/json to indicate that the data is in JSON format.

When the response is received, the code parses the response as JSON and updates the results element with the data.

