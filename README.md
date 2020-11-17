<h1 align="center">Problem Statement</h1>
Two types of pizza: regular, square (shapes)
* pizza can have many toppings, toppings can be cheese, tomato, capsicum, onion, corn and so on.
* pizza can be in multiple sizes: small, medium, large

API's to be created based on the above database creation :-(Django, python and rest API's)
* create API to create a regular pizza and a square pizza
* create API to list all the stored pizza
* create API to filter the pizza based on size, type
* create API to delete any of the listed pizza
When Pizza is listed in the API it should also contain information about all the toppings it has.


Built with (but not limited to) :
   * [django](https://www.djangoproject.com/)
   * [djangorestframework](https://www.django-rest-framework.org/)
   


## Setup

1. `git clone gh repo clone Mayank-Bhatt-450/pizza_API`
2. `cd `
3. `pip install -r requirements.txt` 
   _or place virtual environment and then install_
4. `manage.py runserver`

## Usage

**Example Response**
To list all the stored pizza


* GET : `http://localhost//:8000`


```json
[
    {
        "id": 2,
        "pizza_type": "square",
        "pizza_size": "medium",
        "toppings": "cheese, tomato"
    },
    {
        "id": 3,
        "pizza_type": "regular",
        "pizza_size": "large",
        "toppings": "capsicum, onion, corn"
    },
    {
        "id": 4,
        "pizza_type": "square",
        "pizza_size": "small",
        "toppings": "onion, corn"
    }
]
```
**Example Response**
To create a regular pizza and a square pizza

* GET : `http://localhost//:8000/search/<search variable like small or regular>

To filter the pizza based on size, type
  ```
`Do replace the <JWT> in the above request with the token you have acquired.`

```json
[
    {
        "id": 4,
        "pizza_type": "square",
        "pizza_size": "small",
        "toppings": "onion, corn"
    }
]
```
To delete any of the listed pizza
* DELETE : `http://localhost//:8000/<id>`

To update any of the listed pizza
* PUT: `http://localhost//:8000/<id>`

## License
MIT
