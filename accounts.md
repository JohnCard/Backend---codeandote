# App Accounts - Technical Description

## Main Components

### 1. **Models**

#### User
Custom user model that inherits from `AbstractBaseUser`, `PermissionsMixin`, and `TrackingModel`.

**Main fields:**
- `username` (CharField): Unique username
- `first_name` and `last_name` (CharField): First name and last name
- `email` (EmailField): Unique email address (primary authentication field)
- `is_staff` (BooleanField): Indicates whether the user is a staff member
- `is_active` (BooleanField): Indicates whether the account is active
- `balance` (DecimalField): User balance (default 75000)
- `image` (ImageField): User's profile picture
- `description` (TextField): Brief profile description
- `email_verified` (BooleanField): Indicates whether the email has been verified
- `date_joined` and `last_login` (DateTimeField): Creation and last login dates

**Configuration:**
- `USERNAME_FIELD = "email"`: Email-based authentication
- `REQUIRED_FIELDS = ["username"]`

### 2. **Serializers**

#### UserSerializer
ModelSerializer serializer for the User model.

**Serialized fields:**
- `id`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `balance`, `image`

**Custom method:**
- `get_image()`: Validates and returns the URL of the profile image

### 3. **Views**

#### UserAPIView
View that inherits from `RetrieveAPIView` to retrieve data for a specific user by their ID.

- **Lookup field:** `id`
- **Serializer:** `UserSerializer`
- **Method:** GET
- **Response:** Serialized User object

#### UserReturn
Generic view that returns complete information about the authenticated user, including:
- Basic user data
- List of shopping cart items
- List of saved collections
- Categories associated with products

### 4. **URLs**

```python
path('user/<int:id>', UserAPIView.as_view(), name='user')  # Retrieve user by ID
path('user', UserReturn.as_view(), name='user-return')     # Retrieve authenticated user info
```

---

## Endpoint: `/accounts/user`

### Request
```
GET /accounts/user
Method: GET
```

### Response
```json
{
  "ok": true,
    "id": 1,
    "username": "John_Card_django_veloper",
    "name": "Juan Carlos",
    "last_name": "Sánchez Martínez",
    "email": "johncard962@gmail.com",
    "is_staff": true,
    "is_active": true,
    "balance": 77892.05,
    "description": "Dark area return skin none east range responsibility. Next here away half simply.\nOwn lawyer pull although method. Society assume half effort indicate skill party use.\nYour thing north a billion team.\nSend skill perhaps.",
    "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://cdn-icons-png.freepik.com/512/9398/9398920.png",
    "created_at": "26/03/2026",
    "items": [
        {
            "id": 13,
            "name": "With live.",
            "description": "Stand environmental cause win.\nAway authority administration think. Along risk both pressure over live onto. Hotel evening less serious threat food.\nMust her beautiful car save tax candidate.",
            "price": 553.2,
            "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_t.png",
            "stock": 4,
            "categories": [
                "Libros",
                "Para",
                "Lado"
            ],
            "quantity": 5
        },
        {
            "id": 30,
            "name": "College behind alone.",
            "description": "Look Congress short scientist particularly. Six why gas while skin light job unit. Product home speech population then term decide goal.\nWrong step north generation first marriage assume. More sell risk keep property page fear.",
            "price": 797.97,
            "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_t.png",
            "stock": 8,
            "categories": [
                "Libros",
                "Rosa",
                "Club"
            ],
            "quantity": 1
        }
    ],
    "collection": [
        {
            "id": 22,
            "name": "Person within.",
            "description": "Personal hospital development budget certain role. Heart cold person military show nearly perform. Condition individual media kind leave involve.\nQuite experience old example deep mouth. Program if class because.",
            "price": 266.22,
            "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://fakestoreapi.com/img/61mtL65D4cL._AC_SX679_t.png",
            "categories": [
                "N",
                "Madre",
                "Cantidad"
            ],
            "quantity": 3
        },
        {
            "id": 30,
            "name": "College behind alone.",
            "description": "Look Congress short scientist particularly. Six why gas while skin light job unit. Product home speech population then term decide goal.\nWrong step north generation first marriage assume. More sell risk keep property page fear.",
            "price": 797.97,
            "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_t.png",
            "categories": [
                "Libros",
                "Rosa",
                "Club"
            ],
            "quantity": 4
        }
    ]
}

```

**Description** Retrieves all information associated with the currently authenticated user

---

## Endpoint: `user/<int:id>`

### Request
```
GET /accounts/user/1
Method: GET
```

### Response
```json
{
  "id": 1,
  "username": "John_Card_django_veloper",
  "first_name": "Juan Carlos",
  "last_name": "Sánchez Martínez",
  "email": "johncard962@gmail.com",
  "is_staff": true,
  "is_active": true,
  "balance": 77892.05,
  "image": "https://cdn-icons-png.freepik.com/512/9398/9398920.png"
}
```

**Description:** This endpoint retrieves the public data of a specific user by their ID. It returns the serialized user information without requiring authentication
