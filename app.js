const express = require('express');
const bodyParser = require('body-parser');
const Spider = require('./db');
const exec = require('child_process').exec;

const app = express();

app.use(express.static('public'))
app.use(bodyParser.json());

app.get('/getInfo', (req, res) => {
  exec('python spider.py', (err, doc) => {
    console.log(doc);
    res.json(doc);
  })
})

app.post('/signin', (req, res) => {
  let userName = req.body.userName;
  let passWord = req.body.passWord;
  Spider.findOne({ userName: userName, passWord: passWord }, (err, doc) => {
    if (doc) {
      res.send('ok')
      return;
    }
    res.send('no');
  })
})

app.post('/signup', async (req, res) => {
  let userName = req.body.userName;
  let request = await Spider.findOne({ userName: userName });
  console.log(request);
  if (request) {
    res.send('no')
    return;
  }
  Spider.create(req.body, (err, doc) => {
    console.log(doc);
  })
  res.send('ok')
})

app.listen(3000, () => {
  console.log('App listening port on 3000!');
})