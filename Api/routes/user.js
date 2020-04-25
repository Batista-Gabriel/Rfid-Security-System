const express = require('express')// framework
const router = express.Router();//framework function
const userController = require('../controllers/userController')
router.get('/',userController.index)
router.get('/:id',userController.user) //get user by id
router.get('/byname/:userName',userController.search) //get user by name
router.post('/',userController.create)
router.patch('/:id',userController.patch) 
router.delete('/:id',userController.delete) 

module.exports =router;