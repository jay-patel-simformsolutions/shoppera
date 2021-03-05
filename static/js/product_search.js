var back_button = document.querySelector('#back-arrow');

function goBack(){
	this.style.transform = {
		scale: 0.8
	}
	var product_container = document.getElementById('product-container');
	var product_data_element = document.querySelector('#product-data-element');
	product_data_element.style.display = 'none';
	product_container.style.display = 'inline-block';
}


back_button.addEventListener('click', goBack);

function openProduct(){
	console.log('Hello World',this);
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
			data = JSON.parse(this.responseText);
			// console.log(typeof(data),data);
			var product_container = document.getElementById('product-container');
			var product_data_element = document.querySelector('#product-data-element');
			var image_tag = product_data_element.querySelector('#lg-prdct-img');
			var product_data_title = product_data_element.querySelector('#product-data-title');
			var product_data_description = product_data_element.querySelector('#product-data-description');
			var product_data_price = product_data_element.querySelector('#product-data-price');
			var product_data_mrp = product_data_element.querySelector('#product-data-mrp');
			var product_data_button = product_data_element.querySelector('#product-data-button');
			image_tag.src = data['product_primary_image'];
			product_data_title.innerHTML = data['product_title'];
			product_data_description.innerHTML = data['product_description'];
			product_data_price.innerHTML = data['product_price'];
			product_data_mrp.innerHTML = data['product_mrp'];
			product_data_button.href += data['id'];
			product_container.style.display = 'none';
			product_data_element.style.display = 'block';
		}
	}
	xhttp.open('GET','/products/product-data/' + this.id, true);
	xhttp.send();
}


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
				// console.log(product);
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
				product_container.appendChild(product_element);
				// console.log(product_buy);
				product_buy.addEventListener('click', openProduct);
				product_buy.setAttribute('id', product['id']);
			}
		}
	};
	xhttp.open("GET", "/api-test?search=" + search_input, true);
	xhttp.send();	
}