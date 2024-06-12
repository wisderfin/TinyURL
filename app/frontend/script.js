var errorElement = document.querySelector('.error');
var responseElement = document.querySelector('.response');
var resultElement = document.getElementById('result');


document.getElementById('go').addEventListener('click', function() {
    var link = document.getElementById('link').value;
    if (link !== null && !link.includes('http://') && !link.includes('https://')) {
        link = 'http://' + link;
    }
    axios.post('http://localhost:8000/compressor/add', {
        full: link
    }, {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        console.log(response.data);
        errorElement.setAttribute('id', 'false');
        var shortUrl = response.data.short; // Получаем значение поля short из ответа
        var fullShortUrl = 'http://localhost:8000/' + shortUrl; 
        document.getElementById('result').value = fullShortUrl;
        responseElement.setAttribute('id', 'true');



    })
    .catch(error => {
        console.error('Ошибка:', error);
        errorElement.setAttribute('id', 'true');
        responseElement.setAttribute('id', 'false');
        
    });
});


document.getElementById('copy').addEventListener('click', async function() {
    var resultField = document.getElementById('result');
    var resultText = resultField.value;
    
    try {
        await navigator.clipboard.writeText(resultText);
        console.log('Текст скопирован в буфер обмена');
    } catch (err) {
        console.error('Ошибка копирования:', err);
    }
});