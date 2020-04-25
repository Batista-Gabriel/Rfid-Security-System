const express = require('express');
const bodyParser = require('body-parser')
const route = require ('./routes')

const app=express();
 
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ 
    extended:true
}))

app.use('/',route)

app.listen('3000')