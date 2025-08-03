document.getElementById('predict-button').addEventListener('click', async () => {
    const area = document.getElementById('area').value;
    const mzzone = document.getElementById('mzzone').value;
    const sale_cond = document.getElementById('sale_cond').value;
    const n_bedroom = document.getElementById('n_bedroom').value;
    const n_bathroom = document.getElementById('n_bathroom').value;
    const park_facil = document.querySelector('input[name="PARK_FACIL"]:checked') ? 'Yes' : 'No';

    // Basic validation
    if (!area || !mzzone || !sale_cond || !n_bedroom || !n_bathroom) {
        alert('Please select all required fields.');
        return;
    }

    const data = {
        area: area,
        mzzone: mzzone,
        sale_cond: sale_cond,
        n_bedroom: n_bedroom,
        n_bathroom: n_bathroom,
        park_facil: park_facil
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            const price = result.price.toLocaleString('en-IN', { style: 'currency', currency: 'INR' });
            document.getElementById('predicted-price').textContent = price;
            document.getElementById('result-container').style.display = 'block';
        } else {
            alert('Error: ' + result.error);
        }

    } catch (error) {
        console.error('Failed to fetch:', error);
        alert('An unexpected error occurred. Please try again later.');
    }
});