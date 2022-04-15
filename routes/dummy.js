var express = require('express');
var router = express.Router();
const axiosBase = require("axios");
const axios = axiosBase.create({
    baseURL: process.env.ORION_URL || "https://3h23dkp3e1.execute-api.ap-northeast-1.amazonaws.com",
    headers: {
        "Content-Type": "application/json",
    },
    timeout: 1000,
    responseType: "json",
});


router.post('/', function (req, res, next) {
    console.log(req.body)
    axios
        .post(`/v1/update`, {
            dateObserved: req.body.dateObserved.value,
            peopleCount: req.body.peopleCount.value
        })
        .then(function (response) {
            console.log("データ送信が成功しました");
            res.status(200).json({
                message: "OK. Succeeded.",
            });
        })
        .catch(function (err) {
            res.status(500);
            console.log("データ送信に失敗しました", err);
        });
});

module.exports = router;
