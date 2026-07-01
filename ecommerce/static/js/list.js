import { cardItem, addItemCart } from "./helpers.js";

let min = 8
let max = 16

let row = document.getElementById('queryset-row')

const addItemsButton = document.querySelector('.btn-success')
const shorterListButton = document.querySelector('.btn-danger')

row.addEventListener('click', async (e) => {
    if (e.target.classList.contains('btn')) {
        let response
        const id = e.target.id
        const divParent = e.target.closest('.col-md-3')
        const stock = divParent.children[0].children[1].children[2].children[2]
        response = await addItemCart(id)
        if('stock_cart' in response){
            stock.innerText = `stock - ${response['stock_gallery']}`
        }else{
            stock.innerText = 'sold out item'
        }
    }
});

addItemsButton.addEventListener('click', () =>{
    queryset.slice(min,max).map((item) => {
        row.innerHTML += cardItem(item)
    })
    min += 8
    max += 8
})

shorterListButton.addEventListener('click', () =>{
    for(let i=8; i--; i==0){
        row.lastElementChild.remove()
    }
    min -= 8
    max -= 8
})