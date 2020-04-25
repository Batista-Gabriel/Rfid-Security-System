const express = require('express')
const router = express.Router();
const cardController = require('../controllers/cardController')

router.post('/',cardController.create)
router.get('/',cardController.index)
router.get('/:id',cardController.card) //this card info
router.get('/thiscarduser/:id',cardController.cardUser) //user info
router.delete('/:id',cardController.delete)

module.exports = router;