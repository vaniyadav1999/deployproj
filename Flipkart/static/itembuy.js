let cost = document.getElementById('price').textContent
console.log(Number(cost))
let quantity = document.getElementById('quantity').textContent
console.log(Number(quantity))
document.getElementById('total_price').textContent = `${Number(cost)*Number(quantity)}.00 ₹`
            