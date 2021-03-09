var price_from = document.querySelector('#price-from');

function updateFrom(){
	console.log('________',this.value);
	let x = document.querySelector('#from');
	x.innerHTML = this.value;
}

price_from.addEventListener('change', updateFrom);


var price_to = document.querySelector('#price-to');

function updateTo(){
	console.log('________',this.value);
	let x = document.querySelector('#to');
	x.innerHTML = this.value;
}

price_to.addEventListener('change', updateTo);


var filter_button = document.querySelector('#filter-button');

function applyFilter(){
	// console.log('Hello From applyFilter');
	// console.log(price_from,price_to);
	var price_from = document.querySelector('#price-from').value;
	var price_to = document.querySelector('#price-to').value;
	var color_select = document.querySelector('#color-select').value;
	var products_section = document.querySelector('#products-section');
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
			console.log(this.responseText);
			products_section.innerHTML = this.responseText;
		}
	}
	xhttp.open('GET','products/filter-products?price_from=' + price_from + '&price_to=' + price_to + '&color=' + color_select, true);
	xhttp.send();
}


filter_button.addEventListener('click',applyFilter)