var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next){
    stocks = [
        {
            'url':'',
            'title':'AGTC',
            'open': 4.7,
            'price': 4.8,
            'volume': 45239,
            'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
            'reason':'recommand'
        },
        {
            'url':'',
            'title':'AGTC',
            'open': 4.7,
            'price': 4.8,
            'volume': 45239,
            'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
            'reason':'hot'
        }];
        res.json(stocks);
});

module.exports = router;