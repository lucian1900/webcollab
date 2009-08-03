function post(url, data){
    x = new XMLHttpRequest()
    x.onreadystatechange = function(){
        console.log(x.responseText)
    }
    
    x.open('POST', 'http://localhost:5000'+url, true)
    x.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    x.send(data)
}

function delete(url){
    x = new XMLHttpRequest()
    x.onreadystatechange = function() {
        console.log(x.responseText)
    }
    x.open('DELETE', 'http://localhost:5000'+url, true)
    x.send(null)
}