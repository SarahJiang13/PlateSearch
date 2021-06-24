const form = document.querySelector('#signup-form');

// listen for submit even
form.addEventListener('submit', () => {
    // TODO: submit post request here
});

form.addEventListener('submit', (event) => {

    // disable default action
    event.preventDefault();

    // configure a request
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/signup');

    // prepare form data
    let data = new FormData(form);

    // set headers
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

    // send request
    xhr.send(data);

    // listen for `load` event
    xhr.onload = () => {
        console.log(xhr.responseText);
    }
    
});

form.addEventListener('submit', (event) => {

    // disable default action
    event.preventDefault();
    
    // make post request
    fetch('/signup', {
        method: 'POST',
        body: new FormData(form),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(res => res.text())
    .then(html => console.log(html))
    .catch(err => console.error(err));
});