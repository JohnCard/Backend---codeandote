**List items**

-   **Endpoint** `/ecommerce/item-api/items/`
-   **Method** `GET`
-   **Description** List every items by json formats
-   **Response body**

```json
[
    {
        "name": "College behind alone.",
        "description": "Look Congress short scientist particularly. Six why gas while skin light job unit. Product home speech population then term decide goal.\nWrong step north generation first marriage assume. More sell risk keep property page fear.",
        "price": "797.97",
        "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_t.png"
    },
    {
        "name": "Memory trial week past.",
        "description": "But leg account win. Have entire call forget away apply let involve. View air mission traditional especially billion.\nStill campaign yourself site. Positive go result section study follow skin.",
        "price": "433.79",
        "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://fakestoreapi.com/img/71kWymZ%2Bc%2BL._AC_SX679_t.png"
    }
]
```

**List items**

-   **Endpoint** `/ecommerce/gallery`
-   **Method** `GET`
-   **Description** Getting all data from Product model database by json formats
-   **Response body**

```json
{
    "count": 76,
    "next": "http://127.0.0.1:8000/ecommerce/gallery?page=2",
    "previous": null,
    "results": [
        {
            "id": 52,
            "name": "ZenGo Likely T-Shirt",
            "description": "This product combines high performance with long-lasting battery. Designed for comfort and efficiency.",
            "price": "624124.66",
            "categories": [
                {
                    "id": 32,
                    "name": "Libros"
                },
                {
                    "id": 28,
                    "name": "Rosa"
                },
                {
                    "id": 8,
                    "name": "Club"
                }
            ],
            "image": "http://127.0.0.1:8000/https%3A/fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2t.png"
        }
        ...
    ]
}
```

**Product category filters**

-   **by category** `/ecommerce/gallery-filters?ordering=price,stock&categories__in=&price_range_min=&price_range_max=&name=`
-   **Method** `GET`
-   **Description** Filtering items
-   **Respoonse body**

```json
{
    "count": 2,
    "next": "http://127.0.0.1:8000/ecommerce/gallery-filters?categories__in=&name=&ordering=&page=2&price_range_max=&price_range_min=",
    "previous": null,
    "results": [
        {
            "id": 30,
            "name": "College behind alone.",
            "description": "Look Congress short scientist particularly. Six why gas while skin light job unit. Product home speech population then term decide goal.\nWrong step north generation first marriage assume. More sell risk keep property page fear.",
            "price": "797.97",
            "categories": [
                {
                    "id": 32,
                    "name": "Libros"
                },
                {
                    "id": 28,
                    "name": "Rosa"
                },
                {
                    "id": 8,
                    "name": "Club"
                }
            ],
            "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_t.png",
            "stock": 8
        },
        {
            "id": 29,
            "name": "Memory trial week past.",
            "description": "But leg account win. Have entire call forget away apply let involve. View air mission traditional especially billion.\nStill campaign yourself site. Positive go result section study follow skin.",
            "price": "433.79",
            "categories": [
                {
                    "id": 31,
                    "name": "Santa"
                },
                {
                    "id": 30,
                    "name": "Países"
                },
                {
                    "id": 22,
                    "name": "Unión"
                }
            ],
            "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://fakestoreapi.com/img/71kWymZ%2Bc%2BL._AC_SX679_t.png",
            "stock": 10
        }
    ]
}
```

**Retrieve item by its id**

-   **Endpoint** `/ecommerce/gallery/<int:id>`
-   **Method** `GET`
-   **Response body**

```json
{
    "id": 20,
    "name": "Nation attack card usually.",
    "description": "Up peace place. Why learn baby central prove where. Trouble thought rise.\nTown attack art order want significant sell let. Year week two easy class small.\nEntire money black fish Republican around since. Still agree argue conference thought order.",
    "price": "1745.64",
    "categories": [
        {
            "id": 27,
            "name": "Puedo"
        },
        {
            "id": 25,
            "name": "Psoe"
        },
        {
            "id": 8,
            "name": "Club"
        }
    ],
    "image": "https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_t.png",
    "stock": 10
}
```

**Create item**

-   **Endpoint** `/ecommerce/gallery-create`
-   **Method** `POST`
-   **Description** Creates a new Product instance
-   **Request body**

