console.log('Hola')

let lastScrollTop = 0;
const header = document.querySelector('.header');

window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop > lastScrollTop) {
        // Прокрутка вниз - скрыть хедер
        header.classList.add('hidden-header');
    } else {
        // Прокрутка вверх - показать хедер
        header.classList.remove('hidden-header');
    }
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // Учитываем возможные отрицательные значения
});
