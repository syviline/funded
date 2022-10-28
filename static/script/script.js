const transactionsCtx = document.querySelector('.transactions_canvas').getContext('2d')
const transactionsChart = new Chart(transactionsCtx, {
    type: 'doughnut', data: {
        labels: ['Магазины', 'Бары', 'Еще что-то'],
        datasets: [{
            label: 'My First Dataset',
            data: [300, 50, 100],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
            ],
            hoverOffset: 4,
        }]
    }, options: {responsive: true, borderWidth: 0}
})

const monthTransactionsCanvas = document.querySelector('.month_transactions_canvas').getContext('2d')
const monthTransactions = new Chart(monthTransactionsCanvas, {
    type: 'bar', data: {
        labels: ['Январь', 'Февраль', 'Март', 'Апрель'],
        datasets: [{
            label: 'Траты в месяц',
            data: [48000, 28000, 17000, 50000],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    },
})