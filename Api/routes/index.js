const express = require('express')// framework
const router = express.Router();//framework function
const user = require('./user')
const card = require('./card')

router.use("/card",card)
router.use("/user",user)

module.exports = router;