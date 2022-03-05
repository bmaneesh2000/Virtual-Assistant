var exp = require('express')
var app= exp()
app.get('/',function(req,res){
    res.send('konichiwa sekai')
});
app.listen(7373);