import { devolution, fetchUser, trComponent, buyItem, removeItemCart } from "./helpers.js";

// user´s balance container
const balance = document.getElementById('balance')
const balanceSpan = document.getElementById('balance-span')

// accordion container
const accordion = document.getElementById('accordionExample')
accordion.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', async function() {
        let response
        const ul = this.closest('ul')
        const liStock = ul.children[1]
        const bgStock = liStock.children[1]
        const stock = liStock.children[0]
        const li = this.closest('li')
        //
        const successBtn = li.querySelector('.btn-success')
        const dangerBtn = li.querySelector('.btn-danger')
        const bgSuccessBtn = li.querySelector('.btn-success.disabled')
        const bgDangerBtn = li.querySelector('.btn-danger.disabled')
        //
        bgSuccessBtn.classList.toggle('d-none')
        bgDangerBtn.classList.toggle('d-none')
        successBtn.classList.toggle('d-none')
        dangerBtn.classList.toggle('d-none')
        stock.classList.toggle('d-none')
        bgStock.classList.toggle('d-none')
        //
        const action = this.textContent
        const id = this.dataset.class
        const accordionItem = document.getElementById(`accordion-${id}`)
        //
        if(action == 'remove'){
            response = await removeItemCart(id)
        }else{
            balance.classList.toggle('d-none')
            balanceSpan.classList.toggle('d-none')
            response = await buyItem(id)
            //
            if(response['new_collection_item']){
                const user = await fetchUser()
                const collection = user['collection']
                const newItem = collection[collection.length-1]
                tbody.innerHTML += trComponent(newItem)
            }else{
                const tableStock = document.getElementById(`table-stock-${id}`)
                tableStock.innerText = response['stock_collection']
            }
            //
            balance.innerText = Number(response['balance']).toLocaleString('en-US', {
                style: 'currency',
                currency: 'USD',
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            })
            balance.classList.toggle('d-none')
            balanceSpan.classList.toggle('d-none')
        }

        if('stock_cart' in response){
            stock.innerText = `stock - ${response['stock_cart']}`
            bgSuccessBtn.classList.toggle('d-none')
            bgDangerBtn.classList.toggle('d-none')
            successBtn.classList.toggle('d-none')
            dangerBtn.classList.toggle('d-none')
            stock.classList.toggle('d-none')
            bgStock.classList.toggle('d-none')
        }else{
            accordionItem.remove()
        }
    });
});

// tbody container
const tbody = document.querySelector('tbody')
tbody.addEventListener('click', async (e) => {
    if(e.target.classList.contains('btn')){
        const tr = e.target.closest('tr')
        const td = tr.children[5]
        const tdButton = tr.children[6]
        const stock = td.children[0]
        const span = td.children[1]
        const id = e.target.dataset.class
        //
        balance.classList.toggle('d-none')
        balanceSpan.classList.toggle('d-none')
        stock.classList.toggle('d-none')
        span.classList.toggle('d-none')
        tdButton.classList.toggle('d-none')
        //* await function
        const response = await devolution(id)
        if('stock_collection' in response){
            //* rewrite damaged components
            stock.innerText = response['stock_collection']
            //
            stock.classList.toggle('d-none')
            span.classList.toggle('d-none')
            tdButton.classList.toggle('d-none')
        }else{
            tr.remove()
        }
        //
        balance.innerText = Number(response['balance']).toLocaleString('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        })
        balance.classList.toggle('d-none')
        balanceSpan.classList.toggle('d-none')
    }
})