console.log('hello')
const forms = document.querySelectorAll('form');

forms.forEach(
    el => el.addEventListener('submit', onSubmit)
)

function onSubmit(e) {
    e.preventDefault();
}

