var express = require('express');
var router = express.Router();
const { Client } = require('pg');

router.post('/', function(req, res) {

	res.send({test: 'test'});

});

module.exports = router;  
