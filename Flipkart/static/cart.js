var i = 1;
var quantity = document.getElementById('display');
var quantity2 = document.getElementById('quantity');
var quantity3 = document.getElementById('quantity_1');
var item = parseFloat(document.getElementById('price').innerText); 
var total = document.getElementById('total');

document.getElementById('increment').addEventListener('click', function() {
    i++;
    if (i > 5) {
        window.alert('Maximum Limit Reached');
        i = 5; 
    }
    updateQuantityAndTotal();
});

document.getElementById('decrement').addEventListener('click', function() {
    i--;
    if (i < 1) {
        i = 1; 
    }
    updateQuantityAndTotal();
});

function updateQuantityAndTotal() {
    quantity.textContent = i;
    quantity2.textContent= i;
    quantity3.value = i;
    var total_price = `${item * i}`;

    total.textContent = `${total_price}.00`;
    document.getElementById('price_1').value = `${total_price}.00`
    document.getElementById('quantity_1').value = i;
}