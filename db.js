const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/spider', { useNewUrlParser: true })

let spiderSchema = new mongoose.Schema({
    userName: String,
    passWord: String
})

module.exports = mongoose.model('spider', spiderSchema)