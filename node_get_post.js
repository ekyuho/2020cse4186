const express = require('express')
const app = express()
app.use(express.json())
require('date-utils')
port = 8000

app.get('/capston2020', function(req, res) {
    r = req.query
    r.ip = req.ip.replace(/^.*:/, '')
    r.time = (new Date()).toFormat("YYYY-MM-DD HH:MI:SS")
    r.email = "ekyuho@gmail.com"
    r.stuno = "20202030"
    console.log(r)
    res.send(JSON.stringify(r))
})

app.post('/capston2020', function(req, res) {
    r = req.body
    r.ip = req.ip.replace(/^.*:/, '')
    r.time = (new Date()).toFormat("YYYY-MM-DD HH:MI:SS")
    r.email = "ekyuho@gmail.com"
    r.stuno = "20202030"
    console.log(req.body)
    res.send(JSON.stringify(r))
})

app.get('/capston2020/:a/:b', function(req, res) {
    r = req.params
    ip = req.ip.replace(/^.*:/, '')
    r.time = (new Date()).toFormat("YYYY-MM-DD HH:MI:SS")
    r.email = "ekyuho@gmail.com"
    r.stuno = "20202030"
    console.log(r)
    res.send(JSON.stringify(r))
})
