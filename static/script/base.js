function currentPage(element) {
    document.querySelector(element).classList.add('chosen')
}

function elem(selector) {
    return document.querySelector(selector);
}

function getElementIndex(element) {
    return Array.from(element.parentNode.children).indexOf(element)
}

Element.prototype.setData = function (name, value) {
    this.dataset[name] = value;
}

Element.prototype.getData = function (name) {
    return this.dataset[name]
}

document.querySelectorAll('.custom_select').forEach(el => {
    let input = document.createElement('input')
    let select = el.querySelector('select')
    input.setAttribute('placeholder', el.dataset['placeholder'])
    el.appendChild(input)
    let select_items = document.createElement('div')
    el.appendChild(select_items)
    input.addEventListener('focus', () => {
        fillSelectItems()
        select_items.classList.remove('hidden')
        let searchValue = el.getData('searchValue')
        if (searchValue) {
            input.value = searchValue
        } else {
            input.value = ''
        }
    })
    input.addEventListener('focusout', ev => {
        select_items.classList.add('hidden')
        let selectedIndex = parseInt(el.getData('selectedIndex'))
        if (selectedIndex || selectedIndex === 0) {
            input.value = select.querySelector(`option:nth-child(${selectedIndex + 1})`).innerText
        } else {
            input.value = ''
        }
    })
    input.addEventListener('input', ev => {
        el.setData('searchValue', input.value)
        fillSelectItems()
    })
    select_items.classList.add('select_items')
    select_items.classList.add('hidden')

    function fillSelectItems() {
        select_items.innerHTML = ''
        let searchValue = el.dataset.searchValue
        if (!searchValue) {
            searchValue = ''
        }
        el.querySelectorAll('select option').forEach(option => {
            if (!option.innerText.toLowerCase().includes(searchValue.toLowerCase())) return
            let option_item = document.createElement('div')
            option_item.classList.add('option_item')
            option_item.dataset.value = option.value
            option_item.innerText = option.innerText
            option_item.addEventListener('mousedown', ev => {
                ev.preventDefault()
                let index = getElementIndex(el.querySelector(`select option[value="${option_item.dataset.value}"]`))
                select.selectedIndex = index
                el.setData('selectedIndex', index)
                el.setData('selectedValue', option_item.dataset.value)
                input.value = ''
                el.setData('searchValue', '')
                input.blur()
            })
            select_items.appendChild(option_item)
        })
        if (!select_items.innerHTML) {
            select_items.innerHTML = '<div>Ничего не найдено</div>'
        }
    }

    fillSelectItems()
})

function toggleMenu() {
    let st = elem('nav').style.display
    if (st == 'none') {
        elem('nav').style.display = 'block'
    } else {
        elem('nav').style.display = 'none'
    }
}