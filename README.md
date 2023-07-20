# store_manager_app
Project of practice with FastAPI Python
***
## Descripcion
En el proyecto se definen 3 modelos `item`, `client` y `sale` que estan involucradas en la gestion y venta de una tienda
***
## Modelos

| `item`                        | `client`               | `sale`                  |
|:----------------------------|:---------------------|:------------------------|
| `id` -> int                   | `id` -> int            | `id` -> int             |
| `name` -> str                 | `name` -> str          | `id_item` -> int        |
| `price` -> float              | `identity_card` -> str | `id_client` -> int      |
| `purchase_price` -> float     | `phone` -> str         | `amount` -> int         |
| `purchase_date` -> datetime   | `credit_card` -> str   | `sale_date` -> datetime |
| `tax` -> float                | `debt` -> float        |                         |
| `location` -> str             |                      |                         |
| `expiration_date` -> datetime |                      |                         |

### Description de Modelos

#### **item:**
* `id`: identificador unico del item, autoincremental
* `name`: nombre del item
* `price`: precio de venta del item
* `purchase_price`: precio de compra del item
* `purchase_date`: fecha en la que se compro el item
* `tax`: impuesto sobre el articulo
* `location`: ubicacion del producto dentro de la tienda
* `expiration_date`: fecha de expiracion del producto

#### **client:**
* `id`: identificador unico del client, autoincremental
* `name`: nombre del client
* `identity_card`: tarjeta de identidad del client
* `phone`: numero de telefono del client
* `credit_card`: tarjeta de credito del client
* `debt`: cantidad que debe a la tienda

#### **sale:**
* `id`: identificador unico del client, autoincremental
* `id_item`: llave foranea al item de la compra
* `id_client`: llave foranea al client de la compra
* `amount`: cantidad del id_item que compra
* `sale_date`: fecha de la venta

***

## Metodos de la API

### Item
1. `[GET]` /items -> Devuelve todos los items almacenados
2. `[GET]` /items/{item_id} -> Devuelve el `Item` correspondiente al valor del `item_id`
3. `[POST]` /items -> Crea un nuevo objeto de tipo `Item` y lo almacena en la DB los datos del `Item` llegan a traves del body en forma de json 
4. `[PUT]` /items/{item_id} -> Hace update de los atributos del objeto `Item` con id correspondiente a `item_id`, los valores de update llegan a traves del body en forma de json 
5. `[DELETE]` /items/{item_id} -> Elimina el objeto de tipo `Item` con id correspondiente a `item_id`
 
### Client
1. `[GET]` /clients -> Devuelve todos los clients almacenados
2. `[GET]` /clients/{clients_id} -> Devuelve el `Client` correspondiente al valor del `client_id`
3. `[POST]` /clients -> Crea un nuevo objeto de tipo `Client` y lo almacena en la DB los datos del `Client` llegan a traves del body en forma de json 
4. `[PUT]` /clients/{clients_id} -> Hace update de los atributos del objeto `Client` con id correspondiente a `client_id`, los valores de update llegan a traves del body en forma de json 
5. `[DELETE]` /clients/{clients_id} -> Elimina el objeto de tipo `Client` con id correspondiente a `client_id`

### Sale
1. `[GET]` /sales -> Devuelve todos los clients almacenados
2. `[GET]` /sales/{sales_id} -> Devuelve el `Sale` correspondiente al valor del `sale_id`
3. `[POST]` /sales -> Crea un nuevo objeto de tipo `Sale` y lo almacena en la DB los datos del `Sale` llegan a traves del body en forma de json 
4. `[PUT]` /sales/{sales_id} -> Hace update de los atributos del objeto `Sale` con id correspondiente a `sale_id`, los valores de update llegan a traves del body en forma de json 
5. `[DELETE]` /sales/{sales_id} -> Elimina el objeto de tipo `Sale` con id correspondiente a `sale_id`
