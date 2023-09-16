/**
 * in stock
 */
import { createClient } from 'redis';
import {promisify} from 'util';
const express = require('express');
const redis_client = createClient()

const redis_get_promise = promisify(redis_client.get).bind(redis_client)
//data
const listProducts = [
    { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
  ];

function getItemById(id){
    return listProducts.filter((item) => item.id === id)[0]
}
// the server running on port 1245

const PORT = 1245
const app = express()
// get a json of list_products
app.get('/list_products', (req, rep) => {
    return rep.json(listProducts)
})



function reserveStockById(itemId, stock){
    redis_client.set(itemId, stock)
}
reserveStockById(1,{ Id: 1, name: 'Suitcase 250', price: 50, stock: 4 }.toString() )

async function getCurrentReservedStockById(itemId){
    const stock = await redis_get_promise(itemId);
    return stock;
}
app.get('/list_products/:itemId', async(req, res) => {
    const itemId = parseInt(req.params.itemId)
    const prod = getItemById(itemId)

    if (prod) {
        const reserve = await getCurrentReservedStockById(itemId)
        prod.currentQuantity = reserve

        res.statusCode = 200
        res.json(prod)
    }else {
        res.statusCode = 404;
        res.send({"status":"Product not found"})
    }
})
app.get('/reserve_product/:itemId', (req, res) => {
    const item = getItemById(parseInt(req.params.itemId))

    if (item) {
        if (item.stock >= 1) {
            reserveStockById(item.Id, 1)
            res.statusCode = 200
            res.send({"status":"Reservation confirmed","itemId":item.Id})
        }else {
            res.statusCode = 403
            res.send({"status":"Not enough stock available","itemId": item.Id})
        }
    }else {
        res.statusCode = 404
        res.send({"status":"Product not found"})
    }
})
app.listen(PORT, () => {
    console.log('Listening on port: ' + PORT)
})