```json
{
    "name": "Type item name",
    "description": "Type a description for your item",
    "price": 27348,
    "categories": [
        {
            "id": 32,
            "name": "Libros"
        },
        {
            "id": 28,
            "name": "Rosa"
        },
        {
            "id": 8,
            "name": "Club"
        }
    ]
}
```

-   **Response body**

```json
{
    "name": "Type item name",
    "description": "Type a description for your item",
    "price": "27348.00",
    "categories": [
        {
            "id": 32,
            "name": "Libros"
        },
        {
            "id": 28,
            "name": "Rosa"
        },
        {
            "id": 8,
            "name": "Club"
        }
    ],
    "image": "http://127.0.0.1:8000/https%3A/fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_t.png"
}
```

**Update item by its id**

-   **Endpoint** `/ecommerce/gallery/<int:id>`
-   **Method** `PUT`
-   **Request body**

```json
{
    "name": "Type item update name",
    "description": "This is an example update data for this item",
    "price": 94572,
    "categories": [
        {
            "id": 32,
            "name": "Libros"
        },
        {
            "id": 28,
            "name": "Rosa"
        },
        {
            "id": 8,
            "name": "Club"
        }
    ]
}
```

-   **Response body**

```json
{
    "name": "Type item update name",
    "description": "This is an example update data for this item",
    "price": "94572.00",
    "image": "http://127.0.0.1:8000/https%3A/fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_t.png",
    "categories": [
        {
            "id": 32,
            "name": "Libros"
        },
        {
            "id": 28,
            "name": "Rosa"
        },
        {
            "id": 8,
            "name": "Club"
        }
    ]
}
```

**Delete item**

-   **Endpoint** `/ecommerce/gallery/<int:id>`
-   **Method** `DELETE`

-   **Response body only if the specified ID does not exist in the gallery. This applies to the GET (Retrieve), PUT, and DELETE methods for ecommerce/gallery/<int:id> endpoint**

```json
{
    "detail": "No Product matches the given query."
}
```

**Add item to shopping cart by its id**

-   **Endpoint** `/ecommerce/add-item/<int:id>`
-   **Method** `POST`
-   **Response body (if this item is still available)**

```json
{
    "ok": true,
    "stock_cart": 3,
    "stock_gallery": 8
}
```

-   **Response body (if this item is not available anymore)**

```json
{
    "ok": "False",
    "message": "Sold out"
}
```

**Remove item from shopping cart by its id**

-   **Endpoint** `/ecommerce/add-item/<int:id>`
-   **Method** `DELETE`
-   **Response body (if this item is still in shopping cart)**

```json
{
    "ok": true,
    "stock_cart": 1,
    "stock_gallery": 7
}
```

-   **Response body (if this item is not in shopping cart anymore)**

```json
{
    "ok": "False",
    "message": "Not found item"
}
```

**Buy item by its id**

-   **Endpoint** `/ecommerce/buy-item/<int:id>`
-   **Method** `POST`
-   **Response body (if this item is in shopping cart)**

```json
{
    "ok": true,
    "stock_collection": 1,
    "new_collection_item": true/false,
    "balance": 77686.28
}
```

-   **Response body (if this item is not in shopping cart anymore)**

```json
{
    "ok": "False",
    "message": "Not found item"
}
```

**Return item by its id**

-   **Endpoint** `/ecommerce/buy-item/<int:id>`
-   **Method** `DELETE`
-   **Response body (if this item is still in collection)**

```json
{
    "ok": true,
    "stock_collection": 1,
    "stock_gallery": 6,
    "balance": 77686.28
}
```

-   **Response body (if this item was removed from collection)**

```json
{
    "ok": true,
    "message": "Removed item",
    "stock_gallery": 8,
    "balance": 77892.05
}
```

-   **Response body (if item was not found in collection)**

```json
{
    "ok": "False",
    "message": "Not found item"
}
```

**List categories**

-   **Endpoint** `/ecommerce/categories`
-   **Method** `GET`
-   **Description** List every category instances by json formats
-   **Response body**

```json
[
    {
        "id": 35,
        "name": "Aún"
    },
    {
        "id": 34,
        "name": "Rodríguez"
    },
    {
        "id": 2,
        "name": "Administración"
    },
    {
        "id": 1,
        "name": "Propia"
    }
]
```

**Excel report - gallery data**

-   **Endpoint** `/ecommerce/gallery-report`
-   **Method** `GET`
-   **Description** Retrieves a report in excel format about available items in gallery, graphs, tables
-   **Response body**

```json
{
	"file": "<file_data>"
}
```
