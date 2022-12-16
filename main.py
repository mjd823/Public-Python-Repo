import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors

def personalized_learning(child, database):
    """
    Retrieves resources related to the child's interests and skills, and finds the ones
    that are most similar to the child's interests and skills using the KMeans algorithm.
    """
    try:
        interests = child['interests']
        skills = child['skills']

        # Search the database for resources related to the child's interests and skills
        resources = database.search(interests=interests, skills=skills)

        # Create a vector representation of the child's interests and skills
        child_vector = create_vector(interests, skills)

        # Use the KMeans algorithm to find resources that are most similar to the child's interests and skills
        kmeans = KMeans(n_clusters=len(resources))
        kmeans.fit(resources)
        closest_resources = kmeans.predict(child_vector)

        return closest_resources
    except Exception as e:
        print("An error occurred while trying to retrieve personalized learning resources:", e)
        return []

def collaborative_learning(children, database):
    """
    Retrieves resources and family projects suitable for collaborative learning, and finds
    the ones that are most similar to the children's interests and skills using the NearestNeighbors algorithm.
    """
    try:
        # Search the database for resources and family projects that are suitable for collaborative learning
        resources = database.search(collaborative=True)
        family_projects = database.search(type='family project', collaborative=True)

        # Create a vector representation of the children's interests and skills
        children_vectors = [create_vector(child['interests'], child['skills']) for child in children]

        # Use the NearestNeighbors algorithm to find the resources and family projects that are most similar to the children's interests and skills
        nn = NearestNeighbors(n_neighbors=len(resources) + len(family_projects))
        nn.fit(children_vectors)
        closest_resources, _ = nn.kneighbors()

        return closest_resources, family_projects
    except Exception as e:
        print("An error occurred while trying to retrieve collaborative learning resources:", e)
        return [], []

def filter_by_age(children, resources):
    """
    Filters the resources to only include ones that are suitable for the children's ages.
    """
    try:
        # Only return resources that are suitable for the children's ages
        suitable_resources = []
        for child in children:
            if child['age'] < 10:
                suitable_resources.extend([resource for resource in resources if resource['age_range'][0] <= child['age'] <= resource['age_range'][1]])

        return suitable_resources
    except Exception as e:
        print("An error occurred while trying to filter resources by age:", e)
        return []

def generate_activity_suggestions(children, resources):
    """
    Generates a list of activities based on the children's interests and the resources available.
    """
    try:
        # Create a list of activities based on the children's interests
        activities = []
        for child in children:
            for resource in resources:
                if set(child['interests']).intersection(set(resource['interests'])):
                    activities.extend(resource['activities'])

        return activities
    except Exception as e:
        print("An error occurred while trying to generate activity suggestions:", e)
        return []

def filter_by_interest(children, resources):
    """
    Filters the resources to only include ones that are relevant to the children's interests.
    """
    try:
        # Return a list of the resources that are relevant to the children's interests
        relevant_resources = []
        for child in children:
            for resource in resources:
                if set(child['interests']).intersection(set(resource['interests'])):
                    relevant_resources.append(resource)

        return relevant_resources
    except Exception as e:
        print("An error occurred while trying to filter resources by interest:", e)
        return []

def create_vector(interests, skills):
    """
    Creates a vector representation of the interests and skills.
    """
    # Create a vector representation of the interests and skills
    vector = np.zeros(len(interests) + len(skills))
    for i, interest in enumerate(interests):
        vector[i] = 1
    for i, skill in enumerate(skills):
        vector[i + len(interests)] = 1

    return vector
