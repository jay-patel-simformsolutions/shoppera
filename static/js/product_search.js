window.onload = function (){
	var product_container = document.getElementById('product-container');
	var search_input = document.getElementById('search-input').value;
	// console.log(search_input);
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			// console.log(typeof(this.responseText),this.responseText);
			data = JSON.parse(this.responseText);
			// console.log(typeof(data),data)
			for (product of data){
				console.log(product);
				var product_element = document.getElementById('product-element').cloneNode(true);
				var image_tag = product_element.querySelector('.product-image');
				var product_title = product_element.querySelector('.product-title');
				var product_price = product_element.querySelector('.product-price');
				var product_buy = product_element.querySelector('.product-buy');
				image_tag.setAttribute('src',product['product_primary_image']);
				// console.log(image_tag);
				product_element.style.display = 'inline-block';
				product_title.innerHTML = product['product_title'];
				product_price.innerHTML = 'Rs. ' + product['product_price'];
				product_buy.href += product['id'];
				product_container.appendChild(product_element);
			}
		}
	};
	xhttp.open("GET", "/api-test?search=" + search_input, true);
	xhttp.send();	
}