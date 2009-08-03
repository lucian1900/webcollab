function xhr(method, url, data){

    
    x.open(method, 'http://localhost:5000'+url, true); 
    x.send(data)
}

function post(url, data){
    x = new XMLHttpRequest(); 
    x.onreadystatechange = function(){
        console.log(x.responseText);
    }
    
    x.open('POST', 'http://localhost:5000'+url, true);
    x.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
    x.send(data)
}