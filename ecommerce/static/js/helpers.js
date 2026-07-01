const baseUrl = 'http://127.0.0.1:8000/'

const headers = {
    accept: 'application/json',
    Authorization: `Token ${authToken}`
}

const devolution = async (id) => {
    const endpoint = `${baseUrl}ecommerce/buy-item/${id}`
    const fetchOptions = {
        method: 'DELETE',
        headers: headers
    }
    const response = await fetch(endpoint, fetchOptions)
    let data = await response.json()
    return data
}

const fetchUser = async () => {
    const endpoint = `${baseUrl}accounts/user`
    const fetchOptions = {
        method: 'GET',
        headers: headers
    }
    const response = await fetch(endpoint, fetchOptions)
    let data = await response.json()
    return data
}

const removeItemCart = async (id) => {
    const endpoint = `${baseUrl}ecommerce/add-item/${id}`
    const fetchOptions = {
        method: 'DELETE',
        headers: headers
    }
    const response = await fetch(endpoint, fetchOptions)
    let data = await response.json()
    return data
}

const addItemCart = async (id) => {
    const endpoint = `${baseUrl}ecommerce/add-item/${id}`
    const fetchOptions = {
        method: 'POST',
        headers: headers
    }
    const response = await fetch(endpoint, fetchOptions)
    let data = await response.json()
    return data
}

const buyItem = async (id) => {
    const endpoint = `${baseUrl}ecommerce/buy-item/${id}`
    const fetchOptions = {
        method: 'POST',
        headers: headers
    }
    const response = await fetch(endpoint, fetchOptions)
    let data = await response.json()
    return data
}

const trComponent = (item) => {
    return `<tr>
        <th scope="row">${item.id}</th>
        <td>${item.name}</td>
        <td>${item.description}</td>
        <td style="width: 12rem">${item.categories.map(mapItem => mapItem.replace('.','')).join(', ')}</td>
        <td style="width: 6rem">${Number(item.price).toLocaleString('en-US')}</td>
        <td style="width: 5rem">
            <span id="table-stock-${item.id}">${item.quantity}</span>
            <span class="placeholder col-12 d-none"></span>
        </td>
        <td style="width: 8rem">
            <button class="btn btn-danger" data-class=${item.id}>return</button>
            <button class="btn btn-danger disabled placeholder d-none"></button>
        </td>
    </tr>`
}

const accordionItem = (item, accordionState) => {
    return `<div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${item.id}" aria-expanded="true" aria-controls="collapse${item.id}">
                ${item.name}
            </button>
        </h2>
        <div id="collapse${item.id}" class="accordion-collapse {% if forloop.first %} ${accordionState} {% endif %}" data-bs-parent="#accordionExample">
            <div class="accordion-body">
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">price - ${item.price}</li>
                    <li class="list-group-item">
                        <span>stock - ${item.stock}</span>
                        <span class="placeholder col-12 d-none"></span>
                    </li>
                    <li class="list-group-item">Categories - ${item.categories.map(mapItem => mapItem.replace('.','')).join(', ')}</li>
                    <li class="list-group-item">${item.description}</li>
                    <li class="list-group-item">
                        <button class="btn btn-danger" data-class=${item.id}>remove</button>
                        <button class="btn btn-success" data-class=${item.id}>buy</button>
                        <button class="btn btn-danger disabled placeholder d-none"></button>
                        <button class="btn btn-success disabled placeholder d-none"></button>
                    </li>
                </ul>
            </div>
        </div>
    </div>`
}

const cardItem = (item) => {
    return `
    <div class="col-md-3 pb-3">
        <div class="card">
            <img src=${item.image.replace('https://res.cloudinary.com/de1slf4r1/image/upload/v1/media/','')} class="card-img-top img-card" alt=${item.name}>
            <div class="card-body">
                <h5 class="card-title">${item.id} - ${item.name}</h5>
                <p class="card-text min-h-150">${item.description.slice(0,170)}...</p>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">categories - ${item.categories.map(mapItem => mapItem.replace('.','')).join(', ')}</li>
                    <li class="list-group-item">$ ${Number(item.price).toLocaleString('en-US')}</li>
                    <li class="list-group-item">stock - ${item.stock}</li>
                </ul>
                <button href="#" class="btn btn-primary" id=${item.id}>buy</button>
            </div>
        </div>
    </div>
    `
}

export { devolution, fetchUser, trComponent, removeItemCart, buyItem, accordionItem, cardItem, addItemCart }