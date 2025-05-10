fetch('/data')
    .then(response => response.json())
    .then(data => {
        const labels = data.labels;
        const values = data.values;

        new Chart(document.getElementById("myChart"), {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Sample Data',
                    data: values,
                    borderColor: 'green',
                    fill: false
                }]
            }
        });
    })
    .catch(err => console.error("Fetch Error:", err));
