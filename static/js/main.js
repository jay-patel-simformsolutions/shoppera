function changeQuantity(argument,e) {
	// body...
	var x = {id : argument , lname : String(e.value)}
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
	  let result = JSON.parse(this.responseText);
      document.getElementById("total-amount").innerHTML =
      'Rs.' + result.t_amount;
    }
  };

	xhttp.open("POST", "/cart/change-quantity", true);
  	xhttp.send('{"id" :'+ argument +', "qty" : '+ String(e.value) + '}');
}