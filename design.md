This is a Python SDK for the LOTR database.

# Define the interface

First we start off by defining our interface, how we want users of this SDK to use our package. It should follow conventions often seen in the language. Pythonistas expect snake case and easy to work with clients.

```python
from lotr import client

client = Client(key=<api_key>)

movies = client.get_movie()
for movie in movies:
    id = movie._id
    name = movie.name
    runtime = movie.runtime_in_minutes
    budget = movie.budget_in_millions
    ...
    quotes = movie.quotes()
    
```

# Some nice to have features:

- We could simply wrap the Requests library and let the user manipulate a dictionary, but that's not fun at all and negates the need for a SDK. This SDK wraps each of the entities in wrapper classes that expose attributes in snake case and has helper methods to fetch related entities. For example:

```python
client = Client(key=<api_key>)
movie = client.get_movie(movie_id="5cd95395de30eff6ebccde5d")
movie.name # The Return of the King
movie.budget_in_millions # 281
quotes = movie.quotes()
first_quote = quotes[0]
first_quote.dialog # "Deagol!"
```

# Additional features to implement:

I explicitly didn't implement pagination in this SDK because pagination and page size are concepts that should be invisible to the user. 

The SDK should manage what is fetched from the API and lazily load in for endpoints that fetch all elements of a specific entity.  

One strawman implementation is to set the pagesize to something small like 10-20 elements. Then provide an iterator interface that fetches additional items when needed. 


